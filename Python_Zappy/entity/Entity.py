__author__ = 'Travis Moy'

import pyglet
import warnings
from level.commands.CompoundCmd import CompoundCmd
from level.commands.command_fragments import LevelRemoveEntity


class Entity(object):
    DEFAULT_IMAGE_PATH = 'images/defaults/default_entity.png'
    IMAGE_FOLDER = 'images/entities/'
    # The higher the priority, the later the Entity is drawn.
    PRIORITY = 0

    def __init__(self, _eid, _level, _image_name=None, _entity_name='Default Entity Name', **kwargs):
        """
        :type _eid: int
        :type _level: level.LevelView.LevelView
        :type _image_name: str
        :type _entity_name: str
        """
        super(Entity, self).__init__(**kwargs)
        self.eid = _eid
        self.entity_name = _entity_name

        self._image_name = _image_name
        self._level = _level

        self._x = -1
        self._y = -1

        self.entity_image = self._load_return_image(self._image_name)

    def is_player_controlled(self):
        return False

    def destroy(self):
        self._level.add_command(CompoundCmd("{0} has been destroyed!".format(self.entity_name),
                                            LevelRemoveEntity(self.eid, self._level)))

    def get_coords(self):
        return self._x, self._y

    def set_coords(self, _x, _y):
        self._x = _x
        self._y = _y

    def _load_return_image(self, _image_name):
        loader = pyglet.resource.Loader('@assets')

        if self._image_name is None:
            self.entity_image = loader.image(self.DEFAULT_IMAGE_PATH)

        image_path = '{0}{1}'.format(self.IMAGE_FOLDER, _image_name)
        try:
            return loader.image(image_path)
        except pyglet.resource.ResourceNotFoundException:
            warnings.warn('Cannot load image {0}; attemping to load default entity image.'.format(image_path),
                          RuntimeWarning)
            return loader.image(self.DEFAULT_IMAGE_PATH)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __eq__(self, other):
        """
        :type other: Entity
        :rtype: bool
        """
        try:
            return self.eid == other.eid and self._image_name == other._image_name and \
                self.entity_name == other.entity_name
        except AttributeError:
            return False

    def __repr__(self):
        return "id={0}, {1} at ({2}, {3})".format(self.eid, self.entity_name, self._x, self._y)