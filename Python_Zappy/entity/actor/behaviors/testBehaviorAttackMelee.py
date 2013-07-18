__author__ = 'Travis Moy'

import unittest
import loader.oldLoaderLevel
import entity.actor.Adversary as Adversary
import entity.actor.behaviors.BehaviorAttackMelee as BehaviorAttackMelee
import entity.actor.senses.SenseSeismic as SenseSeismic
from level.commands.command_fragments import EntityDealDamage


class TestBehaviorAttackMelee(unittest.TestCase):

    def setUp(self):
        self.loader_level = loader.oldLoaderLevel.oldLoaderLevel('entity/actor/behaviors/behavior_test_levels')
        self.level = self.loader_level.get_level(0)
        self.adversary = Adversary.Adversary(0, self.level.view, _senses=[SenseSeismic.SenseSeismic(5)])
        self.behavior = BehaviorAttackMelee.BehaviorAttackMelee()

    def tearDown(self):
        self.loader_level = None
        self.level = None
        self.adversary = None
        self.behavior = None

    def test_special_can_execute(self):
        player_eid = self.level.player_actor.eid

        # Test that it can execute if same square
        self.level.place_entity_at(self.adversary, 2, 2)
        self.assertTrue(self.behavior._special_can_execute(player_eid, self.level.view, self.adversary))
        self.level.remove_entity_from(self.adversary, 2, 2)

        # Test that it can execute if adjacent
        self.level.place_entity_at(self.adversary, 2, 3)
        self.assertTrue(self.behavior._special_can_execute(player_eid, self.level.view, self.adversary))
        self.level.remove_entity_from(self.adversary, 2, 3)

        # Test that it cannot execute if not adjacent
        self.level.place_entity_at(self.adversary, 3, 3)
        self.assertFalse(self.behavior._special_can_execute(player_eid, self.level.view, self.adversary))
        self.level.remove_entity_from(self.adversary, 3, 3)

    def test_execute_effects(self):
        player_eid = self.level.player_actor.eid

        self.behavior._execute_effects(player_eid, self.level.view, self.adversary)
        self.assertEqual(len(self.level.command_log), 1)
        self.assertTrue(isinstance(self.level.command_log[0][0], EntityDealDamage))

suite = unittest.TestLoader().loadTestsFromTestCase(TestBehaviorAttackMelee)
unittest.TextTestRunner(verbosity=2).run(suite)