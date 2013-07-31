__author__ = 'Travis Moy'

import pyglet
import warnings


class Cell(object):
    DEFAULT_IMAGE_PATH = 'images/defaults/defaultcell.png'
    LOADER = pyglet.resource.Loader(['@assets'])

    def __init__(self, _image_location=DEFAULT_IMAGE_PATH, _passable=True, _transparent=True):
        """
        :type _image_location: str
        :type _passable: bool
        :type _transparent: bool
        """
        self.is_passable = _passable
        self.is_transparent = _transparent
        self._contains = []
        self._image_location = _image_location

        self._image = None
        self._load_image(_image_location)

    def change_cell_image_by_image(self, _image):
        self._image = _image

    def change_cell_image_by_location(self, _image_location):
        self._image_location = _image_location
        self._load_image(_image_location)

    # Returns a map. Key is priority, contents are lists of images.
    def get_display_images(self, _in_fow=False):
        """
        :type _in_fow: bool
        :rtype: dict
        """
        warnings.warn("Checking hasattr(entity, 'max_moves') to see if it's an Actor or not!")
        display_dict = dict()
        display_dict[-1] = [self._image]
        for entity in self._contains:
            if not (_in_fow and hasattr(entity, 'max_moves')):
                try:
                    priority = entity.PRIORITY
                    image = entity.entity_image
                    if priority in display_dict.keys():
                        display_dict[priority].append(image)
                    else:
                        display_dict[priority] = [image]
                except AttributeError as e:
                    warnings.warn(e.message)
        return display_dict

    # Don't store the result of this function! It is for looking, not touching!
    def get_all_entities(self):
        """:rtype: list"""
        return self._contains

    def add_entity(self, _entity):
        """:type _entity: entity.Entity.Entity"""
        self._contains.append(_entity)

    def remove_entity(self, _entity):
        """
        :type _entity: entity.Entity.Entity
        :rtype: bool
        """
        try:
            self._contains.remove(_entity)
            return True
        except ValueError:
            return False

    def contains_eid(self, eid):
        """
        :type eid: int
        :rtype: bool
        """
        for e in self._contains:
            if e.eid == eid:
                return True
        return False

    def contains_entity(self, _entity):
        """
        :type _entity: entity.Entity.Entity
        :rtype: bool
        """
        return _entity in self._contains

    # Searches for file in local, then in assets, then tries to load default.
    # If for some reason the default is absent, throws an exception.
    def _load_image(self, _filename):
        """:type _filename: str"""
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
        """
        :type other: Cell
        :rtype: bool
        """
        try:
            self_dict = self.__dict__.copy()
            other_dict = other.__dict__.copy()
            self_contains = self_dict.pop('_contains')
            other_contains = other_dict.pop('_contains')
            return sorted(self_contains) == sorted(other_contains) and self_dict == other_dict
        except AttributeError:
            return False

    def __repr__(self):
        return "(P: {0} I: {1} C: {2})".format(self.is_passable, self._image_location, self._contains)