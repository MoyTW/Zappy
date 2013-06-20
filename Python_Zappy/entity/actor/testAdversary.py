__author__ = 'Travis Moy'

import unittest
import entity.actor.Adversary as Adversary
import entity.actor.senses.SenseSeismic as SenseSeismic
import loader.LoaderLevel
from entity.actor.behaviors.BehaviorMoveStupidHorizontal import BehaviorMoveStupidHorizontal
from entity.actor.behaviors.BehaviorMoveStupidVertical import BehaviorMoveStupidVertical
from entity.actor.Faction import FACTIONS


class TestAdversary(unittest.TestCase):

    def setUp(self):
        horizontal = BehaviorMoveStupidHorizontal(_move_cost=1)
        vertical = BehaviorMoveStupidVertical(_move_cost=1)

        self.level = loader.LoaderLevel.LoaderLevel('entity/actor/behaviors/behavior_test_levels').get_level(0)
        self.adversary = Adversary.Adversary(_level=self.level, _senses=[SenseSeismic.SenseSeismic(5)],
                                             behaviors=[horizontal, vertical])

    def tearDown(self):
        self.level = None
        self.adversary = None

    def test_multiple_passes(self):
        self.adversary._max_moves = 3
        self.adversary.replenish_moves()
        self.level.place_entity_at(self.adversary, 0, 0)
        self.assertTrue(self.adversary.take_action())
        self.assertEqual(self.adversary.get_coords(), (1, 1))
        self.level.remove_entity_from(self.adversary, *self.adversary.get_coords())
        self.assertEqual(self.adversary.get_current_moves(), 1)

    def test_second_executed_if_first_not(self):
        # Test that if first fails, goes to second.
        self.level.place_entity_at(self.adversary, 1, 0)
        self.assertTrue(self.adversary.take_action())
        self.assertEqual(self.adversary.get_coords(), (1, 1))
        self.level.remove_entity_from(self.adversary, *self.adversary.get_coords())

    def test_first_executed_second_not(self):
        self.level.place_entity_at(self.adversary, 0, 0)
        self.assertTrue(self.adversary.take_action())
        self.assertEqual(self.adversary.get_coords(), (1, 0))
        self.level.remove_entity_from(self.adversary, *self.adversary.get_coords())

    def test_neither_executed(self):
        # Test that nothing happens if both fail.
        self.level.place_entity_at(self.adversary, 1, 1)
        self.assertFalse(self.adversary.take_action())
        self.assertEqual(self.adversary.get_coords(), (1, 1))
        self.level.remove_entity_from(self.adversary, *self.adversary.get_coords())

    def test_select_target(self):
        self.adversary._faction = FACTIONS.TEST_0
        self.high_threat = Adversary.Adversary(_level=self.level, _faction=FACTIONS.TEST_1, _base_threat=5)
        self.no_threat = Adversary.Adversary(_level=self.level, _faction=FACTIONS.TEST_1, _base_threat=0)

        self.level.place_entity_at(self.adversary, 1, 3)
        self.level.place_entity_at(self.high_threat, 0, 4)
        self.level.place_entity_at(self.no_threat, 0, 3)

        self.adversary.detect_entities()
        self.assertEqual(self.high_threat, self.adversary.select_target())

suite = unittest.TestLoader().loadTestsFromTestCase(TestAdversary)
unittest.TextTestRunner(verbosity=2).run(suite)