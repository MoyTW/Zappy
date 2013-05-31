__author__ = 'Travis Moy'

import pyglet


class LoaderEntityIndex(object):

    def __init__(self, level):
        self._level = level

        self._loader = pyglet.resource.Loader('@assets.entities')
        self._entity_dict = dict()

    # Consults dict; if not in dict, load. If in dict, create new instance, return
    # entity_dict is filled with Template objects
    # Call Template.create_instance(level, self)
    def create_entity_by_name(self, name):
        pass

    # Attempt to load name using loader
    # Create Template from json, push onto dict
    def _load_entity_by_name(self, name):
        pass