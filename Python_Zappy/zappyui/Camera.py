__author__ = 'Travis Moy'

import math
import pyglet


class Camera(object):
    IMAGE_ACROSS = 64

    _sprites = list()
    _batches = dict()
    _magnification = 1
    _sprite_across = 64

    def __init__(self, _level, lower_left=(0, 0), upper_right=(640, 480), center_tile=[0, 0],
                 cursor_image_file='images/camera_cursor.png'):
        self._level = _level
        self._center_tile = center_tile
        self._cursor_image = pyglet.resource.image(cursor_image_file)
        self._cursor = pyglet.sprite.Sprite(self._cursor_image)

        # These are set by self.resize_view(); listed for my ease.
        self._lower_left = None
        self._upper_right = None
        self._lower_left_pixel = None
        self._num_rows = None
        self._num_cols = None
        self.resize_view(lower_left, upper_right)

    # How the heck do you write a test for this one!?
    # Draws in ascending priority (-3 before 6) - this means that higher priority will be cleaner.
    def draw(self):
        batch_keys = self._batches.keys()
        batch_keys.sort()
        for key in batch_keys:
            self._batches.get(key).draw()

    def center_on(self, x, y):
        self._center_tile = [x, y]
        lower_left_index = (int(x - math.floor(self._num_rows / 2)),
                            int(y - math.floor(self._num_cols / 2)))
        # Just to be safe, in case it's changed
        self._sprite_across = self.IMAGE_ACROSS * self._magnification

        self._sprites = list()

#        for row in range(lower_left_index[0], lower_left_index[0] + self._num_rows):
#            for col in range(lower_left_index[1], lower_left_index[1] + self._num_cols):
        for row in range(0, self._num_rows):
            for col in range(0, self._num_cols):
                cell_row_index = lower_left_index[0] + row
                cell_col_index = lower_left_index[1] + col
                display_images = self._level.get_display_images_at(cell_row_index, cell_col_index)
                self._process_display_images_and_add_sprites(display_images, row, col)

    # Processes the display images. No duh. That's a useless comment.
    # Currently it creates sprites for the first image of each priority.
    # If the priority is not in _batches, it adds it.
    def _process_display_images_and_add_sprites(self, display_images, row, col):
        if display_images is None:
            return

        #print "PROCESSING! Lower-left pixel is: {0}".format(self._lower_left_pixel)

        display_keys = display_images.keys()
        display_keys.sort()

        for priority in display_keys:
            if priority not in self._batches:
                self._batches[priority] = pyglet.graphics.Batch()

            sprite = pyglet.sprite.Sprite(
                display_images[priority][0],
                x=self._lower_left_pixel[0] + row * self._sprite_across,
                y=self._lower_left_pixel[1] + col * self._sprite_across,
                batch=self._batches[priority]
            )
            self._sprites.append(sprite)

    def center_on_entity(self, entity):
        pass

    def step(self, direction):
        pass

    def resize_view(self, lower_left, upper_right):
        self._sprite_across = self.IMAGE_ACROSS * self._magnification
        self._lower_left = lower_left
        self._upper_right = upper_right

        center_pixel = ((upper_right[0] + lower_left[0]) / 2,
                        (upper_right[1] + lower_left[1]) / 2)
        self._cursor.set_position(center_pixel[0] - self._sprite_across / 2, center_pixel[1] - self._sprite_across / 2)

        self._num_rows = 1 + int(math.ceil((float(upper_right[0] - lower_left[0])) /
                                 float(self._sprite_across)))
        self._num_cols = 1 + int(math.ceil(float((upper_right[1] - lower_left[1])) /
                                 float(self._sprite_across)))

        self._lower_left_pixel = ((center_pixel[0] - (float(self._num_rows) / 2.0) *
                                  self._sprite_across),
                                 (center_pixel[1] - (float(self._num_cols) / 2.0) *
                                  self._sprite_across))
