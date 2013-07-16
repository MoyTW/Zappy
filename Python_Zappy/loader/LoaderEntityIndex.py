__author__ = 'Travis Moy'

import pyglet
import entity.Entity
import z_json
import warnings


class LoaderEntityIndex(object):

    def __init__(self):
        self._loader = pyglet.resource.Loader('@assets.entities')
        self._template_dict = dict()

    def get_list_of_loaded_templates(self):
        return self._template_dict.keys()

    def get_template(self, template_name):
        return self._template_dict.get(template_name)

    # Consults dict; if not in dict, load. If in dict, create new instance, return
    # entity_dict is filled with Template objects
    # Call Template.create_instance(level, self)
    def create_entity_by_name(self, name, lvl_view):
        """
        :type name: str
        :type lvl_view: level.LevelView.LevelView
        """
        eid = self._get_and_increment_eid(lvl_view)

        if name not in self._template_dict:
            self._load_template_by_name(name)

        if self._template_dict[name] is None:
            ret_ent = entity.Entity.Entity(_eid=eid, _level=lvl_view,
                                           _entity_name='No Entity In Index With Name {0}'.format(name),
                                           _image_name=None)
        else:
            ret_ent = self._template_dict[name].create_instance(eid=eid, level=lvl_view, entity_index=self)

        return ret_ent

    # Takes a list of TemplateTools or strings.
    def create_tool_list(self, tools, user, lvl_view):
        """
        :type tools: list
        :type user: entity.actor.Actor.Actor
        :type lvl_view: level.LevelView.LevelView
        """
        if tools is None:
            return []

        tool_list = list()

        for t in tools:
            # First, try to use it as a template.
            try:
                instance = t.create_instance(eid=self._get_and_increment_eid(lvl_view), level=lvl_view,
                                             entity_index=self, user=user)
            except AttributeError:
                # If that fails, try to load it by name.
                instance = self.create_entity_by_name(name=t, lvl_view=lvl_view)
            # Append the result to the list
            tool_list.append(instance)

        return tool_list

    def _get_and_increment_eid(self, level):
        try:
            eid = level.max_eid
            level.max_eid += 1
        except AttributeError:
            warnstr = str(level) + 'parameter to create_entity_name has no max_eid attribute! Defaulting to -1.'
            warnings.warn(warnstr)
            eid = -1
        return eid

    # Attempt to load name using loader; if cannot find or error in conversion, defaults to None
    def _load_template_by_name(self, name):
        try:
            json = self._loader.text(name).text
            template = z_json.JSONCONVERTER.simple_to_custom_object(json_string=json)
            self._template_dict[name] = template
        except (pyglet.resource.ResourceNotFoundException, z_json.JsonConverterException) as e:
            warnings.warn(e)
            self._template_dict[name] = None