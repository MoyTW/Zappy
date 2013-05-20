__author__ = 'Travis Moy'

import unittest
import pyglet
import loader.LoaderLevel
import zappyui.Camera
from pyglet.window import key


class TestCameraDraw(unittest.TestCase):

    def setUp(self):
        pyglet.resource.path = ['@zappyui', '.']
        pyglet.resource.reindex()

        temp_loader = loader.LoaderLevel.LoaderLevel('zappyui/test_assets')
        self.default_level = temp_loader.get_level(0)
        self.default_camera = zappyui.Camera.Camera(self.default_level,
                                                    cursor_image_file='test_assets/camera_cursor.png')

    def tearDown(self):
        self.default_camera = None
        self.default_level = None

    # This test must be visually verified (I can't think of a good way to test it otherwise!).
    # Press 'y' if it is correct. Any other key will cause the test to fail.
    def test_draw(self):
        self.default_camera.center_on(2, 3)

        self.good = False
        width = 640
        height = 480

        window = pyglet.window.Window(width=width, height=height)

        labels = list()
        labels.append(pyglet.text.Label('TEST: Camera.draw()', font_size=30, x=width // 2, y=height - 60,
                                        anchor_x='center', anchor_y='center'))
        labels.append(pyglet.text.Label("Press 'y' if the icon looks good.", font_size=20, x=width // 2, y=120,
                                        anchor_x='center', anchor_y='center'))
        labels.append(pyglet.text.Label('Press any other key if it does not.', font_size=20, x=width // 2, y=80,
                                        anchor_x='center', anchor_y='center'))

        @window.event
        def on_draw():
            if self.default_camera is not None:
                self.default_camera.draw()
                for label in labels:
                    label.draw()
            else:
                pyglet.app.exit()

        @window.event
        def on_key_press(symbol, modifiers):
            if symbol != key.Y:

                self.good = False
                #self.assertTrue(False, "User did not accept the results of Camera.draw()!")
                #pyglet.app.exit()
            else:
                self.good = True
            pyglet.app.exit()

        pyglet.app.run()

        self.assertTrue(self.good, "User did not accept the results of Camera.draw()!")