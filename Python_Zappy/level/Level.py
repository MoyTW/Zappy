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
        if other is None:
            return False
        elif isinstance(other, Level):
            if not self.get_level_info() == other.get_level_info():
                return False

            cell_equality = True

            # Brute force, mindless comparison.
            for w in range(0, self.get_width()):
                for h in range(0, self.get_height()):
                    if self._cells[w][h] != other._cells[w][h]:
                        cell_equality = False

            return cell_equality
        else:
            return self.__dict__ == other.__dict__

    def __repr__(self):
        return "({0}, {1}".format(self.get_level_info(), self._cells)