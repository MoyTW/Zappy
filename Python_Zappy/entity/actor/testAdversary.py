__author__ = 'Travis Moy'

import unittest
import entity.actor.Adversary as Adversary
import entity.actor.senses.SenseSeismic as SenseSeismic
import loader.LoaderLevel
from entity.actor.behaviors.BehaviorMoveStupidHorizontal import BehaviorMoveStupidHorizontal
from entity.actor.behaviors.BehaviorMoveStupidVertical import BehaviorMoveStupidVertical


class TestAdversary(unittest.TestCase):

    def setUp(self):
        horizontal = BehaviorMoveStupidHorizontal()
        vertical = BehaviorMoveStupidVertical()

        self.level = loader.LoaderLevel.LoaderLevel('entity/actor/behaviors/behavior_test_levels').get_level(0)
        self.adversary = Adversary.Adversary(level=self.level, senses=SenseSeismic.SenseSeismic(5),
                                             behaviors=[horizontal, vertical])

    def tearDown(self):
        self.level = None
        self.adversary = None

    def test_multiple_passes(self):
        self.adversary._max_moves = 3
        self.level.place_entity_at(self.adversary, 0, 0)
        self.assertTrue(self.adversary.take_action())
        self.assertEqual(self.adversary.get_coords(), (1, 1))
        self.level.remove_entity_from(self.adversary, *self.adversary.get_coords())
        self.assertEqual(self.adversary.get_current_moves(), 1)

    def test_behaviors_ordering(self):
        # Test that if first fails, goes to second.
        self.level.place_entity_at(self.adversary, 1, 0)
        self.assertTrue(self.adversary.take_action())
        self.assertEqual(self.adversary.get_coords(), (1, 1))
        self.level.remove_entity_from(self.adversary, *self.adversary.get_coords())

        # Test that the first is executed if it does not fail.
        self.level.place_entity_at(self.adversary, 0, 0)
        self.assertTrue(self.adversary.take_action())
        self.assertEqual(self.adversary.get_coords(), (1, 0))
        self.level.remove_entity_from(self.adversary, *self.adversary.get_coords())

        # Test that nothing happens if both fail.
        self.level.place_entity_at(self.adversary, 1, 1)
        self.assertFalse(self.adversary.take_action())
        self.assertEqual(self.adversary.get_coords(), (1, 0))
        self.level.remove_entity_from(self.adversary, *self.adversary.get_coords())

suite = unittest.TestLoader().loadTestsFromTestCase(TestAdversary)
unittest.TextTestRunner(verbosity=2).run(suite)