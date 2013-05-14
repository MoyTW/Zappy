__author__ = 'Travis Moy'

import pyglet
import warnings


class Cell(object):
    DEFAULT_IMAGE_PATH = 'images/defaults/defaultcell.png'

    def __init__(self, image_file=DEFAULT_IMAGE_PATH, passable=True):
        self._passable = passable
        self._contains = []
        self._image_file = image_file

        try:
            self._image = pyglet.resource.image(image_file)
        except pyglet.resource.ResourceNotFoundException:
            try:
                warnings.warn("Error loading specified Cell image, attempting to load default Cell image.")
                self._image = pyglet.resource.image(self.DEFAULT_IMAGE_PATH)
            except pyglet.resource.ResourceNotFoundException:
                warnings.warn("Error loading default Cell image.")
                self._image = None

    def get_cell_image(self):
        pass

    def get_passable(self):
        pass

    def get_mobile_image(self):
        pass

    # Returns the image to be displayed on screen. Higher-order images are overlaid on lower-order ones as follows:
    # Mobile -> Tool -> Consumable -> Environmental -> Cell
    # If there are multiple Mobiles, nests a +n image in the lower-right corner.
    def get_display_image(self):
        pass

    # Don't store the result of this function! It is for looking, not touching!
    def get_all_entities(self):
        pass

    def add_entity(self):
        pass

    def remove_entity(self):
        pass

    def contains_entity(self, entity):
        pass

    def __eq__(self, other):
        if other is None:
            return False
        return self.__dict__ == other.__dict__