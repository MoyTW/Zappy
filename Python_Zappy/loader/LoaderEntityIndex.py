__author__ = 'Travis Moy'

import pyglet


class LoaderEntityIndex(object):

    def __init__(self):
        self._loader = pyglet.resource.Loader('@assets.entities')

    def create_entity_by_name(self, name):
        pass

    def _load_entity_by_name(self, name):
        pass