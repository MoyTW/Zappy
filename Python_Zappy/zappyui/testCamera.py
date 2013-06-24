__author__ = 'Travis Moy'

import unittest
import pyglet
import loader.LoaderLevelLVL
import zappyui.Camera
from z_defs import DIR
import dummies.DummyLoaderEntityIndex


class TestCamera(unittest.TestCase):

    def setUp(self):
        pyglet.resource.path = ['@zappyui', '.']
        pyglet.resource.reindex()

        temp_loader = loader.LoaderLevelLVL.LoaderLevelLVL('zappyui/test_assets')
        temp_loader._entity_index = dummies.DummyLoaderEntityIndex.DummyLoaderEntityIndex()
        self.default_level = temp_loader.get_level(0)
        self.default_camera = zappyui.Camera.Camera(self.default_level,
                                                    cursor_image_file='test_assets/camera_cursor.png')

    def tearDown(self):
        self.default_camera = None
        self.default_level = None

    # center_on() recalculates which sprites need to be drawn
    # This test is probably testing too many things at once...
    def test_center_on_upper_left(self):
        cam = self.default_camera
        # This should give us a 3x3 area to work with - more manageable
        cam.resize_view((0, 0), (100, 100))
        cam.center_on(1, 5)

        image_dict = dict()
        # So basically what I'm doing here is I've worked out that the x/y coordinates of the special cells should be
        # between two x/y values. Rounding may be a problem so I made it a range. To check that the sprites are being
        # loaded with the correct coordinates, compare the sprite.x to min_x and max_x; if it's within, it's correct.
        # Tuple format is (min_x, max_x, min_y, max_y)
        image_dict[pyglet.resource.image('test_assets/images/u.png')] = (72, 92, 8, 28)
        image_dict[pyglet.resource.image('test_assets/images/v.png')] = (8, 28, 8, 28)
        image_dict[pyglet.resource.image('test_assets/images/w.png')] = (-56, -36, 8, 28)
        image_dict[pyglet.resource.image('test_assets/images/x.png')] = (-56, -36, -56, -36)
        image_dict[pyglet.resource.image('test_assets/images/y.png')] = (8, 28, -56, -36)
        image_dict[pyglet.resource.image('test_assets/images/z.png')] = (72, 92, -56, -36)

        self.assertTrue(cam._center_tile[0] == 1 and cam._center_tile[1] == 5)
        #self.assertEqual(len(cam._sprites), 6)
        for sprite in cam._sprites:
            comp_tuple = image_dict.get(sprite.image)
            self.assertFalse(comp_tuple is None, "There's a sprite loaded that shouldn't be!")
            self.assertTrue(comp_tuple[0] < sprite.x < comp_tuple[1])
            self.assertTrue(comp_tuple[2] < sprite.y < comp_tuple[3])

    '''
    No longer valid test; Camera excludes drawing tiles not visible by player. Tiles off the map are marked opaque.
    def test_center_on_runs_off_upper_right(self):
        cam = self.default_camera
        cam.resize_view((0, 0), (100, 100))
        cam.center_on(4, 5)
        self.assertEqual(len(cam._sprites), 4)
    '''

    '''
    No longer valid test; Camera excludes drawing tiles not visible by player. Tiles off the map are marked opaque.
    def test_center_on_runs_off_lower_left(self):
        cam = self.default_camera
        cam.resize_view((0, 0), (100, 100))
        cam.center_on(0, 0)
        self.assertEqual(len(cam._sprites), 4)
    '''

    # center_on_entity() recalculates which sprites need to be drawn
    def test_center_on_entity(self):
        self.default_camera.center_on_entity('TestStringEntity')
        self.assertTrue(self.default_camera._center_tile[0] == 2, self.default_camera._center_tile[1] == 1)
        self.default_camera.center_on_entity('ShouldNotMoveTheCamera')
        self.assertTrue(self.default_camera._center_tile[0] == 2, self.default_camera._center_tile[1] == 1)

    # recalculates which sprites need to be drawn
    def test_step(self):
        cam = self.default_camera
        cam.center_on(1, 1)

        cam.step(DIR.N)
        self.assertEqual((1, 2), cam.get_center_tile())
        cam.step(DIR.NE)
        self.assertEqual((2, 3), cam.get_center_tile())
        cam.step(DIR.E)
        self.assertEqual((3, 3), cam.get_center_tile())
        cam.step(DIR.SE)
        self.assertEqual((4, 2), cam.get_center_tile())
        cam.step(DIR.S)
        self.assertEqual((4, 1), cam.get_center_tile())
        cam.step(DIR.SW)
        self.assertEqual((3, 0), cam.get_center_tile())
        cam.step(DIR.W)
        self.assertEqual((2, 0), cam.get_center_tile())
        cam.step(DIR.NW)
        self.assertEqual((1, 1), cam.get_center_tile())

        cam.step(-999)
        self.assertEqual((1, 1), cam.get_center_tile())

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