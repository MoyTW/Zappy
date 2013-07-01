__author__ = 'Travis Moy'

from z_defs import DIR
import math
import pyglet
import warnings
from z_algs import Z_ALGS


class Camera(object):
    IMAGE_ACROSS = 64
    DEFAULT_CURSOR_IMAGE = 'images/camera_cursor.png'
    FOW_IMAGE = 'images/defaults/default_fow.png'
    LOADER = pyglet.resource.Loader(['@assets'])

    def __init__(self, level=None, lower_left=(0, 0), upper_right=(640, 480), center_tile=(0, 0),
                 cursor_image_file=DEFAULT_CURSOR_IMAGE):
        self._level = level
        self._center_tile = center_tile

        self._draw_cursor = True
        self._sprites = list()
        self._batches = dict()
        self._fow_batch = pyglet.graphics.Batch()
        self._magnification = 1
        self._sprite_across = 64

        self._explored_cells = set()  # Cells which the player has, at some point, seen.

        # Convenience.
        self._fow_image = None
        self._load_fow_image()

        # These are set by self._load_cursor(); listed for my ease.
        self._cursor_image = None
        self._cursor = None
        self._load_cursor(cursor_image_file)

        # These are set by self.resize_view(); listed for my ease.
        self._lower_left = None
        self._upper_right = None
        self._lower_left_pixel = None
        self._num_rows = None
        self._num_cols = None
        self.resize_view(lower_left, upper_right)

    def get_x(self):
        return self._center_tile[0]

    def get_y(self):
        return self._center_tile[1]

    def get_center_tile(self):
        return self._center_tile[0], self._center_tile[1]

    def enable_cursor(self):
        self._draw_cursor = True

    def disable_cursor(self):
        self._draw_cursor = False

    def set_level(self, _level, center_tile=(0, 0)):
        self._level = _level
        self._center_tile = center_tile
        self.center_on(center_tile[0], center_tile[1])

    # How the heck do you write a test for this one!?
    # Draws in ascending priority (-3 before 6) - this means that higher priority will be cleaner.
    def draw(self):
        if self._level is None:
            return False

        # This is pretty ugly, honestly.
        self.center_on(self._center_tile[0], self._center_tile[1])

        batch_keys = self._batches.keys()
        batch_keys.sort()
        for key in batch_keys:
            self._batches.get(key).draw()
        if self._draw_cursor:
            self._cursor.draw()

        self._fow_batch.draw()

    def center_on(self, x, y):
        if self._level is None:
            return False

        self._center_tile = [x, y]
        lower_left_index = (int(x - math.floor(self._num_rows / 2)),
                            int(y - math.floor(self._num_cols / 2)))
        # Just to be safe, in case magnification has changed
        self._sprite_across = self.IMAGE_ACROSS * self._magnification

        self._sprites = list()
        player_actor = self._level.get_player_actor()
        # Ugly as hell, we're poking all over where we shouldn't be!
        # If there's no entity to match, it will disregard the FOW.
        try:
            visible_cells = Z_ALGS.calc_visible_cells_from(*player_actor.get_coords(),
                                                           radius=player_actor._senses[0]._range,
                                                           func_transparent=self._level.cell_is_transparent)
            self._explored_cells.update(visible_cells)
        except AttributeError:
            visible_cells = None

        for row in range(0, self._num_rows):
            for col in range(0, self._num_cols):
                cell_row_index = lower_left_index[0] + row
                cell_col_index = lower_left_index[1] + col

                in_fow = False
                # Determine the FOW state
                if visible_cells is not None and (cell_row_index, cell_col_index) not in visible_cells and \
                        self._level.get_cell_at(cell_row_index, cell_col_index) is not None:
                    in_fow = True

                # Check to see if it's in _explored_cells
                if (cell_row_index, cell_col_index) in self._explored_cells:
                    display_images = self._level.get_display_images_at(cell_row_index, cell_col_index, in_fow)
                    self._process_display_images_and_add_sprites(display_images, row, col)

                    # This is the code to draw the FOW sprite over the cell.
                    if in_fow:
                        sprite = pyglet.sprite.Sprite(
                            self._fow_image,
                            x=self._lower_left_pixel[0] + row * self._sprite_across,
                            y=self._lower_left_pixel[1] + col * self._sprite_across,
                            batch=self._fow_batch)
                        sprite.opacity = 128
                        self._sprites.append(sprite)

    # Processes the display images. No duh. That's a useless comment.
    # Currently it creates sprites for the first image of each priority.
    # If the priority is not in _batches, it adds it.
    def _process_display_images_and_add_sprites(self, display_images, row, col):
        if display_images is None:
            return

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
        if self._level is None:
            return False

        loc = self._level.find_coordinates_of_entity(entity)
        if loc is not None:
            self.center_on(loc[0], loc[1])

    def step(self, direction):
        target_coords = DIR.get_coords_in_direction_from(direction, self.get_x(), self.get_y())
        self.center_on(target_coords[0], target_coords[1])

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

        # the -32 + rows/cols mod 2 * 32 is to make sure that if the number of rows/cols is even, it doesn't misalign.
        self._lower_left_pixel = ((center_pixel[0] - (float(self._num_rows) / 2.0) *
                                  self._sprite_across - 32 + (self._num_rows % 2) * 32),
                                 (center_pixel[1] - (float(self._num_cols) / 2.0) *
                                  self._sprite_across) - 32 + (self._num_cols % 2) * 32)

    # Checks local, assets for target file: if no, tries to load default. If no default, throws.
    def _load_cursor(self, file):
        try:
            self._cursor_image = pyglet.resource.image(file)
        except pyglet.resource.ResourceNotFoundException:
            try:
                self._cursor_image = self.LOADER.image(file)
            except pyglet.resource.ResourceNotFoundException:
                warnings.warn("Error loading specified Cursor image, attempting to load default Cursor image.")
                self._cursor_image = self.LOADER.image(self.DEFAULT_CURSOR_IMAGE)
        self._cursor = pyglet.sprite.Sprite(self._cursor_image)

    def _load_fow_image(self):
        self._fow_image = self.LOADER.image(self.FOW_IMAGE)