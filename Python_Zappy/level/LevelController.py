__author__ = 'Travis Moy'

import warnings


class LevelController(object):
    def __init__(self, level):
        self._level = level
        warnings.warn('LevelController is not yet fully implemented! zappy_attempt_move, zappy_use_item, and '
                      'zappy_get_tools are passing.')

    def get_level(self):
        return self._level

    def get_zappy(self):
        return self._level.get_player_actor()

    def zappy_attempt_move(self, order):
        pass

    def zappy_use_item(self):
        pass

    def zappy_get_tools(self):
        pass