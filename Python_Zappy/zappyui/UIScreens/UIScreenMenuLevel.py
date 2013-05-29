__author__ = 'Travis Moy'

import UIScreen
import math
import pyglet
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

    _level_drawables = list()
    _fixed_drawables = list()
    _level_batch = pyglet.graphics.Batch()
    _fixed_batch = pyglet.graphics.Batch()

    def __init__(self, loader_level, viewport_info, factory):
        self._loader_level = loader_level
        self._viewport_info = viewport_info
        self._factory = factory

        # Convenience.
        self._avail_width = None
        self._avail_height = None
        self._num_cols = None
        self._num_rows = None

        self._init_number_levels_to_show()

        self._num_levels = self._loader_level.get_num_levels()
        self._current_page = 0
        self._num_pages = int(math.ceil(float(self._num_levels) / float((self._num_rows * self._num_cols))))

        self._draw_points = [[None for _ in range(self._num_rows)] for _ in range(self._num_cols)]
        self._init_draw_points()

        self._init_fixed_drawables()

    def _init_fixed_drawables(self):
        temp_loader = pyglet.resource.Loader('@assets')

        left_image = temp_loader.image("{0}left.png".format(self.ASSETS_PATH))
        left_sprite = pyglet.sprite.Sprite(left_image,
                                           x=self.BORDER_WIDTH / 2 - left_image.width / 2,
                                           y=self._viewport_info.height / 2 - left_image.height / 2,
                                           batch=self._fixed_batch)
        self._fixed_drawables.append(left_sprite)

        right_image = temp_loader.image("{0}right.png".format(self.ASSETS_PATH))
        right_sprite = pyglet.sprite.Sprite(right_image, x=self._viewport_info.width -
                                            self.BORDER_WIDTH / 2 - (left_image.width / 2),
                                            y=self._viewport_info.height / 2 - right_image.height / 2,
                                            batch=self._fixed_batch)
        self._fixed_drawables.append(right_sprite)

    def _init_number_levels_to_show(self):
        self.avail_width = self._viewport_info.width - self.BORDER_WIDTH * 2
        self._num_cols = self.avail_width / self.BLOCK_WIDTH
        self.avail_height = self._viewport_info.height - self.BORDER_HEIGHT * 2
        self._num_rows = self.avail_height / self.BLOCK_HEIGHT

    def _init_draw_points(self):
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

    def _draw_at_point(self, point, level_number):
        print "Drawing level {0} at {1}".format(level_number, point)
        info = self._loader_level.get_level_info(level_number)
        if info is None:
            return

        preview_sprite = pyglet.sprite.Sprite(info.get_preview(),
                                              x=point[0] - info.get_preview().width * self.PREVIEW_SCALE / 2,
                                              y=point[1])
        preview_sprite.scale = self.PREVIEW_SCALE
        preview_sprite.draw()

    def handle_order(self, order):
        pass

    def _draw_level_display(self):
        local_number = 0
        y = self._num_rows - 1
        while y >= 0:
            x = 0
            while x < self._num_cols:
                level_number = local_number + self._current_page * (self._num_cols * self._num_rows)
                self._draw_at_point(self._draw_points[x][y], level_number)
                local_number += 1
                x += 1
            y -= 1

    # Draw as follows: [0][3], [1][3], [2][3], [3][3]
    def draw(self):
        self._fixed_batch.draw()
        self._draw_level_display()