__author__ = 'Travis Moy'

import unittest
import pyglet
from pyglet.window import key


class TestCameraSetLevel(unittest.TestCase):

    def setUp(self):
        self.default_level = None
        self.level_one = None

    def tearDown(self):
        self.default_level = None
        self.level_one = None

    def test_set_level(self):
        self.good = False

        window = pyglet.window.Window()

        header = pyglet.text.Label('TEST: Camera.set_level()', font_size=30, x=window.width // 2, y=window.height - 60,
                                   anchor_x='center', anchor_y='center')

        @window.event
        def on_draw():
            window.clear()
            header.draw()

        @window.event
        def on_key_press(symbol, modifiers):
            if symbol == key.Y:
                self.good = True
            pyglet.app.exit()

        pyglet.app.run()

        self.assertTrue(self.good, "User did not accept the results of Camera.set_level()!")