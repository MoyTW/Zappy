__author__ = 'Travis Moy'

import level.levelExceptions
import warnings
import level.Record as Record
import level.LevelView as LevelView


class Level(object):
    # cells is a rectangular grid of Cell objects.
    def __init__(self, info, cells=None, player_actor=None):
        self._info = info
        self._cells = cells
        self._player_actor = player_actor
        self.max_eid = 0
        self.record = Record.Record()
        self.view = LevelView.LevelView(self)

    def get_level_info(self):
        return self._info

    @property
    def level_name(self):
        return self._info.info_name

    @property
    def level_number(self):
        return self._info.info_number

    @property
    def level_width(self):
        return self._info.info_width

    @property
    def level_height(self):
        return self._info.info_height

    @property
    def level_preview_image(self):
        return self._info.info_preview_image

    @property
    def player_actor(self):
        return self._player_actor

    @player_actor.setter
    def player_actor(self, value):
        if self._player_actor is None:
            self._player_actor = value
        else:
            warnings.warn("There are multiple candidates for the player actor on this map!")

    def add_entry(self, entry):
        self.record.add_entry(entry)

    def cells_are_none(self):
        if self._cells is None:
            return True
        return False

    # Should throw some manner of exception if cells is not None
    def set_cells(self, cells):
        if self._cells is None:
            if len(cells) != self.level_width:
                raise level.levelExceptions.LevelWidthNotMatchedByCells("len(cells)={0} != self._width={1}"
                                                                        .format(len(cells), self.level_width))
            elif len(cells[0]) != self.level_height:
                raise level.levelExceptions.LevelHeightNotMatchedByCells("len(cells[0])={0} != self._width={1}"
                                                                         .format(len(cells), self.level_width))
            self._cells = cells
        else:
            raise level.levelExceptions.LevelCellsAlreadySetError("Cannot assign cells to level {0} (#{1}) - it "
                                                                  "already has cells assigned to it!"
                                                                  .format(self.level_name,
                                                                          self.level_number))

    # Also replaces the player_actor
    def replace_cells(self, cells):
        self._player_actor = None
        self._cells = None
        self.set_cells(cells)

    # If the entity has the function "set_coords" defined, this will attempt to call it.
    def place_entity_at(self, entity, x, y):
        if self.are_valid_coords(x, y):
            self._cells[x][y].add_entity(entity)
        try:
            entity.set_coords(x, y)
        except AttributeError:
            pass

    def remove_entity_from(self, entity, x, y):
        if self.are_valid_coords(x, y):
            if self._cells[x][y].remove_entity(entity):
                try:
                    entity.set_coords(-1, -1)
                except AttributeError:
                    pass
                return True
        return False

    def move_entity_from_to(self, entity, old_x, old_y, new_x, new_y):
        if not self.remove_entity_from(entity, old_x, old_y):
            return False
        self.place_entity_at(entity, new_x, new_y)
        return True

    def are_valid_coords(self, x, y):
        if 0 <= x < self.level_width and 0 <= y < self.level_height:
                return True
        return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __eq__(self, other):
        """
        :type other: Level
        :rtype: bool
        """
        try:
            if self._info == other._info and self._cells is None and other._cells is None:
                return True
        except AttributeError:
            return False

        try:
            for x in range(self.level_width):
                for y in range(self.level_height):
                    if not self._cells[x][y] == other._cells[x][y]:
                        return False

            return self._info == other._info and self._player_actor == other._player_actor
        except (TypeError, IndexError, AttributeError):
            return False

    def __repr__(self):
        return "({0}, {1})".format(self._info, self._cells)