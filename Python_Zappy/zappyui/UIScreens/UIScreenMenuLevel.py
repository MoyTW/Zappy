__author__ = 'Travis Moy'

import UIScreen
import math
import pyglet
import warnings
from zappyui.Orders import ORDERS


# Init must take - what?
# At some point we've got to integrate player history in here, too.
class UIScreenMenuLevel(UIScreen.UIScreen):
    ASSETS_PATH = 'images/menu_level/'
    PREVIEW_SIZE = 300
    PREVIEW_SCALE = .75
    BLOCK_WIDTH = 250
    BLOCK_HEIGHT = 400
    BORDER_WIDTH = 50
    BORDER_HEIGHT = 40
    FONT_SIZE = 20

    _label_batch = pyglet.graphics.Batch()
    _level_batch = pyglet.graphics.Batch()

    def __init__(self, loader_level, viewport_info, factory):
        self._loader_level = loader_level
        self._viewport_info = viewport_info
        self._factory = factory

        # Note that a value of -1 means "left arrow" and a value of self._num_on_page means "right arrow"
        self._selection = 0
        self._previous_selection = 0
        self._current_page = 0

        self.avail_width = self._viewport_info.width - self.BORDER_WIDTH * 2
        self._num_cols = self.avail_width / self.BLOCK_WIDTH
        self.avail_height = self._viewport_info.height - self.BORDER_HEIGHT * 2
        self._num_rows = self.avail_height / self.BLOCK_HEIGHT
        self._num_levels = self._loader_level.get_num_levels()
        self._num_pages = int(math.ceil(float(self._num_levels) / float((self._num_rows * self._num_cols))))
        self._num_on_page = self._num_rows * self._num_cols

        self._draw_points = None
        self._init_draw_points()

        #Convenience
        self._left_sprite = None
        self._right_sprite = None
        self._left_selection_sprite = None
        self._right_selection_sprite = None
        self._level_selection_sprite = None
        self._init_default_sprites()

        self._level_drawables = None
        self._repopulate_level_drawables()

    def _init_default_sprites(self):
        temp_loader = pyglet.resource.Loader('@assets')

        # Left image and selection
        left_image = temp_loader.image("{0}left.png".format(self.ASSETS_PATH))
        left_selection_image = temp_loader.image("{0}left_selection.png".format(self.ASSETS_PATH))
        left_x = self.BORDER_WIDTH / 2 - left_image.width / 2
        left_y = self._viewport_info.height / 2 - left_image.height / 2
        self._left_sprite = pyglet.sprite.Sprite(left_image, x=left_x, y=left_y)
        self._left_selection_sprite = pyglet.sprite.Sprite(left_selection_image, x=left_x, y=left_y)

        # Right image and selection
        right_image = temp_loader.image("{0}right.png".format(self.ASSETS_PATH))
        right_selection_image = temp_loader.image("{0}right_selection.png".format(self.ASSETS_PATH))
        right_x = self._viewport_info.width - self.BORDER_WIDTH / 2 - (left_image.width / 2)
        right_y = self._viewport_info.height / 2 - right_image.height / 2
        self._right_sprite = pyglet.sprite.Sprite(right_image, x=right_x, y=right_y)
        self._right_selection_sprite = pyglet.sprite.Sprite(right_selection_image, x=right_x, y=right_y)

        # Load the level selection image and create sprite; no location set by default
        level_selection_image = temp_loader.image("{0}level_selection.png".format(self.ASSETS_PATH))
        self._level_selection_sprite = pyglet.sprite.Sprite(level_selection_image)
        self._level_selection_sprite.scale = 1.01 * self.PREVIEW_SCALE
        self._move_level_selection_sprite()

#***** Initializes the centerpoints for the tiles *****#
    def _init_draw_points(self):
        self._draw_points = [[None for _ in range(self._num_rows)] for _ in range(self._num_cols)]
        height_per_row = self.avail_height / self._num_rows
        for i in range(self._num_rows):
            row_starts_at = self.BORDER_HEIGHT + height_per_row * i
            row_center = row_starts_at + height_per_row / 2
            self._init_draw_points_row(i, row_center)

    def _init_draw_points_row(self, row, y_center):
        width_per_col = self.avail_width / self._num_cols
        for i in range(self._num_cols):
            col_starts_at = self.BORDER_WIDTH + width_per_col * i
            col_center = col_starts_at + width_per_col / 2

            self._draw_points[i][row] = (col_center, y_center)
#***** End Centerpoints Code *****#

