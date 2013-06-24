__author__ = 'Travis Moy'

import unittest
import loader.LoaderLevelV1 as LoaderLevel
import level.LevelInfo as LevelInfo
from z_json import JSONCONVERTER
import pyglet


class TestLoaderLevelV1(unittest.TestCase):

    def setUp(self):
        self.loader_level = LoaderLevel.LoaderLevelV1('loader/test_levels')

    def tearDown(self):
        self.loader_level = None

    def test_load_all_levels_infos(self):
        info0 = self.loader_level._levels[0].get_level_info()
        self.assertEqual(info0.get_number(), 0)
        self.assertEqual(info0.get_name(), 'TestLevel0')

        info1 = self.loader_level._levels[1].get_level_info()
        self.assertEqual(info1.get_number(), 1)
        self.assertEqual(info1.get_name(), 'TestLevel1')

    def test_get_level_info(self):
        self.loader_level._load_level_info('0.lvlV1')
        info = self.loader_level._levels[0].get_level_info()
        self.assertTrue(isinstance(info, LevelInfo.LevelInfo))
        self.assertEqual(info.get_name(), 'TestLevel0')
        self.assertEqual(info.get_number(), 0)
        self.assertEqual(info.get_width(), 5)
        self.assertEqual(info.get_height(), 5)

    def test_load_return_cell_templates(self):
        template_json = '{ "#": "test/wall.json", ".": "test/floor.json", "D": "test/drone.json" }'

        template_loader = pyglet.resource.Loader('@assets')
        floor = JSONCONVERTER.simple_to_custom_object(template_loader.text('cells/test/floor.json').text)
        wall = JSONCONVERTER.simple_to_custom_object(template_loader.text('cells/test/wall.json').text)
        drone = JSONCONVERTER.simple_to_custom_object(template_loader.text('cells/test/drone.json').text)

        templates = self.loader_level._load_return_cell_templates(template_json)
        try:
            self.assertEqual(templates['.'], floor)
            self.assertEqual(templates['#'], wall)
            self.assertEqual(templates['D'], drone)
        except (KeyError, TypeError):
            self.assertFalse(True, "Dict is not populated correctly!")

    def test_load_level(self):
        self.assertFalse(True)

    def test_get_level(self):
        self.assertFalse(True)

    def test_can_locate_player_controlled_entity(self):
        self.assertFalse(True)

suite = unittest.TestLoader().loadTestsFromTestCase(TestLoaderLevelV1)
unittest.TextTestRunner(verbosity=2).run(suite)
