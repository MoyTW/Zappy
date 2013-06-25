__author__ = 'Travis Moy'

import unittest
import loader.LoaderLevelV1 as LoaderLevel
import level.LevelInfo as LevelInfo
import level.Level as Level
from z_json import JSONCONVERTER
import pyglet


class TestLoaderLevelV1(unittest.TestCase):

    def setUp(self):
        self.loader_level = LoaderLevel.LoaderLevelV1('loader/test_levels')

    def tearDown(self):
        self.loader_level = None

    def create_test_template(self):
        template_loader = pyglet.resource.Loader('@assets')
        floor = JSONCONVERTER.simple_to_custom_object(template_loader.text('cells/test/floor.json').text)
        wall = JSONCONVERTER.simple_to_custom_object(template_loader.text('cells/test/wall.json').text)
        drone = JSONCONVERTER.simple_to_custom_object(template_loader.text('cells/test/drone.json').text)
        template = {"#": wall, ".": floor, "D": drone}
        return template

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

        expected_template = self.create_test_template()

        templates = self.loader_level._load_return_cell_templates(template_json)
        try:
            self.assertEqual(templates['.'], expected_template['.'])
            self.assertEqual(templates['#'], expected_template['#'])
            self.assertEqual(templates['D'], expected_template['D'])
        except (KeyError, TypeError):
            self.assertFalse(True, "Dict is not populated correctly!")

    def test_load_level_cells(self):
        comp_level = Level.Level(self.loader_level.get_level_info(0))
        func_level = self.loader_level._levels[0]
        template = self.create_test_template()
        layout_string = "# . # . #\n# . . . #\n# . D . #\n# . . . #\n# # # # #\n"

        comp_level.replace_cells([[None for _ in range(0, 5)] for _ in range(0, 5)])

        # You start from the top. In other words, x = 0, y = height - 1
        i = 0
        x = 0
        y = 4
        while y >= 0:
            while x < 5:
                char = layout_string[i]
                template[char].create_instance(comp_level, self.loader_level._entity_index, _x=x, _y=y)
                i += 2
                x += 1
            x = 0
            y -= 1

        self.loader_level._load_level_cells(template, layout_string, func_level)

        equal = True
        try:
            for x in range(0, 5):
                for y in range(0, 5):
                    if comp_level._cells[x][y] != func_level._cells[x][y]:
                        print comp_level[x][y]
                        print func_level[x][y]
                        equal = False
        except TypeError:
            self.assertFalse(True, "The function has not yet been implemented.")

        self.assertTrue(equal)

    def test_load_level(self):
        self.loader_level._load_level(0)
        self.assertFalse(True)

    def test_get_level(self):
        self.assertFalse(True)

    def test_can_locate_player_controlled_entity(self):
        self.assertFalse(True)

suite = unittest.TestLoader().loadTestsFromTestCase(TestLoaderLevelV1)
unittest.TextTestRunner(verbosity=2).run(suite)
