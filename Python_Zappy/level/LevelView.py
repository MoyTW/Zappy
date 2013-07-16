__author__ = 'Travis Moy'

#import level.Level as Level


class LevelView(object):
    def __init__(self, lvl):
        """
        :type lvl: level.Level.Level
        """
        self.lvl = lvl

    @property
    def player_actor(self):
        return self.lvl.player_actor

    def get_display_images_at(self, x, y, _in_fow=False):
        if self.lvl.are_valid_coords(x, y):
            return self.lvl._cells[x][y].get_display_images(_in_fow)
        return None

    def get_cell_at(self, x, y):
        if self.lvl.are_valid_coords(x, y):
            return self.lvl._cells[x][y]
        return None

    def cell_is_passable(self, x, y):
        if self.lvl.are_valid_coords(x, y):
            return self.lvl._cells[x][y].is_passable
        return False

    def cell_is_transparent(self, x, y):
        if self.lvl.are_valid_coords(x, y):
            return self.lvl._cells[x][y].is_transparent
        return False

    # Horrifying, really. A more efficient (but more work-intensive) way would be to maintain an internal list, and to
    # update it each time an entity is placed or removed.
    #
    # However, until it becomes a problem performance-wise, just leave it at this.
    def get_all_entities(self):
        entities = list()
        for x in range(self.lvl.level_width):
            for y in range(self.lvl.level_height):
                entities.extend(self.get_all_entities_at(x, y))
        return entities

    def get_all_entities_at(self, x, y):
        if self.lvl.are_valid_coords(x, y):
            return self.lvl._cells[x][y].get_all_entities()
        return None

        # Dumb search
    def find_coordinates_of_entity(self, entity):
        for x in range(self.lvl.level_width):
            for y in range(self.lvl.level_height):
                if self.lvl._cells[x][y].contains_entity(entity):
                    return [x, y]
        return None