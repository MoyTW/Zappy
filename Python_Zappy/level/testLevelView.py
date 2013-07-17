__author__ = 'Travis Moy'

import unittest
import level.Level as Level
import level.LevelInfo as LevelInfo
import level.Cell as Cell
import entity.actor.Actor as Actor


class TestLevelView(unittest.TestCase):
    def setUp(self):
        info = LevelInfo.LevelInfo("Test", 0, 1, 1, "NSF")
        cell = Cell.Cell()
        cell.add_entity(Actor.Actor(0, None, _entity_name="One"))
        cell.add_entity(Actor.Actor(1, None, _entity_name="Two"))
        cell.add_entity(Actor.Actor(2, None, _entity_name="Three"))

        self.one_square = Level.Level(info)
        self.one_square.set_cells([[cell]])
        self.view = self.one_square.view

    def tearDown(self):
        self.one_square = None

    def test_get_eids_at(self):
        self.assertEqual(sorted(self.one_square.view.get_eids_at(0, 0)), sorted([1, 0, 2]))

    def test_get_all_eids(self):
        self.assertEqual(sorted(self.one_square.view.get_all_eids()), sorted([1, 0, 2]))

    def test_get_entity_name(self):
        self.assertEqual(self.view.get_entity_name(0), "One")
        self.assertEqual(self.view.get_entity_name(1), "Two")
        self.assertEqual(self.view.get_entity_name(2), "Three")
        self.assertEqual(self.view.get_entity_name(3), None)

suite = unittest.TestLoader().loadTestsFromTestCase(TestLevelView)
unittest.TextTestRunner(verbosity=2).run(suite)