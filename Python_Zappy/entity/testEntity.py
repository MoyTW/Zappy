__author__ = 'Travis Moy'

import unittest
import entity.Entity as Entity


class TestEntity(unittest.TestCase):

    def setUp(self):
        self.default_entity = Entity.Entity(0, None)

    def tearDown(self):
        self.default_entity = None

    def test_eq(self):
        eq_entity = Entity.Entity(0, None)
        self.assertEqual(self.default_entity, eq_entity)

        ne_entity = Entity.Entity(1, None)
        self.assertFalse(self.default_entity == ne_entity)
        self.assertNotEqual(self.default_entity, ne_entity)

    # Required for this test: in image, in the entity folder, of dimensions 100x100 titled "test_entity.png"
    # Also requires the default be in place, of course.
    def test_load_image(self):
        image = self.default_entity._load_return_image('test_entity.png')
        self.assertEqual(image.width, 100)
        self.assertEqual(image.height, 100)

suite = unittest.TestLoader().loadTestsFromTestCase(TestEntity)
unittest.TextTestRunner(verbosity=2).run(suite)