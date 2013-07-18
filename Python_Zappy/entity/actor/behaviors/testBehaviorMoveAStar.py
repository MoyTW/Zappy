__author__ = 'Travis Moy'

import unittest
import loader.oldLoaderLevel
import entity.actor.Adversary as Adversary
import entity.actor.behaviors.BehaviorMoveAStar as BehaviorMoveAStar
import entity.actor.senses.SenseSeismic as SenseSeismic
from level.commands.command_fragments import LevelMoveEntity


class TestBehaviorMoveAStar(unittest.TestCase):

    def setUp(self):
        self.loader_level = loader.oldLoaderLevel.oldLoaderLevel('entity/actor/behaviors/behavior_test_levels')
        self.level = self.loader_level.get_level(0)
        self.adversary = Adversary.Adversary(99, self.level.view, _senses=[SenseSeismic.SenseSeismic(5)])
        self.behavior = BehaviorMoveAStar.BehaviorMoveAStar()

    def tearDown(self):
        self.loader_level = None
        self.level = None
        self.adversary = None
        self.behavior = None

    def special_can_execute_from(self, x, y, expected_result, player_eid, level_view, adversary):
        """:type expected_result: bool"""
        self.level.place_entity_at(self.adversary, x, y)
        if expected_result is True:
            self.assertTrue(self.behavior._special_can_execute(player_eid, level_view, adversary))
        else:
            self.assertFalse(self.behavior._special_can_execute(player_eid, level_view, adversary))
        self.level.remove_entity_from(self.adversary, x, y)

    def test_special_can_execute(self):
        params = (self.level.player_actor.eid, self.level.view, self.adversary)
        pass

    def test_execute_effects(self):
        player_eid = self.level.player_actor.eid

        self.level.place_entity_at(self.adversary, 3, 3)
        self.adversary.turn_begin()
        self.behavior._execute_effects(player_eid, self.level.view, self.adversary)
        self.assertEqual(len(self.level.command_log), 1)
        self.assertTrue(isinstance(self.level.command_log[0][0], LevelMoveEntity))

suite = unittest.TestLoader().loadTestsFromTestCase(TestBehaviorMoveAStar)
unittest.TextTestRunner(verbosity=2).run(suite)