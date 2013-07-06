__author__ = 'Travis Moy'

import level.levelExceptions
import warnings
import entity.actor.Adversary as Adversary


class Level:
    # cells is a rectangular grid of Cell objects.
    def __init__(self, info, cells=None, player_actor=None):
        self._info = info
        self._cells = cells
        self._player_actor = player_actor

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
        print "player_actor.setter called!"
        if self._player_actor is None:
            print "assigning!"
            self._player_actor = value
        else:
            warnings.warn("There are multiple candidates for the player actor on this map!")

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

    def get_cell_at(self, x, y):
        if self._check_coordinates(x, y):
            return self._cells[x][y]
        return None

    def get_all_entities_at(self, x, y):
        if self._check_coordinates(x, y):
            entities = self._cells[x][y].get_all_entities()
            return entities
        return None

    # Horrifying, really. A more efficient (but more work-intensive) way would be to maintain an internal list, and to
    # update it each time an entity is placed or removed.
    #
    # However, until it becomes a problem performance-wise, just leave it at this.
    def get_all_entities(self):
        entities = list()
        for x in range(self.level_width):
            for y in range(self.level_height):
                entities.extend(self.get_all_entities_at(x, y))
        for entity in entities:
            if isinstance(entity, Adversary.Adversary):
                print entity
        return entities

    def cell_is_passable(self, x, y):
        cell = self.get_cell_at(x, y)
        if cell is not None:
            return cell.is_passable
        return False

    def cell_is_transparent(self, x, y):
        cell = self.get_cell_at(x, y)
        if cell is not None:
            return cell.is_transparent
        return False

    def get_display_images_at(self, x, y, _in_fow=False):
        if self._check_coordinates(x, y):
            return self._cells[x][y].get_display_images(_in_fow)
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
            if self._cells[x][y].remove_entity(entity):
                try:
                    entity.set_coords(-1, -1)
                except AttributeError:
                    pass
                return True
        return False

    def move_entity_from_to(self, entity, old_x, old_y, new_x, new_y):
        if not self.remove_entity_from(entity, old_x, old_y):
            print "Could not remove", entity.entity_name, "from", old_x, old_y
            return False
        self.place_entity_at(entity, new_x, new_y)
        print "Removed",  entity.entity_name, "from", old_x, old_y, "and placed at", new_x, new_y
        return True

    # Dumb search
    def find_coordinates_of_entity(self, entity):
        for x in range(self.level_width):
            for y in range(self.level_height):
                cell = self.get_cell_at(x, y)
                if cell.contains_entity(entity):
                    return [x, y]
        return None

    def _check_coordinates(self, x, y):
        if 0 <= x < self.level_width and 0 <= y < self.level_height:
                return True
        return False

    def __eq__(self, other):
        return sorted(self.__dict__) == sorted(other.__dict__)

    def __repr__(self):
        return "({0}, {1}".format(self._info, self._cells)