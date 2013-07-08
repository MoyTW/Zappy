__author__ = 'Travis Moy'

import unittest
import entity.Entity as Entity


class TestEntity(unittest.TestCase):

    def setUp(self):
        self.default_entity = Entity.Entity(0, None)

    def tearDown(self):
        self.default_entity = None

    # Required for this test: in image, in the entity folder, of dimensions 100x100 titled "test_entity.png"
    # Also requires the default be in place, of course.
    def test_load_image(self):
        image = self.default_entity._load_return_image('test_entity.png')
        self.assertEqual(image.width, 100)
        self.assertEqual(image.height, 100)

suite = unittest.TestLoader().loadTestsFromTestCase(TestEntity)
unittest.TextTestRunner(verbosity=2).run(suite)