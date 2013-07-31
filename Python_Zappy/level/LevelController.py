__author__ = 'Travis Moy'

import warnings
import entity.actor.Adversary as Adversary
from z_defs import DIR

import level.commands.CompoundCmd as cmpd
from level.commands.command_fragments import *


class LevelController(object):
    def __init__(self, _level):
        """
        :type _level: level.Level.Level
        """
        self._level = _level
        self._zappy = self._level.player_actor
        """:type: entity.actor.Actor.Actor"""
        self.level_won = False
        self.level_failed = False

        self._destroyed_entities = list()  # Not currently used for anything!

    @property
    def level_completed(self):
        return self.level_won or self.level_failed

    #@property
    #def level(self):
    #    return self._level

    @property
    def level_view(self):
        return self._level.view

    @property
    def zappy(self):
        return self._zappy

    def get_eids_at(self, _x, _y):
        return self.level_view.get_eids_at(_x, _y)

    def get_zappy_x_y(self):
        return self._zappy._x, self._zappy._y

    def zappy_attempt_move(self, _direction):
        destination = DIR.get_coords_in_direction_from(_direction, *self.zappy.get_coords())
        if self.level_view.cell_is_passable(*destination):
            lvl_move = LevelMoveEntity(self.zappy.eid, self.level_view, *(self.get_zappy_x_y() + destination))
            use_moves = EntityUseMoves(self.zappy.eid, self._level.view, 1)
            command = cmpd.CompoundCmd("Zappy moves", lvl_move, use_moves)
            self._level.add_command(command)
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
        return [tool.eid for tool in self._zappy.get_tools()]

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
                        except AttributeError as e:
                            warnings.warn(e.message)
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
            self.level_won = True
            return

        print "Zappy HP:", self._zappy.current_hp

        # Check end conditions
        if self._zappy.is_destroyed():
            self.level_failed = True
            return

        # Player's turn
        self._zappy.turn_begin()