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
    def create_entity_by_name(self, name, level):
        if name not in self._template_dict:
            self._load_template_by_name(name)

        if self._template_dict[name] is None:
            ret_ent = entity.Entity.Entity(_level=level, _entity_name='No Entity In Index With Name {0}'.format(name),
                                           _image_name=None)
        else:
            ret_ent = self._template_dict[name].create_instance(level=level, entity_index=self)
        return ret_ent

    # Attempt to load name using loader; if cannot find or error in conversion, defaults to None
    def _load_template_by_name(self, name):
        try:
            json = self._loader.text(name).text
            template = z_json.JSONCONVERTER.simple_to_custom_object(json_string=json)
            self._template_dict[name] = template
        except (pyglet.resource.ResourceNotFoundException, z_json.JsonConverterException) as e:
            print e.message
            warnings.warn(e.message)
            self._template_dict[name] = None