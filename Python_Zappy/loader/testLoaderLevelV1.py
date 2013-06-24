__author__ = 'Travis Moy'

import unittest
import loader.LoaderLevelV1 as LoaderLevel
import level.LevelInfo as LevelInfo


class TestLoaderLevelV1(unittest.TestCase):

    def setUp(self):
        self.loader_level = LoaderLevel.LoaderLevelV1('loader/test_levels')

    def tearDown(self):
        self.loader_level = None

    def test_load_all_levels_infos(self):
        self.assertFalse(True)

    def test_get_level_info(self):
        info = self.loader_level._load_level_info(0)
        self.assertTrue(isinstance(info, LevelInfo.LevelInfo))
        self.assertEqual(info.get_name(), 'TestLevel')
        self.assertEqual(info.get_number(), 0)
        self.assertEqual(info.get_width(), 5)
        self.assertEqual(info.get_height(), 5)

    def test_load_level(self):
        self.assertFalse(True)

    def test_get_level(self):
        self.assertFalse(True)

    def test_can_locate_player_controlled_entity(self):
        self.assertFalse(True)

suite = unittest.TestLoader().loadTestsFromTestCase(TestLoaderLevelV1)
unittest.TextTestRunner(verbosity=2).run(suite)
