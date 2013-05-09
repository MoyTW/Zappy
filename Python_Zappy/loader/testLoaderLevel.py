__author__ = 'Travis Moy'

import unittest


class TestLoaderLevel(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_load_all_levels_infos(self):
        self.assertTrue(False)

suite = unittest.TestLoader().loadTestsFromTestCase(TestLoaderLevel)
unittest.TextTestRunner(verbosity=2).run(suite)