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
        cell.add_entity(Actor.Actor(0, None))
        cell.add_entity(Actor.Actor(1, None))
        cell.add_entity(Actor.Actor(2, None))

        self.one_square = Level.Level(info)
        self.one_square.set_cells([[cell]])

    def tearDown(self):
        self.one_square = None

    def test_get_eids_at(self):
        self.assertEqual(sorted(self.one_square.view.get_eids_at(0, 0)), sorted([1, 0, 2]))

    def test_get_all_eids(self):
        self.assertEqual(sorted(self.one_square.view.get_all_eids()), sorted([1, 0, 2]))

suite = unittest.TestLoader().loadTestsFromTestCase(TestLevelView)
unittest.TextTestRunner(verbosity=2).run(suite)