__author__ = 'Travis Moy'


import unittest
import pyglet


class TestCameraSetLevel(unittest.TestCase):

    def test_set_level(self):
        window = pyglet.window.Window()
        header = pyglet.text.Label('TEST: Camera.set_level()', font_size=30, x=window.width // 2, y=window.height - 60,
                                   anchor_x='center', anchor_y='center')

        @window.event
        def on_draw():
            header.draw()

        @window.event
        def on_key_press(symbol, modifiers):
            pyglet.app.exit()

        pyglet.app.run()