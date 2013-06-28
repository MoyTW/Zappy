__author__ = 'Travis Moy'

import unittest
import entity.actor.Actor as Actor
import entity.actor.senses.SenseSight as SenseSight
import entity.actor.effects.EffectBlind as EffectBlind


class TestEffectBlind(unittest.TestCase):

    def setUp(self):
        self.actor = Actor.Actor(None, _senses=[
            SenseSight.SenseSight(4),
            SenseSight.SenseSight(1)
        ])

    def tearDown(self):
        self.actor = None

    def test_removes_all_sight_senses(self):
        self.actor.apply_status_effect(EffectBlind.EffectBlind(10, self.actor))
        self.actor.turn_begin()
        self.actor.turn_end()
        self.assertEqual(len(self.actor._senses), 0)

    def test_expires_properly(self):
        self.actor.apply_status_effect(EffectBlind.EffectBlind(1, self.actor))
        self.actor.turn_begin()
        self.actor.turn_end()
        self.assertEqual(len(self.actor._senses), 2)

suite = unittest.TestLoader().loadTestsFromTestCase(TestEffectBlind)
unittest.TextTestRunner(verbosity=2).run(suite)
