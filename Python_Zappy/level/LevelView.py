__author__ = 'Travis Moy'

import warnings


class LevelView(object):
    def __init__(self, lvl):
        """
        :type lvl: level.Level.Level
        """
        self.lvl = lvl

    @property
    def player_actor(self):
        return self.lvl.player_actor

    def get_entity_name(self, eid):
        warnings.warn("OH GOD THIS CODE IN LEVELVIEW.GET_ENTITY_NAME OH GOD NO")
        entities = self._get_all_entities()
        for e in entities:
            if e.eid == eid:
                return e.entity_name
        return None

    def add_command(self, cmd):
        """
        :type cmd: level.commands.Command.Command
        """
        self.lvl.add_command(cmd)

    def get_display_images_at(self, x, y, _in_fow=False):
        """
        :type x: int
        :type y: int
        :type _in_fow: bool
        :rtype: dict
        """
        if self.lvl.are_valid_coords(x, y):
            return self.lvl._cells[x][y].get_display_images(_in_fow)
        return None

    def get_cell_at(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: level.Cell.Cell
        """
        if self.lvl.are_valid_coords(x, y):
            return self.lvl._cells[x][y]
        return None

    def cell_is_passable(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: bool
        """
        if self.lvl.are_valid_coords(x, y):
            return self.lvl._cells[x][y].is_passable
        return False

    def cell_is_transparent(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: bool
        """
        if self.lvl.are_valid_coords(x, y):
            return self.lvl._cells[x][y].is_transparent
        return False

    # Horrifying, really. A more efficient (but more work-intensive) way would be to maintain an internal list, and to
    # update it each time an entity is placed or removed.
    #
    # However, until it becomes a problem performance-wise, just leave it at this.
    def get_all_eids(self):
        """
        :rtype: list
        """
        entities = list()
        for x in range(self.lvl.level_width):
            for y in range(self.lvl.level_height):
                entities.extend(self.get_eids_at(x, y))
        return entities

    def get_eids_at(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: list
        """
        if self.lvl.are_valid_coords(x, y):
            return [e.eid for e in self.lvl._cells[x][y].get_all_entities()]
        return None

        # Dumb search
    def find_coordinates_of_entity(self, entity):
        """
        :type entity: entity.Entity.Entity
        :rtype: tuple
        """
        for x in range(self.lvl.level_width):
            for y in range(self.lvl.level_height):
                if self.lvl._cells[x][y].contains_entity(entity):
                    return x, y
        return None

    def _get_all_entities(self):
        """
        :rtype: list
        """
        entities = list()
        for x in range(self.lvl.level_width):
            for y in range(self.lvl.level_height):
                entities.extend(self.lvl._cells[x][y].get_all_entities())
        return entities