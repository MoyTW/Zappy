__author__ = 'Travis Moy'

import pyglet


class Camera(object):
    IMAGE_ACROSS = 64

    _sprites = []
    _entity_batch = pyglet.graphics.Batch()
    _cell_batch = pyglet.graphics.Batch()
    _magnification = 1
    _sprite_across = 64

    def __init__(self, _level, lower_left=(0, 0), upper_right=(640, 480), center_tile=[0, 0],
                 cursor_image_file='images/camera_cursor.png'):
        self._level = _level
        self._center_tile = center_tile
        self._cursor_image = pyglet.resource.image(cursor_image_file)

        # These are set by self.resize_view(); listed for my ease.
        self._lower_left = None
        self._upper_right = None
        self._num_rows = None
        self._num_cols = None
        self.resize_view(lower_left, upper_right)

    # How the heck do you write a test for this one!?
    def draw(self):
        pass

    def center_on(self, x, y):
        pass

    def center_on_entity(self, entity):
        pass

    def step(self, direction):
        pass

    def resize_view(self, lower_left, upper_right):
        pass
