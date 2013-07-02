__author__ = 'Travis Moy'

import unittest
import loader.oldLoaderLevel as LoaderLevel
import entity.actor.effects.EffectEnrage as EffectEnrage
import entity.actor.Adversary as Adversary
import entity.actor.senses.SenseSeismic as SenseSeismic


class TestEffectEnrage(unittest.TestCase):

    def setUp(self):
        loader = LoaderLevel.oldLoaderLevel('entity/actor/behaviors/behavior_test_levels')
        self.level = loader.get_level(0)
        self.control = loader.get_level_controller(0)

        self.enragee = Adversary.Adversary(self.level, _senses=[SenseSeismic.SenseSeismic(9)])
        self.level.place_entity_at(self.enragee, 1, 3)

        self.enrager = Adversary.Adversary(self.level, _senses=[SenseSeismic.SenseSeismic(9)])
        self.level.place_entity_at(self.enrager, 3, 3)

    def tearDown(self):
        self.level = None
        self.control = None
        self.enragee = None
        self.enrager = None

    def test_changes_target(self):
        self.enragee.turn_begin()
        self.assertEqual(self.enragee.select_target(), self.level.player_actor)

        enrage = EffectEnrage.EffectEnrage(5, self.enragee, self.enrager)
        enrage_func = enrage._select_target_override

        self.enragee.apply_status_effect(enrage)
        self.control.turn_has_ended()
        self.assertEqual(self.enragee.select_target(), self.enrager)
        self.assertEqual(enrage_func, self.enragee.select_target)

    def test_expires_properly(self):
        self.enragee.turn_begin()
        self.assertEqual(self.enragee.select_target(), self.level.player_actor)

        enrage = EffectEnrage.EffectEnrage(1, self.enragee, self.enrager)
        old_func = self.enragee.select_target
        enrage_func = enrage._select_target_override

        self.enragee.apply_status_effect(enrage)
        self.control.turn_has_ended()
        self.control.turn_has_ended()

        self.assertEqual(self.enragee.select_target(), self.level.player_actor)
        self.assertNotEqual(old_func, enrage_func)

suite = unittest.TestLoader().loadTestsFromTestCase(TestEffectEnrage)
unittest.TextTestRunner(verbosity=2).run(suite)