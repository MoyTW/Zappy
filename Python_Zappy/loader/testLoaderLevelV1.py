__author__ = 'Travis Moy'

import unittest
import loader.LoaderLevelV1 as LoaderLevel
import level.LevelInfo as LevelInfo
import level.Level as Level
from z_json import JSONCONVERTER
import pyglet
import level.Cell as Cell


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
        self.assertEqual(info.get_height(), 6)

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
        layout_string = "# # # # #\n# . . . #\n# . D . #\n# . . . #\n# # # # #\n# # # # #\n"

        comp_level.replace_cells([[None for _ in range(0, 6)] for _ in range(0, 5)])

        # You start from the top. In other words, x = 0, y = height - 1
        i = 0
        x = 0
        y = 5
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
                for y in range(0, 6):
                    comp_cell = comp_level._cells[x][y]
                    func_cell = func_level._cells[x][y]
                    if comp_cell != func_cell:
                        if len(comp_cell.get_all_entities()) != len(func_cell.get_all_entities()):
                            equal = False
        except TypeError:
            self.assertFalse(True, "The function has not yet been implemented.")

        self.assertTrue(equal)

    def test_load_level_cells_handle_irregular_whitespace(self):
        template = self.create_test_template()
        layout_string = "# ##      #\n\n\n#\n # . . . #\n# . D . #\n# . . . #\n# # # # #\n# # #  # #\n"
        func_level = self.loader_level._levels[0]

        try:
            self.loader_level._load_level_cells(template, layout_string, func_level)
        except KeyError:
            threw_exception = True
            self.assertFalse(threw_exception, "Could not handle extra whitespace.")

    def test_load_level_cells_irregular_whitespace_equivalent(self):
        comp_level = Level.Level(self.loader_level.get_level_info(0))
        func_level = self.loader_level._levels[0]
        template = self.create_test_template()
        layout_string = "# # # # #\n# . . . #\n# . D . #\n# . . . #\n# # # # #\n# # # # #\n"
        irregular_layout_string = "# ##      #\n\n\n#\n # . . . #\n# . D . #\n# . . . #\n# # # # #\n# # #  # #\n"

        self.loader_level._load_level_cells(template, irregular_layout_string, comp_level)
        self.loader_level._load_level_cells(template, layout_string, func_level)

        equal = True
        try:
            for x in range(0, 5):
                for y in range(0, 6):
                    comp_cell = comp_level._cells[x][y]
                    func_cell = func_level._cells[x][y]
                    if comp_cell != func_cell:
                        if len(comp_cell.get_all_entities()) != len(func_cell.get_all_entities()):
                            equal = False
        except TypeError:
            self.assertFalse(True, "The function has not yet been implemented.")

        self.assertTrue(equal)

    def test_load_entity_list(self):
        json = '[' \
               '{"_entity": "adversaries/FastStupidSeismic.json"},' \
               '{"_entity": "adversaries/FastStupidSeismic.json", "_orders": [{"_order": "place","_x": 2,"_y": 3}]},' \
               '{"_entity": "adversaries/FastStupidSeismic.json", "_orders": [{"_order": "place","_x": 3,"_y": 3}]}' \
               ']'
        target_level = Level.Level(self.loader_level.get_level_info(0))
        target_level.replace_cells([[Cell.Cell() for _ in range(0, 6)] for _ in range(0, 5)])
        self.loader_level._load_entity_list(json, target_level)

        self.assertEqual(len(target_level.get_all_entities()), 2)
        self.assertEqual(len(target_level.get_all_entities_at(2, 3)), 1)
        self.assertEqual(len(target_level.get_all_entities_at(3, 3)), 1)

    # This is only the most cursory of tests - the components are tested already.
    # It's just here to make sure nothing blows up when you combine them.
    def test_load_level(self):
        self.loader_level._load_level(0)
        self.loader_level._load_level(1)

    def test_get_level(self):
        self.assertNotEqual(None, self.loader_level.get_level(0))
        self.assertNotEqual(None, self.loader_level.get_level(1))
        self.assertEqual(None, self.loader_level.get_level(-1))
        self.assertEqual(None, self.loader_level.get_level(15))

    def test_can_locate_player_controlled_entity(self):
        self.loader_level._load_level(0)
        l0 = self.loader_level._levels[0]
        l0_player_actor = l0.get_player_actor()
        self.assertEqual(l0_player_actor.get_coords(), (2, 3))

        self.loader_level._load_level(1)
        l1 = self.loader_level._levels[1]
        l1_player_actor = l1.get_player_actor()
        self.assertEqual(l1_player_actor.get_coords(), (0, 0))

suite = unittest.TestLoader().loadTestsFromTestCase(TestLoaderLevelV1)
unittest.TextTestRunner(verbosity=2).run(suite)
