__author__ = 'Travis Moy'

import warnings


class LevelController(object):
    def __init__(self, level):
        self._level = level
        self._zappy = self._level.get_player_actor()
        warnings.warn('LevelController is not yet fully implemented! zappy_get_tools are passing.')

    def get_level(self):
        return self._level

    def get_zappy(self):
        return self._zappy

    def get_zappy_x_y(self):
        return self._zappy._x, self._zappy._y

    def zappy_attempt_move(self, direction):
        self._zappy.attempt_move(direction)
        if not self._zappy.has_moves():
            self._turn_has_ended()
        return self

    def zappy_use_item(self):
        pass

    def zappy_get_tools(self):
        pass

    def _turn_has_ended(self):
        for entity in self._level.get_all_entities():
            if entity is not self._zappy:
                try:
                    entity.replenish_moves()
                    entity.take_action()
                except AttributeError:
                    pass
        warnings.warn("_turn_has_ended only replenishes Zappy's move points at this time!")
        self._zappy.replenish_moves()