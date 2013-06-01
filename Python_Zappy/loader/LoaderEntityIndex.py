__author__ = 'Travis Moy'

import pyglet


class LoaderEntityIndex(object):

    def __init__(self, level):
        self._level = level

        self._loader = pyglet.resource.Loader('@assets.entities')
        self._template_dict = dict()

    def get_list_of_loaded_templates(self):
        return self._template_dict.keys()

    def get_template(self, template_name):
        return self._template_dict().get(template_name)

    # Consults dict; if not in dict, load. If in dict, create new instance, return
    # entity_dict is filled with Template objects
    # Call Template.create_instance(level, self)
    def create_entity_by_name(self, name):
        pass

    # Attempt to load name using loader
    # Create Template from json, push onto dict
    def _load_template_by_name(self, name):
        pass