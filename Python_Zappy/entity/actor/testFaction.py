__author__ = 'Travis Moy'

import unittest
import entity.actor.Faction as Faction


class TestFaction(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_add_faction_adds(self):
        faction = Faction.Faction('test_faction')
        faction.add_faction_name('friendly', faction.RELATION_FRIENDLY)
        self.assertEqual(len(faction._names_friendly_to), 1)
        faction.add_faction_name('neutral', faction.RELATION_NEUTRAL)
        self.assertEqual(len(faction._names_neutral_to), 1)
        faction.add_faction_name('hostile', faction.RELATION_HOSTILE)
        self.assertEqual(len(faction._names_hostile_to), 1)

    def test_add_faction_assigns_to_most_hostile(self):
        should_be_hostile = 'should_be_hostile'
        faction = Faction.Faction('test_faction')
        faction.add_faction_name(should_be_hostile, faction.RELATION_NEUTRAL)
        faction.add_faction_name(should_be_hostile, faction.RELATION_HOSTILE)
        self.assertEqual(len(faction._names_neutral_to), 0)
        self.assertEqual(len(faction._names_hostile_to), 1)
        self.assertEqual(faction._names_hostile_to[0], should_be_hostile)

suite = unittest.TestLoader().loadTestsFromTestCase(TestFaction)
unittest.TextTestRunner(verbosity=2).run(suite)