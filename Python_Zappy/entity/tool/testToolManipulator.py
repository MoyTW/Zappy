__author__ = 'Travis Moy'

import unittest
import loader.oldLoaderLevel as LoaderLevel
import entity.tool.ToolManipulator as ToolManipulator
import entity.environmentals.Environmental as Environmental
import entity.actor.Adversary as Adversary
import entity.Entity as Entity
from z_defs import RANK


class TestToolManipulator(unittest.TestCase):

    def setUp(self):
        loader = LoaderLevel.oldLoaderLevel('entity/actor/behaviors/behavior_test_levels')
        self.level = loader.get_level(0)

        self.zappy = self.level.player_actor
        self.tool = ToolManipulator.ToolManipulator(99, self.level.view, _user=self.zappy)
        self.zappy._tools.append(self.tool)

    def tearDown(self):
        self.level = None
        self.zappy = None
        self.tool = None

    def test_use(self):
        self.assertEqual(len(self.tool._captured_actors), 0)

        weak = Adversary.Adversary(98, self.level, _rank=RANK.WEAK)
        self.level.place_entity_at(weak, 2, 3)

        weak1 = Adversary.Adversary(97, self.level, _rank=RANK.WEAK)
        self.level.place_entity_at(weak1, 2, 3)

        self.tool.use_on_entity(weak)

        self.assertEqual(len(self.level.view.get_all_eids()), 2)
        self.assertEqual(len(self.tool._captured_actors), 1)

    def test_can_use(self):
        entity = Entity.Entity(10, self.level.view)
        self.level.place_entity_at(entity, 2, 3)
        self.assertFalse(self.tool.can_use_on_entity(entity.eid))

        weak_unstunned = Adversary.Adversary(20, self.level.view, _rank=RANK.WEAK)
        self.level.place_entity_at(weak_unstunned, 2, 3)
        self.assertFalse(self.tool.can_use_on_entity(weak_unstunned.eid))

        weak_stunned = Adversary.Adversary(30, self.level.view, _rank=RANK.WEAK)
        self.level.place_entity_at(weak_stunned, 2, 3)
        weak_stunned.is_stunned = True
        self.assertTrue(self.tool.can_use_on_entity(weak_stunned.eid))

        avg_healthy_unstunned = Adversary.Adversary(40, self.level.view, _rank=RANK.AVERAGE, _max_hp=3)
        self.level.place_entity_at(avg_healthy_unstunned, 2, 3)
        self.assertFalse(self.tool.can_use_on_entity(avg_healthy_unstunned.eid))

        avg_healthy_stunned = Adversary.Adversary(50, self.level.view, _rank=RANK.AVERAGE, _max_hp=3)
        self.level.place_entity_at(avg_healthy_stunned, 2, 3)
        avg_healthy_stunned.is_stunned = True
        self.assertFalse(self.tool.can_use_on_entity(avg_healthy_stunned.eid))

        avg_unhealthy_unstunned = Adversary.Adversary(60, self.level.view, _rank=RANK.AVERAGE, _max_hp=1)
        self.level.place_entity_at(avg_unhealthy_unstunned, 2, 3)
        self.assertFalse(self.tool.can_use_on_entity(avg_unhealthy_unstunned.eid))

        avg_unhealthy_stunned = Adversary.Adversary(70, self.level.view, _rank=RANK.AVERAGE, _max_hp=1)
        self.level.place_entity_at(avg_unhealthy_stunned, 2, 3)
        avg_unhealthy_stunned.is_stunned = True
        self.assertTrue(self.tool.can_use_on_entity(avg_unhealthy_stunned.eid))

        powerful = Adversary.Adversary(80, self.level.view, _rank=RANK.POWERFUL)
        self.level.place_entity_at(powerful, 2, 3)
        self.assertFalse(self.tool.can_use_on_entity(powerful.eid))

suite = unittest.TestLoader().loadTestsFromTestCase(TestToolManipulator)
unittest.TextTestRunner(verbosity=2).run(suite)