__author__ = 'Travis Moy'

import warnings
import entity.actor.Adversary as Adversary


class LevelController(object):
    def __init__(self, level):
        self._level = level
        self._zappy = self._level.get_player_actor()
        self._level_won = False
        self._level_failed = False

        self._destroyed_entities = list()

    def get_entities_at(self, _x, _y):
        return self._level.get_all_entities_at(_x, _y)

    def is_level_completed(self):
        return self._level_won or self._level_failed

    def is_level_won(self):
        return self._level_won

    def is_level_failed(self):
        return self._level_failed

    def get_level(self):
        return self._level

    def get_zappy(self):
        return self._zappy

    def get_zappy_x_y(self):
        return self._zappy._x, self._zappy._y

    def zappy_attempt_move(self, direction):
        self._zappy.attempt_move(direction)
        if not self._zappy.has_moves():
            self.turn_has_ended()

    def zappy_use_tool_on_location(self, _tool, _x, _y):
        _tool.use_on_location(_x, _y)
        if not self._zappy.has_moves():
            self.turn_has_ended()

    def zappy_use_tool_on_entity(self, _tool, _target):
        _tool.use_on_entity(_target)
        if not self._zappy.has_moves():
            self.turn_has_ended()

    def zappy_use_item(self):
        pass

    def zappy_get_tools(self):
        return self._zappy.get_tools()

    def turn_has_ended(self):
        self._zappy.turn_end()

        # Adversaries' turns
        for entity in self._level.get_all_entities():
            if entity is not self._zappy:
                try:
                    if entity.is_destroyed():
                        self._destroyed_entities.append(entity)
                        entity.destroy()
                    else:
                        entity.turn_begin()
                        try:
                            entity.take_action()
                        except AttributeError:
                            pass
                        entity.turn_end()

                        if entity.is_destroyed():
                            self._destroyed_entities.append(entity)
                            entity.destroy()
                except AttributeError:
                    pass

        warnings.warn("The code for winning simply checks if there are any adversaries left. Is placeholder.")
        no_adversaries = True
        for entity in self._level.get_all_entities():
            if isinstance(entity, Adversary.Adversary):
                no_adversaries = False
        if no_adversaries:
            self._level_won = True
            return

        print "Zappy HP:", self._zappy.get_current_hp()

        # Check end conditions
        if self._zappy.is_destroyed():
            self._level_failed = True
            return

        # Player's turn
        self._zappy.turn_begin()