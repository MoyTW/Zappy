__author__ = 'Travis Moy'

import unittest
import z_algs


def no_obstruction(x, y):
    obstructions = [(0, 3), (3, 3), (0, 4), (0, 5), (1, 5)]
    if (x, y) in obstructions:
        return False
    return True


def stops_at_y_is_three(x, y):
    if y >= 3:
        return False
    return True


class TestZAlgs(unittest.TestCase):

    def setUp(self):
        self.algs = z_algs.ZappyAlgs()

    def tearDown(self):
        self.algs = None

    def test_all_coords_in_range(self):
        self.assertEqual(1, len(self.algs.calc_coords_in_range(_range=0, x_center=5, y_center=5)))
        result_range_1 = self.algs.calc_coords_in_range(_range=1, x_center=5, y_center=5)
        self.assertEqual(5, len(result_range_1))
        comparsion_1 = set([(5, 5), (5, 6), (5, 4), (4, 5), (6, 5)])
        self.assertEqual(comparsion_1, result_range_1)
        self.assertEqual(13, len(self.algs.calc_coords_in_range(_range=2, x_center=5, y_center=5)))
        self.assertEqual(25, len(self.algs.calc_coords_in_range(_range=3, x_center=5, y_center=5)))

    def test_add_obstruction(self):
        obstructions = [z_algs.CellAngles(0, .125, .25), z_algs.CellAngles(.6, .65, .7)]
        obstructions = self.algs._add_obstruction(obstructions, z_algs.CellAngles(.9, .925, .95))
        self.assertEqual(len(obstructions), 3)
        obstructions = self.algs._add_obstruction(obstructions, z_algs.CellAngles(.65, .8, .95))
        self.assertEqual(len(obstructions), 2)

        obstructions = [z_algs.CellAngles(0, .125, .25), z_algs.CellAngles(.6, .65, .7), z_algs.CellAngles(.3, .35, .4)]
        obstructions = self.algs._add_obstruction(obstructions, z_algs.CellAngles(0, .5, 1.0))
        self.assertEqual(len(obstructions), 1)
        self.assertEqual(obstructions[0].near, 0)
        self.assertEqual(obstructions[0].far, 1)

    def test_cell_is_obstructed(self):
        obstructions = [z_algs.CellAngles(0.0, .125, .25), z_algs.CellAngles(.75, .875, 1)]
        angle = 1.0 / 6.0
        cell_passes = z_algs.CellAngles(angle, angle + angle * .5, angle + angle)
        self.assertTrue(self.algs._cell_is_visible(cell_passes, obstructions))
        cell_fails = z_algs.CellAngles(angle * 5, angle * 5 + angle * .5, angle * 5 + angle)
        self.assertFalse(self.algs._cell_is_visible(cell_fails, obstructions))

suite = unittest.TestLoader().loadTestsFromTestCase(TestZAlgs)
unittest.TextTestRunner(verbosity=2).run(suite)