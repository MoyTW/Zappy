__author__ = 'Travis Moy'

import level.levelExceptions


class Level:
    # cells is a rectangular grid of Cell objects.
    def __init__(self, info, cells=None):
        self._info = info
        self._cells = cells

    def cells_are_none(self):
        if self._cells is None:
            return True
        return False

    # Should throw some manner of exception if cells is not None
    def set_cells(self, cells):
        if self._cells is None:
            self._cells = cells
        else:
            raise level.levelExceptions.LevelCellsAlreadySetError("This is an error message!")

    def get_level_info(self):
        return self._info

    def get_cell_at(self, x, y):
        return self._cells[x][y]

    def place_entity_at(self, entity, x, y):
        self._cells[x][y].add_entity(entity)

    def remove_entity_from(self, entity, x, y):
        return self._cells[x][y].remove_entity(entity)