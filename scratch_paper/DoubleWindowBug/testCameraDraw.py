__author__ = 'Travis Moy'

import unittest
import pyglet
import DummyCamera


class TestCameraDraw(unittest.TestCase):

    def setUp(self):
        self.default_camera = DummyCamera.DummyCamera()

    def tearDown(self):
        self.default_camera = None

    def test_draw(self):
        window = pyglet.window.Window()

        label = pyglet.text.Label('TEST: Camera.draw()', font_size=30, x=window.width // 2, y=window.height - 60,
                                  anchor_x='center', anchor_y='center')

        @window.event
        def on_draw():
            if self.default_camera is not None:
                self.default_camera.draw()
                label.draw()
            #else:
                #pyglet.app.exit()

        @window.event
        def on_key_press(symbol, modifiers):
            pyglet.app.exit()

        pyglet.app.run()