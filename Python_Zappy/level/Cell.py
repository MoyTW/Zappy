__author__ = 'Travis Moy'

import pyglet
import warnings
import collections


class Cell(object):
    DEFAULT_IMAGE_PATH = 'images/defaults/defaultcell.png'

    def __init__(self, image_file=DEFAULT_IMAGE_PATH, passable=True):
        self._passable = bool(passable)
        self._contains = []
        self._image_file = image_file

        self._load_image(image_file)

    def get_cell_image(self):
        return self._image

    def get_passable(self):
        return self._passable

    # Returns a CellImages object.
    def get_all_cell_images(self):
        pass

    # Don't store the result of this function! It is for looking, not touching!
    def get_all_entities(self):
        return self._contains

    def add_entity(self, entity):
        self._contains.append(entity)

    def remove_entity(self, entity):
        try:
            self._contains.remove(entity)
            return True
        except ValueError:
            return False

    def contains_entity(self, entity):
        return entity in self._contains

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

    def __ne__(self, other):
        return not self.__eq__(other)

    def __eq__(self, other):
        if other is None:
            return False

        contains_equality = True
        try:
            for s, o in zip(self._contains, other._contains):
                if s != o:
                    contains_equality = False
            return self._passable == other._passable and self._image_file == other._image_file and contains_equality
        except AttributeError:
            return False

    def __repr__(self):
        return "(P: {0} I: {1} C: {2})".format(self._passable, self._image_file, self._contains)