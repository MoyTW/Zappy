__author__ = 'Travis Moy'

import unittest
import loader.oldLoaderLevel as LoaderLevel
import entity.tool.ToolHoloprojector as ToolHoloprojector


class DummyActor(object):
    faction = None

    def use_moves(self, energy_cost):
        pass

    def use_energy(self, energy_cost):
        pass

class TestToolHoloprojector(unittest.TestCase):

    def setUp(self):
        loader = LoaderLevel.oldLoaderLevel('entity/actor/behaviors/behavior_test_levels')
        self.level = loader.get_level(0)
        """:type: level.Level.Level"""
        self.zappy = self.level.player_actor
        da = DummyActor()
        self.tool = ToolHoloprojector.ToolHoloprojector(0, _level=self.level.view, _user=da)
        self.zappy._tools.append(self.tool)

    def tearDown(self):
        self.level = None
        self.zappy = None
        self.tool = None

    def test_creates_entity(self):
        self.tool.use_on_location(1, 3)
        self.assertEqual(len(self.level.view.get_all_eids()), 2)

    def test_entity_expires(self):
        self.tool.use_on_location(1, 3)

        if len(self.level.view.get_eids_at(1, 3)) == 0:
            self.assertFalse("The tool is not generating any entities, cannot proceed with test.")

        hologram = self.level.view.get_eids_at(1, 3)[0]
        for _ in range(0, 10):
            hologram.turn_begin()
            hologram.turn_end()
        self.assertTrue(hologram.is_destroyed())

suite = unittest.TestLoader().loadTestsFromTestCase(TestToolHoloprojector)
unittest.TextTestRunner(verbosity=2).run(suite)