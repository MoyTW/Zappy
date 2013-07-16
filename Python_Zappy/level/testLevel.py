__author__ = 'Travis Moy'

import unittest
import level
import pyglet
import entity.actor.Actor as Actor


class TestLevel(unittest.TestCase):
    def setUp(self):
        pyglet.resource.path = ['@level.Cell', '.']
        pyglet.resource.reindex()
        self.default_image_path = 'test_images/defaultcell.png'

        self.width = 5
        self.height = 3

        self.test_info = level.LevelInfo.LevelInfo("Test Level", 0, self.width, self.height, None)
        self.test_cells = [[level.Cell.Cell(self.default_image_path) for h in range(self.height)]
                           for w in range(self.width)]

        self.empty_test_level = level.Level.Level(self.test_info)
        self.initialized_test_level = level.Level.Level(self.test_info, self.test_cells)

    def tearDown(self):
        self.test_info = None
        self.test_cells = None
        self.empty_test_level = None
        self.initialized_test_level = None

    def test_eq(self):
        self.assertNotEqual(self.empty_test_level, self.initialized_test_level)

        lvl_eq_0 = level.Level.Level(self.test_info, self.test_cells)
        actor_0 = Actor.Actor(0, lvl_eq_0)
        lvl_eq_0.place_entity_at(actor_0, 0, 0)
        lvl_eq_1 = level.Level.Level(self.test_info, self.test_cells)
        actor_1 = Actor.Actor(0, lvl_eq_1)
        lvl_eq_1.place_entity_at(actor_1, 0, 0)

        self.assertEqual(lvl_eq_0, lvl_eq_1)

    def test_cells_are_none(self):
        self.assertEquals(self.empty_test_level.cells_are_none(), True)
        self.assertEquals(self.initialized_test_level.cells_are_none(), False)

    # If you attempt to set the cells of an already-set Level, a LevelCellsAlreadySetError is raised.
    def test_set_cells_to_empty_level(self):
        self.empty_test_level.set_cells(self.test_cells)
        self.assertEquals(self.empty_test_level._cells, self.test_cells)

    def test_set_cells_to_full_level(self):
        try:
            self.initialized_test_level.set_cells(self.test_cells)
            self.assertFalse(True, "Level.set_cells() did not throw an exception when attempting to assign cells to an"
                                   "already initialized Level!")
        except level.levelExceptions.LevelCellsAlreadySetError:
            pass

    def test_set_cells_width_mismatch_with_cells(self):
        wrong_width = [["Test" for _ in range(2)] for _ in range(3)]

        try:
            self.empty_test_level.set_cells(wrong_width)
            self.assertFalse(True, "Level.set_cells() did not throw an exception when attempting to assign a cell with"
                                   "an incorrect width!")
        except level.levelExceptions.LevelWidthNotMatchedByCells:
            pass

    def test_set_cells_height_mismatch_with_cells(self):
        wrong_height = [["Test" for _ in range(1)] for _ in range(5)]

        try:
            self.empty_test_level.set_cells(wrong_height)
            self.assertFalse(True, "Level.set_cells() did not throw an exception when attempting to assign a cell with"
                                   "an incorrect height!")
        except level.levelExceptions.LevelHeightNotMatchedByCells:
            pass

    def test_get_level_info(self):
        self.assertEquals(self.test_info, self.empty_test_level.get_level_info())

    def test_get_display_images_at(self):
        self.assertEquals(len(self.initialized_test_level.view.get_display_images_at(1, 2)), 1)
        self.assertEquals(self.initialized_test_level.view.get_display_images_at(-5, 12), None)

    def test_get_passable(self):
        self.initialized_test_level._cells[2][2].is_passable = False
        self.assertEquals(self.initialized_test_level._cells[2][2].is_passable, False)
        self.initialized_test_level._cells[3][1].is_passable = False
        self.assertEquals(self.initialized_test_level._cells[3][1].is_passable, False)

    def test_place_entity_at(self):
        teststr = "Test String!"
        self.initialized_test_level.place_entity_at(teststr, 3, 2)
        self.assertEquals(len(self.initialized_test_level._cells[3][2]._contains), 1)

    def test_remove_entity_from(self):
        teststr = "Test String!"
        self.initialized_test_level.place_entity_at(teststr, 3, 2)
        self.assertTrue(self.initialized_test_level.remove_entity_from(teststr, 3, 2))
        self.assertEquals(len(self.initialized_test_level._cells[3][2]._contains), 0)
        self.assertFalse(self.initialized_test_level.remove_entity_from(teststr, 3, 2))
        self.assertEquals(len(self.initialized_test_level._cells[3][2]._contains), 0)

    def test_find_coordinates_of_entity(self):
        teststr = "Test String!"
        self.initialized_test_level.place_entity_at(teststr, 3, 2)

        try:
            coords = self.initialized_test_level.view.find_coordinates_of_entity(teststr)
            self.assertEquals(coords[0], 3)
            self.assertEquals(coords[1], 2)
            self.assertEquals(None, self.initialized_test_level.view.find_coordinates_of_entity("Blue!"))
        except TypeError:
            self.assertFalse(True, "Level.find_coordinates_of_entity() not returning an iterable with 2 values.")

suite = unittest.TestLoader().loadTestsFromTestCase(TestLevel)
unittest.TextTestRunner(verbosity=2).run(suite)