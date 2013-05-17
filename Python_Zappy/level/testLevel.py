__author__ = 'Travis Moy'

import unittest
import level
import pyglet


class TestLevel(unittest.TestCase):
    def setUp(self):
        pyglet.resource.path = ['@level.Cell', '.']
        pyglet.resource.reindex()
        self.default_image_path = 'test_images/defaultcell.png'

        width = 5
        height = 3

        self.test_info = level.LevelInfo.LevelInfo("Test Level", 0, width, height)
        self.test_cells = [[level.Cell.Cell(self.default_image_path) for h in range(height)] for w in range(width)]

        self.empty_test_level = level.Level.Level(self.test_info)
        self.initialized_test_level = level.Level.Level(self.test_info, self.test_cells)

    def tearDown(self):
        pass

    def test_cells_are_none(self):
        self.assertEquals(self.empty_test_level.cells_are_none(), True)
        self.assertEquals(self.initialized_test_level.cells_are_none(), False)

    # If you attempt to set the cells of an already-set Level, a LevelCellsAlreadySetError is raised.
    def test_set_cells(self):
        self.empty_test_level.set_cells(self.test_cells)
        self.assertEquals(self.empty_test_level._cells, self.test_cells)

        try:
            self.initialized_test_level.set_cells(self.test_cells)
            self.assertFalse(True, "Level.set_cells() did not throw an exception when attempting to assign cells to an"
                                   "already initialized Level!")
        except level.levelExceptions.LevelCellsAlreadySetError as err:
            pass

    def test_get_level_info(self):
        self.assertEquals(self.test_info, self.empty_test_level.get_level_info())

    def test_get_cell_at(self):
        height = 5
        width = 2
        test_strs = [["{0},{1}".format(w, h) for h in range(height)] for w in range(width)]
        self.empty_test_level.set_cells(test_strs)
        self.assertEquals("1,2", self.empty_test_level.get_cell_at(1, 2))
        self.assertEquals("0,4", self.empty_test_level.get_cell_at(0, 4))
        self.assertEquals(None, self.empty_test_level.get_cell_at(-3, 12))

    def test_get_passable(self):
        self.initialized_test_level._cells[2][2]._passable = False
        self.assertEquals(self.initialized_test_level.get_cell_at(2, 2).get_passable(), False)
        self.initialized_test_level._cells[3][1]._passable = False
        self.assertEquals(self.initialized_test_level.get_cell_at(3, 1).get_passable(), False)

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
            c_x, c_y = self.initialized_test_level.find_coordinates_of_entity(teststr)
            self.assertEquals(c_x, 3)
            self.assertEquals(c_x, 2)
        except TypeError:
            self.assertFalse(True, "Level.find_coordinates_of_entity() not returning an iterable with 2 values.")

suite = unittest.TestLoader().loadTestsFromTestCase(TestLevel)
unittest.TextTestRunner(verbosity=2).run(suite)