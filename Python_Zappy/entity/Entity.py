__author__ = 'Travis Moy'

import pyglet
import warnings


class Entity(object):
    DEFAULT_IMAGE_PATH = 'images/defaults/default_entity.png'
    IMAGE_FOLDER = 'images/entities/'
    # The higher the priority, the later the Entity is drawn.
    _priority = 0

    def __init__(self, _image_name, _level, _x=-1, _y=-1, _entity_name='Default Entity Name', **kwargs):
        super(Entity, self).__init__(**kwargs)
        self._image_name = _image_name
        self._level = _level
        self._entity_name = _entity_name

        self._x = _x
        self._y = _y

        self._image = self._load_return_image(self._image_name)

    def destroy(self):
        self._level.remove_entity_from(self, self._x, self._y)

    def get_name(self):
        return self._entity_name

    def get_coords(self):
        return self._x, self._y

    def set_coords(self, _x, _y):
        self._x = _x
        self._y = _y

    def get_image(self):
        return self._image

    def get_priority(self):
        return self._priority

    def _load_return_image(self, _image_name):
        loader = pyglet.resource.Loader('@assets')

        if self._image_name is None:
            self._image = loader.image(self.DEFAULT_IMAGE_PATH)

        image_path = '{0}{1}'.format(self.IMAGE_FOLDER, _image_name)
        try:
            return loader.image(image_path)
        except pyglet.resource.ResourceNotFoundException:
            warnings.warn('Cannot load image {0}; attemping to load default entity image.'.format(image_path),
                          RuntimeWarning)
            return loader.image(self.DEFAULT_IMAGE_PATH)