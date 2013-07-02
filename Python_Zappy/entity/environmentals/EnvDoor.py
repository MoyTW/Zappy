__author__ = 'Travis Moy'

import entity.environmentals.Environmental as Environmental


# The unstable floor will collapse when destroyed, killing everything above it and leaving an impassable tile.
class EnvDoor(Environmental.Environmental):

    def __init__(self, _level, _entity_name='Default Door', _max_hp=100,
                 _open_image_location=None,
                 _closed_image_location=None,
                 _is_open=False,
                 **kwargs):
        super(EnvDoor, self).__init__(_level=_level, _entity_name=_entity_name, _max_hp=_max_hp, **kwargs)
        self._is_open = _is_open
        self._open_image_location = _open_image_location
        self._closed_image_location = _closed_image_location
        self._open_image = self._load_return_image(_open_image_location)
        self._closed_image = self._load_return_image(_closed_image_location)

        if self._is_open:
            self.entity_image = self._open_image
        else:
            self.entity_image = self._closed_image

    def trigger(self):
        if self._is_open:
            self.close()
        else:
            self.open()

    def destroy(self):
        print self.entity_name, 'was destroyed!'
        self.open()
        self._level.remove_entity_from(self, *self.get_coords())

    def open(self):
        print self.entity_name, 'is now open!'
        self._is_open = True
        cell = self._level.get_cell_at(*self.get_coords())
        cell.is_passable = True
        cell.is_transparent = True
        self.entity_image = self._open_image

    def close(self):
        print self.entity_name, ' is not closed!'
        self._is_open = False
        cell = self._level.get_cell_at(*self.get_coords())
        cell.is_passable = False
        cell.is_transparent = False
        self.entity_image = self._closed_image