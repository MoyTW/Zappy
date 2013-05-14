__author__ = 'Travis Moy'

import pyglet
import warnings


class Cell(object):
    DEFAULT_IMAGE_PATH = 'images/defaults/defaultcell.png'

    def __init__(self, image_file=DEFAULT_IMAGE_PATH, passable=True):
        self._passable = passable
        self._contains = []
        self._image_file = image_file

        self._load_image(image_file)

    def get_cell_image(self):
        pass

    def get_passable(self):
        pass

    # Returns a CellImages object.
    def get_all_cell_images(self):
        pass

    # Don't store the result of this function! It is for looking, not touching!
    def get_all_entities(self):
        pass

    def add_entity(self, entity):
        #self._contains.append(entity)
        pass

    def remove_entity(self, entity):
        pass

    def contains_entity(self, entity):
        pass

    def _load_image(self, file):
        try:
            self._image = pyglet.resource.image(file)
        except pyglet.resource.ResourceNotFoundException:
            try:
                warnings.warn("Error loading specified Cell image, attempting to load default Cell image.")
                self._image = pyglet.resource.image(self.DEFAULT_IMAGE_PATH)
            except pyglet.resource.ResourceNotFoundException:
                warnings.warn("Error loading default Cell image.")
                self._image = None

    def __eq__(self, other):
        if other is None:
            return False
        return self.__dict__ == other.__dict__