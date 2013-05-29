__author__ = 'Travis Moy'

import pyglet
import warnings


class Entity(object):
    DEFAULT_IMAGE_PATH = 'images/defaults/default_entity.png'
    IMAGE_FOLDER = 'images/entities/'

    def __init__(self, image_name):
        self._image_name = image_name

        self._image = None
        self._load_image()

    def _load_image(self):
        loader = pyglet.resource.Loader('@assets')
        try:
            self._image = loader.image('{0}{1}'.format(self.IMAGE_FOLDER, self._image_name))
        except pyglet.resource.ResourceNotFoundException as e:
            warnstr = 'Cannot load image {0}; attemping to load default entity image.'.format(self._image_name)
            warnings.warn(warnstr, RuntimeWarning)
            self._image = loader.image(self.DEFAULT_IMAGE_PATH)