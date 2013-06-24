__author__ = 'Travis Moy'

import unittest
import entity.tool.Tool as Tool
import entity.actor.Actor as Actor
from z_algs import Z_ALGS
import loader.LoaderLevelLVL as LoaderLevel


class TestTool(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_satisfies_LOS(self):
        loader = LoaderLevel.LoaderLevelLVL('entity/actor/behaviors/behavior_test_levels')
        level = loader.get_level(0)

        actor = Actor.Actor(level)
        tool = Tool.Tool(level, _user=actor, _requires_LOS=True)
        level.place_entity_at(actor, 1, 0)

        self.assertTrue(tool._satisfies_LOS(_x=1, _y=0))
        self.assertFalse(tool._satisfies_LOS(_x=3, _y=0))
        self.assertFalse(tool._satisfies_LOS(_x=3, _y=2))
        self.assertTrue(tool._satisfies_LOS(_x=0, _y=1))

    def test_location_in_range(self):
        actor = Actor.Actor(_level=None)
        actor._x = 5
        actor._y = 5
        tool = Tool.Tool(None, _user=actor, _range=3)

        self.assertTrue(tool._location_in_range(5, 5))
        self.assertTrue(tool._location_in_range(2, 5))
        self.assertFalse(tool._location_in_range(2, 4))
        self.assertFalse(tool._location_in_range(3, 3))

    def test_user_has_energy(self):
        actor = Actor.Actor(_level=None, _max_energy=15)
        cheap_tool = Tool.Tool(None, _user=actor, _energy_cost=10)
        goldilocks_tool = Tool.Tool(None, _user=actor, _energy_cost=15)
        expensive_tool = Tool.Tool(None, _user=actor, _energy_cost=20)

        self.assertTrue(cheap_tool.user_has_energy())
        self.assertTrue(goldilocks_tool.user_has_energy())
        self.assertFalse(expensive_tool.user_has_energy())

    def test_user_has_moves(self):
        actor = Actor.Actor(_level=None)
        tool = Tool.Tool(None, _user=actor)

        self.assertTrue(tool._user_has_moves())
        actor.use_moves(1)
        self.assertFalse(tool._user_has_moves())


suite = unittest.TestLoader().loadTestsFromTestCase(TestTool)
unittest.TextTestRunner(verbosity=2).run(suite)