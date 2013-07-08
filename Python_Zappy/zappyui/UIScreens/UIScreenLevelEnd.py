__author__ = 'Travis Moy'

import UIScreen
import pyglet
from zappyui.Orders import ORDERS


class UIScreenLevelEnd(UIScreen.UIScreen):

    def __init__(self, level_controller, viewport_info):
        self._viewport = viewport_info
        self._control = level_controller
        self._level = level_controller.level

        self._batch = pyglet.graphics.Batch()

        label_text = 'Neither Victory, Nor Defeat. WTF?'
        if self._control.level_won:
            label_text = 'Victory!'
        elif self._control.level_failed:
            label_text = 'Defeat!'

        message = pyglet.text.Label(label_text,
                                    font_size=72,
                                    y=viewport_info.height // 2,
                                    batch=self._batch)
        message.x = viewport_info.width // 2 - message.content_width // 2
        pyglet.text.Label('Press CANCEL to return to level select.',
                          font_size=18,
                          x=viewport_info.width // 2 - 190,
                          y=viewport_info.height // 2 - 50,
                          batch=self._batch)

    def draw(self):
        self._batch.draw()

    def handle_order(self, order):
        if order == ORDERS.CANCEL:
            return True
        else:
            return self