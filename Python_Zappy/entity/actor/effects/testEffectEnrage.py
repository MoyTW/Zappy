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
        self.assertEqual(self.enragee.select_target(), self.level.get_player_actor())
        self.enragee.apply_status_effect(EffectEnrage.EffectEnrage(5, self.enragee, self.enrager))
        self.assertEqual(self.enragee.select_target(), self.enrager)

    def test_expires_properly(self):
        self.assertEqual(self.enragee.select_target(), self.level.get_player_actor())

        enrage = EffectEnrage.EffectEnrage(5, self.enragee, self.enrager)
        self.enragee.apply_status_effect(enrage)
        enrage.unapply()

        self.assertEqual(self.enragee.select_target(), self.level.get_player_actor())

suite = unittest.TestLoader().loadTestsFromTestCase(TestEffectEnrage)
unittest.TextTestRunner(verbosity=2).run(suite)