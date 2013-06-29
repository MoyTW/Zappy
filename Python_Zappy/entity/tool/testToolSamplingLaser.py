__author__ = 'Travis Moy'

import unittest
import loader.oldLoaderLevel as LoaderLevel
import entity.tool.ToolSamplingLaser as ToolSamplingLaser
import entity.environmentals.Environmental as Environmental
import entity.actor.Adversary as Adversary
import entity.actor.effects.EffectBlind as EffectBlind
import entity.actor.effects.EffectEnrage as EffectEnrage
from z_defs import RANK


class TestToolSamplingLaser(unittest.TestCase):

    def setUp(self):
        loader = LoaderLevel.oldLoaderLevel('entity/actor/behaviors/behavior_test_levels')
        self.level = loader.get_level(0)
        self.zappy = self.level.get_player_actor()
        self.tool = ToolSamplingLaser.ToolSamplingLaser(_level=self.level)
        self.zappy.add_tool(self.tool)

    def tearDown(self):
        self.level = None
        self.zappy = None
        self.tool = None

    def test_on_env(self):
        env = Environmental.Environmental(self.level, _max_hp=100)
        self.tool._strength = 10
        self.tool.use_on_entity(env)
        self.assertEqual(env.get_current_hp(), 90)

    def test_on_weak(self):
        weak = Adversary.Adversary(self.level, _rank=RANK.WEAK)
        self.tool.use_on_entity(weak)
        self.assertTrue(weak.is_destroyed())

    def test_on_average(self):
        try:
            average = Adversary.Adversary(self.level, _rank=RANK.AVERAGE)
            self.tool.use_on_entity(average)
            self.assertEqual(len(average.get_status_effects()), 1)
            self.assertTrue(isinstance(average.get_status_effects()[0], EffectBlind.EffectBlind))
        except AttributeError as e:
            print e.message
            self.assertTrue(False)

    def test_on_powerful_and_terrifying(self):
        try:
            powerful = Adversary.Adversary(self.level, _rank=RANK.POWERFUL)
            self.tool.use_on_entity(powerful)
            self.assertEqual(len(powerful.get_status_effects()), 1)
            self.assertTrue(isinstance(powerful.get_status_effects()[0], EffectEnrage.EffectEnrage))

            terrifying = Adversary.Adversary(self.level, _rank=RANK.POWERFUL)
            self.tool.use_on_entity(terrifying)
            self.assertEqual(len(terrifying.get_status_effects()), 1)
            self.assertTrue(isinstance(terrifying.get_status_effects()[0], EffectEnrage.EffectEnrage))
        except AttributeError as e:
            print e.message
            self.assertTrue(False)

suite = unittest.TestLoader().loadTestsFromTestCase(TestToolSamplingLaser)
unittest.TextTestRunner(verbosity=2).run(suite)