__author__ = 'Travis Moy'

import unittest
import loader.LoaderLevel
import level.LevelInfo


class TestLoaderLevel(unittest.TestCase):
    def setUp(self):
        self.loader = loader.LoaderLevel.LoaderLevel()
        self.loader.LEVEL_DIR = '/test_levels'

        self.level_info_0 = level.LevelInfo.LevelInfo('This is a test level!', 0, 5, 6)
        self.level_info_1 = level.LevelInfo.LevelInfo('Four-Square', 1, 2, 2)
        self.level_info_2 = level.LevelInfo.LevelInfo('Rectangle', 2, 8, 2)

    def tearDown(self):
        pass

    def test_load_all_levels_infos(self):
        self.loader.load_all_levels_infos()

        print "len(loader._levels) is {0}".format(len(self.loader._levels))

        self.assertTrue(len(self.loader._levels) == 3, "The loader loaded an incorrect number of levels!")
        self.assertTrue(self.loader._levels.get(0) == self.level_info_0)
        self.assertTrue(self.loader._levels.get(1) == self.level_info_1)
        self.assertTrue(self.loader._levels.get(2) == self.level_info_2)

    def test_get_level_info(self):
        self.loader.load_all_levels_infos()

        self.assertTrue(self.loader.get_level_info(1) == self.level_info_1)
        self.assertTrue(self.loader.get_level_info(5) is None)

    def test_load_level(self):
        self.assertTrue(False)

    def test_get_level(self):
        self.assertTrue(False)

suite = unittest.TestLoader().loadTestsFromTestCase(TestLoaderLevel)
unittest.TextTestRunner(verbosity=2).run(suite)