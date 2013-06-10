__author__ = 'Travis Moy'

import UIScreen
import pyglet


class UIScreenLevelEnd(UIScreen.UIScreen):
    defeat_batch = pyglet.graphics.Batch()

    def __init__(self, level_controller, viewport_info):
        self._viewport = viewport_info
        self._control = level_controller
        self._level = level_controller.get_level()

        pyglet.text.Label('DEFEAT!',
                          font_size=72,
                          x=viewport_info.width // 2 - 190,
                          y=viewport_info.height // 2,
                          batch=self.defeat_batch)
        pyglet.text.Label('Press any key to return to level select.',
                          font_size=18,
                          x=viewport_info.width // 2 - 190,
                          y=viewport_info.height // 2 - 50,
                          batch=self.defeat_batch)

    def draw(self):
        self.defeat_batch.draw()

    def handle_order(self, order):
        return True

