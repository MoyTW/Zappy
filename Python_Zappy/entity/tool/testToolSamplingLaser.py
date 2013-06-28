__author__ = 'Travis Moy'

import unittest
import loader.oldLoaderLevel as LoaderLevel
import entity.tool.ToolSamplingLaser as ToolSamplingLaser


class TestToolSamplingLaser(unittest.TestCase):

    def setUp(self):
        loader = LoaderLevel.oldLoaderLevel('entity/actor/behaviors/behavior_test_levels')
        self.level = loader.get_level(0)
        self.zappy = self.level.get_player_actor()
        self.tool = ToolSamplingLaser.ToolSamplingLaser(_level=self.level)
        self.zappy.add_tool(self.tool)

    def tearDown(self):
        self.level = None
        self.zappy = None
        self.tool = None

    def test_fails(self):
        self.assertFalse(True)

suite = unittest.TestLoader().loadTestsFromTestCase(TestToolSamplingLaser)
unittest.TextTestRunner(verbosity=2).run(suite)