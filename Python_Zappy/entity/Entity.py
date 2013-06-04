__author__ = 'Travis Moy'

import pyglet
import warnings


class Entity(object):
    DEFAULT_IMAGE_PATH = 'images/defaults/default_entity.png'
    IMAGE_FOLDER = 'images/entities/'
    _priority = 0

    def __init__(self, image_name, level):
        self._image_name = image_name
        self._level = level

        self._image = None
        self._load_image()

    def get_image(self):
        return self._image

    def get_priority(self):
        return self._priority

    def _load_image(self):
        loader = pyglet.resource.Loader('@assets')

        if self._image_name is None:
            self._image = loader.image(self.DEFAULT_IMAGE_PATH)

        image_path = '{0}{1}'.format(self.IMAGE_FOLDER, self._image_name)
        try:
            self._image = loader.image(image_path)
        except pyglet.resource.ResourceNotFoundException:
            warnings.warn('Cannot load image {0}; attemping to load default entity image.'.format(image_path),
                          RuntimeWarning)
            self._image = loader.image(self.DEFAULT_IMAGE_PATH)