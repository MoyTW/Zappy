__author__ = 'Travis Moy'

import unittest
import entity.tool.Tool as Tool
import entity.actor.Actor as Actor
from z_algs import Z_ALGS
import loader.oldLoaderLevel as LoaderLevel


class TestTool(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_satisfies_LOS(self):
        loader = LoaderLevel.oldLoaderLevel('entity/actor/behaviors/behavior_test_levels')
        level = loader.get_level(0)

        actor = Actor.Actor(0, level)
        tool = Tool.Tool(0, level, _user=actor, _requires_LOS=True)
        level.place_entity_at(actor, 1, 0)

        self.assertTrue(tool._satisfies_LOS(_x=1, _y=0))
        self.assertFalse(tool._satisfies_LOS(_x=3, _y=0))
        self.assertFalse(tool._satisfies_LOS(_x=3, _y=2))
        self.assertTrue(tool._satisfies_LOS(_x=0, _y=1))

    def test_location_in_range(self):
        actor = Actor.Actor(0, _level=None)
        actor._x = 5
        actor._y = 5
        tool = Tool.Tool(0, None, _user=actor, _range=3)

        self.assertTrue(tool._location_in_range(5, 5))
        self.assertTrue(tool._location_in_range(2, 5))
        self.assertFalse(tool._location_in_range(2, 4))
        self.assertFalse(tool._location_in_range(3, 3))

    def test_user_has_energy(self):
        actor = Actor.Actor(0, _level=None, _max_energy=15)
        cheap_tool = Tool.Tool(0, None, _user=actor, _energy_cost=10)
        goldilocks_tool = Tool.Tool(0, None, _user=actor, _energy_cost=15)
        expensive_tool = Tool.Tool(0, None, _user=actor, _energy_cost=20)

        self.assertTrue(cheap_tool.user_has_energy())
        self.assertTrue(goldilocks_tool.user_has_energy())
        self.assertFalse(expensive_tool.user_has_energy())

    def test_user_has_moves(self):
        actor = Actor.Actor(0, _level=None)
        tool = Tool.Tool(0, None, _user=actor)

        self.assertTrue(tool._user_has_moves())
        actor.use_moves(1)
        self.assertFalse(tool._user_has_moves())

    def test_cooldown(self):
        actor = Actor.Actor(0, _level=None)
        tool = Tool.Tool(0, None, _user=actor, _cooldown=5)

        tool.use_on_entity(None)
        self.assertEqual(tool.turns_until_ready, 6)

        tool.turn_passed()
        self.assertEqual(tool.turns_until_ready, 5)

suite = unittest.TestLoader().loadTestsFromTestCase(TestTool)
unittest.TextTestRunner(verbosity=2).run(suite)