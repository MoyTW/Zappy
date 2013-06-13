__author__ = 'Travis Moy'

import unittest
import entity.tool.Tool as Tool
import entity.actor.Actor as Actor
from z_algs import Z_ALGS
import loader.LoaderLevel as LoaderLevel


class TestTool(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_satisfies_LOS(self):
        loader = LoaderLevel.LoaderLevel('entity/actor/behaviors/behavior_test_levels')
        level = loader.get_level(0)

        actor = Actor.Actor(level)
        tool = Tool.Tool(level, [], _requires_LOS=True)
        level.place_entity_at(actor, 1, 0)

        self.assertTrue(tool._satisfies_LOS(_x=1, _y=0, _user=tool, _level=level))
        self.assertFalse(tool._satisfies_LOS(_x=3, _y=0, _user=tool, _level=level))
        self.assertFalse(tool._satisfies_LOS(_x=3, _y=2, _user=tool, _level=level))
        self.assertTrue(tool._satisfies_LOS(_x=0, _y=1, _user=tool, _level=level))

    def test_location_in_range(self):
        tool = Tool.Tool(None, [], _range=3)
        actor = Actor.Actor(level=None)
        actor._x = 5
        actor._y = 5

        self.assertTrue(tool._location_in_range(5, 5, actor))
        self.assertTrue(tool._location_in_range(2, 5, actor))
        self.assertFalse(tool._location_in_range(2, 4, actor))
        self.assertFalse(tool._location_in_range(3, 3, actor))

    def test_user_has_energy(self):
        actor = Actor.Actor(level=None, max_energy=15)
        cheap_tool = Tool.Tool(None, [], _energy_cost=10)
        goldilocks_tool = Tool.Tool(None, [], _energy_cost=15)
        expensive_tool = Tool.Tool(None, [], _energy_cost=20)

        self.assertTrue(cheap_tool._user_has_energy(actor))
        self.assertTrue(goldilocks_tool._user_has_energy(actor))
        self.assertFalse(expensive_tool._user_has_energy(actor))


suite = unittest.TestLoader().loadTestsFromTestCase(TestTool)
unittest.TextTestRunner(verbosity=2).run(suite)