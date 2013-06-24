__author__ = 'Travis Moy'

import unittest
import loader.LoaderLevelLVL
import level.LevelInfo
import dummies.DummyLoaderEntityIndex
import pyglet
import loader.LoaderEntityIndex


class TestLoaderLevel(unittest.TestCase):
    def setUp(self):
        pyglet.resource.path = ['@', '.']
        pyglet.resource.reindex()

        self.loader = loader.LoaderLevelLVL.LoaderLevelLVL('loader/test_levels')
        self.loader._entity_index = dummies.DummyLoaderEntityIndex.DummyLoaderEntityIndex()

        resource_loader = pyglet.resource.Loader('@assets')
        self.default_preview = resource_loader.image('images/defaults/default_preview.png')

        self.level_info_0 = level.LevelInfo.LevelInfo('This is a test level!', 0, 5, 6)
        self.level_info_1 = level.LevelInfo.LevelInfo('Four-Square', 1, 2, 2)
        self.level_info_2 = level.LevelInfo.LevelInfo('Rectangle', 2, 8, 3)

    def setUpLevels(self):
        # Set up level 0
        cells_0 = [[level.Cell.Cell(image_file='images/floor.png', passable=True) for _ in range(6)] for _ in range(5)]
        for i in range(5):
            cells_0[i][5] = level.Cell.Cell(image_file='images/wall.png', passable=False)
            cells_0[i][4] = level.Cell.Cell(image_file='images/wall.png', passable=False)
            cells_0[i][1] = level.Cell.Cell(image_file='images/wall.png', passable=False)

        self.level_0 = level.Level.Level(self.level_info_0, cells_0)
        self.level_0.place_entity_at(self.loader._entity_index.create_entity_by_name('TestObj', None), 0, 0)

        # Set up level 1
        cells_1 = [[level.Cell.Cell(image_file='images/floor.png', passable=True) for _ in range(2)] for _ in range(2)]
        self.level_1 = level.Level.Level(self.level_info_1, cells_1)
        self.level_1.place_entity_at(self.loader._entity_index.create_entity_by_name('TestObj', None), 0, 1)

        # Set up level 2
        cells_2 = [[level.Cell.Cell(image_file='images/floor.png', passable=True) for _ in range(3)] for _ in range(8)]
        self.level_2 = level.Level.Level(self.level_info_2, cells_2)
        self.level_2.place_entity_at(self.loader._entity_index.create_entity_by_name('TestObj', None), 1, 1)
        self.level_2.place_entity_at(self.loader._entity_index.create_entity_by_name('TestObj', None), 1, 1)
        self.level_2.place_entity_at(self.loader._entity_index.create_entity_by_name('TestObj', None), 0, 1)
        self.level_2.place_entity_at(self.loader._entity_index.create_entity_by_name('TestObj', None), 0, 1)
        self.level_2.place_entity_at(self.loader._entity_index.create_entity_by_name('TestObj', None), 1, 2)
        self.level_2.place_entity_at(self.loader._entity_index.create_entity_by_name('TestObj', None), 1, 2)

    def tearDown(self):
        pass

    def test_load_level_preview(self):
        resource_loader = pyglet.resource.Loader('@loader')
        self.assertEqual(self.default_preview.width, self.loader._return_level_preview(2).width)
        preview_image_level_zero = resource_loader.image('test_levels/preview_images/0.png')
        self.assertEqual(preview_image_level_zero.width, self.loader._return_level_preview(0).width)

    def test_load_all_levels_infos(self):
        self.loader._load_all_levels_infos()

        self.assertTrue(len(self.loader._levels) == 5, "The loader loaded an incorrect number of levels!")
        self.assertTrue(self.loader._levels.get(1).get_level_info() == self.level_info_1)
        self.assertTrue(self.loader._levels.get(2).get_level_info() == self.level_info_2)

    def test_get_level_info(self):
        self.loader._load_all_levels_infos()

        self.assertTrue(self.loader.get_level_info(1) == self.level_info_1)
        self.assertTrue(self.loader.get_level_info(15) is None)

    def test_load_level(self):
        self.setUpLevels()
        try:
            self.loader._load_level(1)
            self.assertEquals(self.loader._levels[1], self.level_1)
            self.loader._load_level(2)
            self.assertEquals(self.loader._levels[2], self.level_2)
        except KeyError:
            self.assertFalse(True, "KeyError occurred - loading not properly implemented.")

    def test_get_level(self):
        self.setUpLevels()
        self.assertEquals(self.level_1, self.loader.get_level(1))
        self.assertEquals(self.level_2, self.loader.get_level(2))
        self.assertTrue(self.loader.get_level(-3) is None)
        self.assertTrue(self.loader.get_level(12) is None)

    def test_can_locate_player_controlled_entity(self):
        self.loader._entity_index = loader.LoaderEntityIndex.LoaderEntityIndex()
        level_5 = self.loader.get_level(5)
        player_actor = level_5.get_player_actor()
        try:
            self.assertEqual((1, 1), (player_actor._x, player_actor._y))
        except AttributeError:
            self.assertFalse(True, "Is not returning the appropriate actor!")

suite = unittest.TestLoader().loadTestsFromTestCase(TestLoaderLevel)
unittest.TextTestRunner(verbosity=2).run(suite)