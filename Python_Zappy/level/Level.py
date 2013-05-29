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
            if len(cells) != self.get_width():
                raise level.levelExceptions.LevelWidthNotMatchedByCells("len(cells)={0} != self._width={1}"
                                                                        .format(len(cells), self.get_width()))
            elif len(cells[0]) != self.get_height():
                raise level.levelExceptions.LevelHeightNotMatchedByCells("len(cells[0])={0} != self._width={1}"
                                                                         .format(len(cells), self.get_width()))
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

    def get_preview(self):
        return self._info.get_preview()

    def get_cell_at(self, x, y):
        if self._check_coordinates(x, y):
            return self._cells[x][y]
        return None

    def cell_is_passable(self, x, y):
        cell = self.get_cell_at(x, y)
        if cell is not None:
            return cell.get_passable()
        return False

    def get_display_images_at(self, x, y):
        if self._check_coordinates(x, y):
            return self._cells[x][y].get_display_images()
        return None

    # If the entity has the function "set_coords" defined, this will attempt to call it.
    def place_entity_at(self, entity, x, y):
        if self._check_coordinates(x, y):
            self._cells[x][y].add_entity(entity)
        try:
            entity.set_coords(x, y)
        except AttributeError:
            pass

    def remove_entity_from(self, entity, x, y):
        if self._check_coordinates(x, y):
            return self._cells[x][y].remove_entity(entity)
        return False

    def move_entity_from_to(self, entity, old_x, old_y, new_x, new_y):
        if not self.remove_entity_from(entity, old_x, old_y):
            return False
        self.place_entity_at(entity, new_x, new_y)
        return True

    # Dumb search
    def find_coordinates_of_entity(self, entity):
        for x in range(self.get_width()):
            for y in range(self.get_height()):
                cell = self.get_cell_at(x, y)
                if cell.contains_entity(entity):
                    return [x, y]
        return None

    def _check_coordinates(self, x, y):
        if 0 <= x < self.get_width() and 0 <= y < self.get_height():
                return True
        return False

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