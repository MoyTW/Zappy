__author__ = 'Travis Moy'

import level.levelExceptions
import collections


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
            raise level.levelExceptions.LevelCellsAlreadySetError("Cannot assign cells to level {0} (#{1}) - it "
                                                                  "already has cells assigned to it!"
                                                                  .format(self._info.get_name(),
                                                                          self._info.get_number()))

    def get_level_info(self):
        return self._info

    def get_name(self):
        return self._info.get_name()

    def get_number(self):
        return self._info.get_number()

    def get_width(self):
        return self._info.get_width()

    def get_height(self):
        return self._info.get_height()

    def get_cell_at(self, x, y):
        try:
            return self._cells[x][y]
        except IndexError:
            return None

    def place_entity_at(self, entity, x, y):
        self._cells[x][y].add_entity(entity)

    def remove_entity_from(self, entity, x, y):
        return self._cells[x][y].remove_entity(entity)

    def __eq__(self, other):
        print "LEVEL __EQ__ CALLED!"
        if other is None:
            return False
        elif isinstance(other, Level):
            info_equality = self.get_level_info() == other.get_level_info()
            cell_equality = collections.Counter(self._cells) == collections.Counter(other._cells)
            #cell_equality = cmp(self._cells, other._cells) == 0
            print "IE: {0} CE: {1}".format(info_equality, cell_equality)
            return info_equality and cell_equality
        else:
            print "OTHER WAS NOT LEVEL AND NOT NONE"
            return self.__dict__ == other.__dict__

    def __repr__(self):
        return "({0}, {1}".format(self.get_level_info(), self._cells)