__author__ = 'Travis Moy'

import entity.Entity as Entity


class Actor(Entity.Entity):

    def __init__(self, max_moves, level, tools=None, image_name=None):
        super(Actor, self).__init__(image_name=image_name, level=level)

        self._max_moves = max_moves
        self._current_moves = max_moves

        self._tools = tools

    def get_tools(self):
        return self._tools

    def use_tool_on(self, tool, coordinates):
        if tool in self._tools:
            return tool.use_on(coordinates)
        else:
            return False

    def attempt_move(self, direction):
        pass