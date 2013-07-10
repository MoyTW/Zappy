__author__ = 'Travis Moy'

import pyglet
import entity.Entity
import z_json
import warnings


class LoaderEntityIndex(object):

    def __init__(self):
        self._loader = pyglet.resource.Loader('@assets.entities')
        self._template_dict = dict()
        self._current_eid = 0

    def reset_entity_ids(self):
        self._current_eid = 0

    def get_list_of_loaded_templates(self):
        return self._template_dict.keys()

    def get_template(self, template_name):
        return self._template_dict.get(template_name)

    # Consults dict; if not in dict, load. If in dict, create new instance, return
    # entity_dict is filled with Template objects
    # Call Template.create_instance(level, self)
    def create_entity_by_name(self, name, level):
        if name not in self._template_dict:
            self._load_template_by_name(name)

        if self._template_dict[name] is None:
            ret_ent = entity.Entity.Entity(_eid=self._current_eid, _level=level,
                                           _entity_name='No Entity In Index With Name {0}'.format(name),
                                           _image_name=None)
        else:
            ret_ent = self._template_dict[name].create_instance(self._current_eid, level=level, entity_index=self)
        self._current_eid += 1

        return ret_ent

    # Takes a list of TemplateTools or strings.
    def create_tool_list(self, tools, user, level):
        if tools is None:
            return []

        tool_list = list()

        for t in tools:
            # First, try to use it as a template.
            try:
                instance = t.create_instance(eid=self._current_eid, level=level, entity_index=self, user=user)
            except AttributeError:
                # If that fails, try to load it by name.
                instance = self.create_entity_by_name(name=t, level=level)
            # Append the result to the list
            tool_list.append(instance)
            self._current_eid += 1

        return tool_list

    # Attempt to load name using loader; if cannot find or error in conversion, defaults to None
    def _load_template_by_name(self, name):
        try:
            json = self._loader.text(name).text
            template = z_json.JSONCONVERTER.simple_to_custom_object(json_string=json)
            self._template_dict[name] = template
        except (pyglet.resource.ResourceNotFoundException, z_json.JsonConverterException) as e:
            warnings.warn(e)
            self._template_dict[name] = None