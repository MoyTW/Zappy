__author__ = 'Travis Moy'

import pyglet
import warnings
import entity.actor.Actor as Actor


class Cell(object):
    DEFAULT_IMAGE_PATH = 'images/defaults/defaultcell.png'
    LOADER = pyglet.resource.Loader(['@assets'])

    def __init__(self, _image_location=DEFAULT_IMAGE_PATH, _passable=True, _transparent=True):
        self._passable = _passable
        self._transparent = _transparent
        self._contains = []
        self._image_location = _image_location

        self._image = None
        self._load_image(_image_location)

    def get_passable(self):
        return self._passable

    def get_transparent(self):
        return self._transparent

    def set_passable(self, _passable):
        self._passable = _passable

    def set_transparent(self, _transparent):
        self._transparent = _transparent

    def change_cell_image_by_image(self, _image):
        self._image = _image

    def change_cell_image_by_location(self, _image_location):
        self._image_location = _image_location
        self._load_image(_image_location)

    # Returns a map. Key is priority, contents are lists of images.
    def get_display_images(self, _in_fow=False):
        display_dict = dict()
        display_dict[-1] = [self._image]
        for entity in self._contains:
            if not (_in_fow and isinstance(entity, Actor.Actor)):
                try:
                    priority = entity.get_priority()
                    image = entity.get_image()
                    if priority in display_dict.keys():
                        display_dict[priority].append(image)
                    else:
                        display_dict[priority] = [image]
                except AttributeError as e:
                    print e.message
        return display_dict

    # Don't store the result of this function! It is for looking, not touching!
    def get_all_entities(self):
        return self._contains

    def add_entity(self, _entity):
        self._contains.append(_entity)

    def remove_entity(self, _entity):
        try:
            self._contains.remove(_entity)
            return True
        except ValueError:
            return False

    def contains_entity(self, _entity):
        return _entity in self._contains

    # Searches for file in local, then in assets, then tries to load default.
    # If for some reason the default is absent, throws an exception.
    def _load_image(self, _filename):
        try:
            self._image = pyglet.resource.image(_filename)
        except pyglet.resource.ResourceNotFoundException:
            try:
                self._image = self.LOADER.image(_filename)
            except pyglet.resource.ResourceNotFoundException:
                warnings.warn("Error loading specified Cell image, attempting to load default Cell image.")
                self._image = self.LOADER.image(self.DEFAULT_IMAGE_PATH)

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
            return self._passable == other._passable and self._image_location == other._image_location\
                and contains_equality
        except AttributeError as e:
            return False

    def __repr__(self):
        return "(P: {0} I: {1} C: {2})".format(self._passable, self._image_location, self._contains)