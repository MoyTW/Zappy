__author__ = 'Travis Moy'

import entity.Entity as Entity
from z_defs import DIR


class Actor(Entity.Entity):

    def __init__(self, max_moves, level, x=0, y=0, tools=None, image_name=None):
        super(Actor, self).__init__(image_name=image_name, level=level)

        self._max_moves = max_moves
        self._current_moves = max_moves
        self._x = x
        self._y = y

        self._tools = tools

    def set_coords(self, x, y):
        self._x = x
        self._y = y

    def get_tools(self):
        return self._tools

    # Not sure if I want to do it by coordinate, any more.
    # I think I want to do it by entity, instead.
    '''
    def use_tool_on(self, tool, coordinates):
        if tool in self._tools:
            return tool.use_on(coordinates)
        else:
            return False
    '''

    def attempt_move(self, direction):
        if self._current_moves <= 0:
            return False

        target_x, target_y = DIR.get_coords_in_direction_from(direction, self._x, self._y)

        if self._level.cell_is_passable(target_x, target_y):
            if self._level.move_entity_from_to(self, self._x, self._y, target_x, target_y):
                self._current_moves -= 1
                return True

        return False