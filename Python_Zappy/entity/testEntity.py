__author__ = 'Travis Moy'

import unittest
import entity.Entity as Entity
import level.Level as Level
from level.commands.command_fragments import LevelRemoveEntity


class TestEntity(unittest.TestCase):

    def setUp(self):
        self.default_level = Level.Level(None)
        self.default_entity = Entity.Entity(0, self.default_level.view)

    def tearDown(self):
        self.default_entity = None

    def test_eq(self):
        eq_entity = Entity.Entity(0, None)
        self.assertEqual(self.default_entity, eq_entity)

        ne_entity = Entity.Entity(1, None)
        self.assertFalse(self.default_entity == ne_entity)
        self.assertNotEqual(self.default_entity, ne_entity)

    def test_destroy(self):
        self.default_entity.destroy()
        self.assertEqual(len(self.default_level.command_log), 1)
        print type(self.default_level.command_log[0])
        self.assertTrue(isinstance(self.default_level.command_log[0].fragments[0], LevelRemoveEntity))

    # Required for this test: in image, in the entity folder, of dimensions 100x100 titled "test_entity.png"
    # Also requires the default be in place, of course.
    def test_load_image(self):
        image = self.default_entity._load_return_image('test_entity.png')
        self.assertEqual(image.width, 100)
        self.assertEqual(image.height, 100)

suite = unittest.TestLoader().loadTestsFromTestCase(TestEntity)
unittest.TextTestRunner(verbosity=2).run(suite)