__author__ = 'Travis Moy'

import unittest
import pyglet
import Camera
from pyglet.window import key


class TestCameraSetLevel(unittest.TestCase):

    def setUp(self):
        self.default_level = None
        self.level_one = None
        self.default_camera = Camera.Camera(self.default_level, cursor_image_file='test_assets/camera_cursor.png')

    def tearDown(self):
        self.default_camera = None
        self.default_level = None

    def test_draw(self):
        self.good = False
        self.second_level = False
        width = 640
        height = 480

        window = pyglet.window.Window(width=width, height=height)

        header = pyglet.text.Label('TEST: Camera.draw()', font_size=30, x=width // 2, y=height - 60,
                                   anchor_x='center', anchor_y='center')
        prompt = pyglet.text.Label("Press any key to swap levels.", font_size=20, x=width // 2, y=120,
                                   anchor_x='center', anchor_y='center')
        labels = list()
        labels.append(pyglet.text.Label("Press 'y' if the icon looks good.", font_size=20, x=width // 2, y=120,
                                        anchor_x='center', anchor_y='center'))
        labels.append(pyglet.text.Label('Press any other key if it does not.', font_size=20, x=width // 2, y=80,
                                        anchor_x='center', anchor_y='center'))

        @window.event
        def on_draw():
            window.clear()
            if self.default_camera is not None:
                self.default_camera.draw()
                header.draw()
                if self.second_level:
                    pass
                    for label in labels:
                        label.draw()
                else:
                    prompt.draw()
            else:
                pyglet.app.exit()

        @window.event
        def on_key_press(symbol, modifiers):
            if not self.second_level:
                self.default_camera.set_level(self.level_one, (1, 1))
                self.second_level = True
                return

            if symbol != key.Y:
                self.good = False
            else:
                self.good = True
            pyglet.app.exit()

        pyglet.app.run()

        self.assertTrue(self.good, "User did not accept the results of Camera.set_level()!")