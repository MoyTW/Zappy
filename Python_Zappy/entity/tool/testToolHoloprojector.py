__author__ = 'Travis Moy'

import unittest
import loader.LoaderLevelLVL as LoaderLevel
import entity.tool.ToolHoloprojector as ToolHoloprojector


class TestToolHoloprojector(unittest.TestCase):

    def setUp(self):
        loader = LoaderLevel.LoaderLevelLVL('entity/actor/behaviors/behavior_test_levels')
        self.level = loader.get_level(0)
        self.zappy = self.level.get_player_actor()
        self.tool = ToolHoloprojector.ToolHoloprojector(_level=self.level)
        self.zappy.add_tool(self.tool)

    def tearDown(self):
        self.level = None
        self.zappy = None
        self.tool = None

    def test_creates_entity(self):
        self.tool.use_on_location(1, 3)
        self.assertEqual(len(self.level.get_all_entities()), 2)

    def test_entity_expires(self):
        self.tool.use_on_location(1, 3)

        if len(self.level.get_all_entities_at(1, 3)) == 0:
            self.assertFalse("The tool is not generating any entities, cannot proceed with test.")

        hologram = self.level.get_all_entities_at(1, 3)[0]
        for _ in range(0, 10):
            hologram.turn_begin()
            hologram.turn_end()
        self.assertTrue(hologram.is_destroyed())

suite = unittest.TestLoader().loadTestsFromTestCase(TestToolHoloprojector)
unittest.TextTestRunner(verbosity=2).run(suite)