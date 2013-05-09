__author__ = 'Travis Moy'

import unittest


class TestLevel(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_init(self):
        self.assertTrue(False)

    def test_cell_at(self):
        self.assertTrue(False)

    def test_place_entity_at(self):
        self.assertTrue(False)

    def test_remove_entity_from(self):
        self.assertTrue(False)

suite = unittest.TestLoader().loadTestsFromTestCase(TestLevel)
unittest.TextTestRunner(verbosity=2).run(suite)