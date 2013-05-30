__author__ = 'Travis Moy'

import unittest
import z_algs


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

suite = unittest.TestLoader().loadTestsFromTestCase(TestZAlgs)
unittest.TextTestRunner(verbosity=2).run(suite)