__author__ = 'Travis Moy'

import unittest
import loader.oldLoaderLevel as LoaderLevel
import entity.tool.ToolSamplingLaser as ToolSamplingLaser
import entity.environmentals.Environmental as Environmental
import entity.actor.Adversary as Adversary
import entity.actor.effects.EffectBlind as EffectBlind
import entity.actor.effects.EffectEnrage as EffectEnrage
from z_defs import RANK
import warnings


class TestToolSamplingLaser(unittest.TestCase):

    def setUp(self):
        loader = LoaderLevel.oldLoaderLevel('entity/actor/behaviors/behavior_test_levels')
        self.level = loader.get_level(0)
        self.zappy = self.level.player_actor
        self.tool = ToolSamplingLaser.ToolSamplingLaser(90, _level=self.level.view, _user=self.zappy)
        self.zappy._tools.append(self.tool)

    def tearDown(self):
        self.level = None
        self.zappy = None
        self.tool = None

    def test_on_None(self):
        self.assertFalse(self.tool.use_on_entity(None))

    def test_on_env(self):
        env = Environmental.Environmental(80, self.level, _max_hp=100)
        self.level.place_entity_at(env, 2, 2)
        self.tool._damage = 10
        self.tool.use_on_entity(env.eid)
        self.assertEqual(env.current_hp, 90)

    def test_on_weak(self):
        weak = Adversary.Adversary(80, self.level, _rank=RANK.WEAK)
        self.level.place_entity_at(weak, 2, 2)
        self.tool.use_on_entity(weak.eid)
        self.assertTrue(weak.is_destroyed())

    def test_on_average(self):
        try:
            average = Adversary.Adversary(80, self.level, _rank=RANK.AVERAGE)
            self.level.place_entity_at(average, 2, 2)
            self.tool.use_on_entity(average.eid)
            self.assertEqual(len(average.get_status_effects()), 1)
            effect = average.get_status_effects()[0]
            self.assertTrue(isinstance(effect, EffectBlind.EffectBlind))
            self.assertEqual(effect._duration, self.tool._blind_duration)
        except AttributeError as e:
            warnings.warn(e.message)
            self.assertTrue(False)

    def test_on_powerful_and_terrifying(self):
        try:
            powerful = Adversary.Adversary(80, self.level.view, _rank=RANK.POWERFUL)
            self.level.place_entity_at(powerful, 2, 2)
            self.tool.use_on_entity(powerful.eid)
            self.assertEqual(len(powerful.get_status_effects()), 1)
            powerful_effect = powerful.get_status_effects()[0]
            self.assertTrue(isinstance(powerful_effect, EffectEnrage.EffectEnrage))
            self.assertEqual(powerful_effect._duration, self.tool._enrage_duration)

            terrifying = Adversary.Adversary(70, self.level, _rank=RANK.POWERFUL)
            self.level.place_entity_at(terrifying, 2, 2)
            self.tool.use_on_entity(terrifying.eid)
            self.assertEqual(len(terrifying.get_status_effects()), 1)
            terrifying_effect = terrifying.get_status_effects()[0]
            self.assertTrue(isinstance(terrifying_effect, EffectEnrage.EffectEnrage))
            self.assertEqual(terrifying_effect._duration, self.tool._enrage_duration)
        except AttributeError as e:
            warnings.warn(e.message)
            self.assertTrue(False)

suite = unittest.TestLoader().loadTestsFromTestCase(TestToolSamplingLaser)
unittest.TextTestRunner(verbosity=2).run(suite)