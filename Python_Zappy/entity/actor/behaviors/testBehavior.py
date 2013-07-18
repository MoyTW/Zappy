__author__ = 'Travis Moy'

import unittest
import loader.oldLoaderLevel
import entity.actor.Adversary as Adversary
import entity.actor.behaviors.Behavior as Behavior
import entity.actor.senses.SenseSeismic as SenseSeismic


class TestBehavior(unittest.TestCase):

    def setUp(self):
        self.loader_level = loader.oldLoaderLevel.oldLoaderLevel('entity/actor/behaviors/behavior_test_levels')
        self.level = self.loader_level.get_level(0)
        self.adversary = Adversary.Adversary(0, self.level.view, _senses=[SenseSeismic.SenseSeismic(5)])
        self.behavior = Behavior.Behavior(_move_cost=1)

    def tearDown(self):
        self.loader_level = None
        self.level = None
        self.adversary = None
        self.behavior = None

    def test_can_execute(self):
        player_eid = self.level.player_actor.eid

        # Test that it can execute if it has moves
        self.assertTrue(self.behavior._can_execute(player_eid, self.level.view, self.adversary))

        # Test that it cannot execute if it's without moves
        self.adversary.use_moves(self.adversary.current_moves)
        self.assertFalse(self.behavior._can_execute(player_eid, self.level.view, self.adversary))

    def test_uses_movement_points(self):
        self.level.place_entity_at(self.adversary, 0, 0)
        self.adversary.turn_begin()
        start_moves = self.adversary.current_moves
        self.assertTrue(self.behavior.attempt_to_execute(self.level.player_actor.eid, self.level.view, self.adversary))
        self.assertLess(self.adversary.current_moves, start_moves)

suite = unittest.TestLoader().loadTestsFromTestCase(TestBehavior)
unittest.TextTestRunner(verbosity=2).run(suite)