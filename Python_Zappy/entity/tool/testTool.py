__author__ = 'Travis Moy'

import unittest


class TestTool(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_satisfies_LOS(self):
        self.assertTrue(False)

    def test_location_in_range(self):
        self.assertTrue(False)

    def test_user_has_energy(self):
        self.assertTrue(False)

suite = unittest.TestLoader().loadTestsFromTestCase(TestTool)
unittest.TextTestRunner(verbosity=2).run(suite)