__author__ = 'Travis Moy'

import unittest
import Entity


class TestEntity(unittest.TestCase):

    def setUp(self):
        self.default_entity = Entity.Entity(None)

    def tearDown(self):
        self.default_entity = None

    # Required for this test: in image, in the entity folder, of dimensions 100x100 titled "test_entity.png"
    # Also requires the default be in place, of course.
    def test_load_image(self):
        self.default_entity._image_name = 'test_entity.png'
        self.default_entity._load_image()
        self.assertEqual(self.default_entity._image.width, 100)
        self.assertEqual(self.default_entity._image.height, 100)

suite = unittest.TestLoader().loadTestsFromTestCase(TestEntity)
unittest.TextTestRunner(verbosity=2).run(suite)