__author__ = 'Travis Moy'

import unittest
import pyglet
from pyglet.window import key
import loader.LoaderLevel
import zappyui.Camera


class TestCamera(unittest.TestCase):

    def setUp(self):
        pyglet.resource.path = ['@zappyui', '.']
        pyglet.resource.reindex()

        temp_loader = loader.LoaderLevel.LoaderLevel('zappyui/test_assets')
        self.default_level = temp_loader.get_level(0)
        self.default_camera = zappyui.Camera.Camera(self.default_level,
                                                    cursor_image_file='test_assets/camera_cursor.png')

    def tearDown(self):
        pass

    # This test must be visually verified (I can't think of a good way to test it otherwise!).
    # Press 'y' twice if it is correct. Any other key will cause the test to fail.
    def test_draw(self):
        self.good = False
        width = 640
        height = 480

        self.window = pyglet.window.Window(width=width, height=height)

        labels = list()
        labels.append(pyglet.text.Label('TEST: Camera.draw()', font_size=30, x=width // 2, y=height - 60,
                                        anchor_x='center', anchor_y='center'))
        labels.append(pyglet.text.Label('This screen will appear twice.', font_size=20, x=width // 2, y=height - 120,
                                        anchor_x='center', anchor_y='center'))
        labels.append(pyglet.text.Label("Press 'y' if the icon looks good.", font_size=20, x=width // 2, y=120,
                                        anchor_x='center', anchor_y='center'))
        labels.append(pyglet.text.Label('Press any other key if it does not.', font_size=20, x=width // 2, y=80,
                                        anchor_x='center', anchor_y='center'))

        @self.window.event
        def on_draw():
            self.default_camera.draw()
            for label in labels:
                label.draw()

        @self.window.event
        def on_key_press(symbol, modifiers):
            if symbol == key.Y:
                self.good = True
            else:
                self.good = False
            pyglet.app.exit()

        pyglet.app.run()

        # Check to see if the viewer approves
        self.assertTrue(self.good)

    # center_on() recalculates which sprites need to be drawn
    # This test is probably testing too many things at once...
    def test_center_on(self):
        cam = self.default_camera
        # This should give us a 3x3 area to work with - more manageable
        cam.resize_view((0, 0), (100, 100))
        cam.center_on(1, 5)

        image_dict = dict()
        # So basically what I'm doing here is I've worked out that the x/y coordinates of the special cells should be
        # between two x/y values. Rounding may be a problem so I made it a range. To check that the sprites are being
        # loaded with the correct coordinates, compare the sprite.x to min_x and max_x; if it's within, it's correct.
        # Tuple format is (min_x, max_x, min_y, max_y)
        image_dict[pyglet.resource.image('test_assets/images/u.png')] = (-56, -36, 8, 72)
        image_dict[pyglet.resource.image('test_assets/images/v.png')] = (8, 28, 8, 72)
        image_dict[pyglet.resource.image('test_assets/images/w.png')] = (72, 92, 8, 72)
        image_dict[pyglet.resource.image('test_assets/images/x.png')] = (-56, -36, -56, -36)
        image_dict[pyglet.resource.image('test_assets/images/y.png')] = (8, 28, -56, -36)
        image_dict[pyglet.resource.image('test_assets/images/z.png')] = (72, 92, -56, -36)

        self.assertTrue(cam._center_tile[0] == 0 and cam._center_tile[1] == 5)
        self.assertEqual(len(cam._sprites), 6)
        for sprite in cam._sprites:
            comp_tuple = image_dict.get(sprite.image)
            self.assertFalse(comp_tuple is None, "There's a sprite loaded that shouldn't be!")
            self.assertTrue(comp_tuple[0] < sprite.x < comp_tuple[1])
            self.assertTrue(comp_tuple[2] < sprite.y < comp_tuple[3])

    # center_on_entity() recalculates which sprites need to be drawn
    def test_center_on_entity(self):
        self.default_camera.center_on_entity('TestStringEntity')
        self.assertTrue(self.default_camera._center_tile[0] == 2, self.default_camera._center_tile[2] == 1)
        self.default_camera.center_on_entity('ShouldNotMoveTheCamera')
        self.assertTrue(self.default_camera._center_tile[0] == 2, self.default_camera._center_tile[2] == 1)

    # recalculates which sprites need to be drawn
    def test_step(self):
        self.assertFalse(True)

    def test_resize_view(self):
        cam = self.default_camera
        lower_left = (0, 0)
        upper_right = (100, 100)
        cam.resize_view(lower_left, upper_right)
        self.assertEqual(cam._lower_left, lower_left)
        self.assertEqual(cam._upper_right, upper_right)
        self.assertEqual(cam._num_cols, 3)
        self.assertEqual(cam._num_rows, 3)

        lower_left = (0, 50)
        upper_right = (200, 100)
        cam.resize_view(lower_left, upper_right)
        self.assertEqual(cam._num_cols, 2)
        self.assertEqual(cam._num_rows, 5)


suite = unittest.TestLoader().loadTestsFromTestCase(TestCamera)
unittest.TextTestRunner(verbosity=2).run(suite)