#***** Populates self._level_drawables and fills self._level_batch with the level tiles *****#
    def _repopulate_level_drawables(self):
        self._level_drawables = list()
        self._label_batch = pyglet.graphics.Batch()
        local_number = 0
        y = self._num_rows - 1
        while y >= 0:
            x = 0
            while x < self._num_cols:
                level_number = local_number + self._current_page * self._num_on_page
                self._add_tile_at_point(self._draw_points[x][y], level_number)
                local_number += 1
                x += 1
            y -= 1

    def _add_tile_at_point(self, point, level_number):
        info = self._loader_level.get_level_info(level_number)
        if info is None:
            return

        preview_sprite = pyglet.sprite.Sprite(info.get_preview(),
                                              x=point[0] - info.get_preview().width * self.PREVIEW_SCALE / 2,
                                              y=point[1],
                                              batch=self._level_batch)
        preview_sprite.scale = self.PREVIEW_SCALE
        self._level_drawables.append(preview_sprite)

        # Note that labels are apparently stored in the batch itself, unlike sprites! That's why this works, despite the
        # fact that I don't store the generated object. It's also why I clear the batch up in the calling function!
        pyglet.text.Label("Level {0}".format(level_number), x=point[0] - self.BLOCK_WIDTH / 2 + 20,y=point[1] - 30,
                          font_size=self.FONT_SIZE, batch=self._label_batch)
#***** End level_drawables Code *****#

    def can_page_left(self):
        return self._current_page > 0

    def can_page_right(self):
        return self._current_page < self._num_pages - 1

    def handle_order(self, order):
        if order == ORDERS.LEFT or order == ORDERS.RIGHT or order == ORDERS.UP or order == ORDERS.DOWN:
            return self._change_selection(order)
        elif order == ORDERS.CONFIRM:
            return self._confirm_selection()
        elif order == ORDERS.CANCEL:
            return self._cancel()
        return self

    def _cancel(self):
        return None

    def _change_selection(self, order):
        if order == ORDERS.DOWN:
            if self._selection == -1 or self._selection == self._num_on_page:
                pass
            elif not self._selection >= (self._num_rows - 1) * self._num_cols:
                self._selection += self._num_cols
        if order == ORDERS.UP:
            if self._selection == -1 or self._selection == self._num_on_page:
                pass
            elif self._selection != self._num_on_page and not self._selection < self._num_cols:
                self._selection -= self._num_cols
        if order == ORDERS.LEFT:
            if self._selection == self._num_on_page:
                self._selection = self._previous_selection
            elif self._selection == -1:
                pass
            elif self._selection == self._num_on_page or self._selection % self._num_cols != 0:
                self._selection -= 1
            elif self.can_page_left():
                self._previous_selection = self._selection
                self._selection = -1
        if order == ORDERS.RIGHT:
            if self._selection == -1:
                self._selection = self._previous_selection
            elif self._selection == self._num_on_page:
                pass
            elif self._selection % self._num_cols != self._num_cols - 1:
                self._selection += 1
            elif self.can_page_right():
                self._previous_selection = self._selection
                self._selection = self._num_on_page
        if -1 < self._selection < self._num_on_page:
            self._move_level_selection_sprite()
        return self

    def _move_level_selection_sprite(self):
        x = self._selection % self._num_cols
        y = self._selection / self._num_cols - 1
        point = self._draw_points[x][y]
        self._level_selection_sprite.x = point[0] - (self._level_selection_sprite.width / 2)
        self._level_selection_sprite.y = point[1]

    def _confirm_selection(self):
        if self._selection == -1:
            return self._flip_page(-1)
        elif self._selection == self._num_on_page:
            return self._flip_page(1)
        else:
            return self._attempt_to_launch_level()

    def _attempt_to_launch_level(self):
        level_num = self._selection + self._current_page * self._num_on_page
        self._loader_level.regen_level(level_num)
        return self._factory.create_ScreenLevel(self._loader_level.get_level_controller(level_num))

    def _flip_page(self, direction):
        self._current_page += direction
        if direction > 0:
            self._selection = 0
        else:
            self._selection = self._num_on_page - 1
        self._move_level_selection_sprite()
        self._repopulate_level_drawables()
        return self

#***** Drawing Code *****#
    def draw(self):
        self._draw_arrows()
        self._level_batch.draw()
        self._label_batch.draw()
        self._draw_selection()

    def _draw_arrows(self):
        if self.can_page_left():
            self._left_sprite.draw()
        if self.can_page_right():
            self._right_sprite.draw()

    def _draw_selection(self):
        if -1 < self._selection < self._num_on_page:
            self._level_selection_sprite.draw()
        elif self._selection == -1:
            self._left_selection_sprite.draw()
        elif self._selection == self._num_on_page:
            self._right_selection_sprite.draw()
#***** End Drawing Code *****#