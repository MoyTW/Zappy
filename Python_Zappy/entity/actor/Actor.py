__author__ = 'Travis Moy'

import entity.Entity as Entity
from z_defs import DIR


class Actor(Entity.Entity):
    _priority = 3

    def __init__(self, level, max_hp=1, max_moves=1, x=-1, y=-1, tools=None, senses=None, image_name=None,
                 player_controlled=False):
        super(Actor, self).__init__(image_name=image_name, level=level)

        self._max_hp = max_hp
        self._current_hp = self._max_hp
        self._max_moves = max_moves
        self._current_moves = max_moves
        self._x = x
        self._y = y
        self._player_controlled = player_controlled

        if tools is None:
            self._tools = list()
        else:
            self._tools = tools
        if senses is None:
            self._senses = list()
        else:
            self._senses = senses

        # Set by self.detect_entities()
        self._detected_entities = list()

# Accessors
    def get_detected_entities(self):
        return self._detected_entities

    def get_coords(self):
        return self._x, self._y

    def get_max_hp(self):
        return self._max_hp

    def get_current_hp(self):
        return self._current_hp

    def get_current_moves(self):
        return self._current_moves

    def get_tools(self):
        return self._tools

    def is_player_controlled(self):
        return self._player_controlled

    def is_destroyed(self):
        return self._current_hp < 0

    def has_moves(self):
        return self._current_moves > 0

    def use_moves(self, moves):
        self._current_moves -= moves

    def deal_damage(self, damage):
        self._current_hp -= damage

    def set_coords(self, x, y):
        self._x = x
        self._y = y

    def replenish_moves(self):
        self._current_moves = self._max_moves

    # Not sure if I want to do it by coordinate, any more.
    # I think I want to do it by entity, instead.
    '''
    def use_tool_on(self, tool, coordinates):
        if tool in self._tools:
            return tool.use_on(coordinates)
        else:
            return False
    '''

    def detect_entities(self):
        self._detected_entities = list()
        for sense in self._senses:
            self._detected_entities.extend(sense.detect_entities(self._x, self._y, self._level))
        if self in self._detected_entities:
            self._detected_entities.remove(self)

    def attempt_move(self, direction):
        if self._current_moves <= 0:
            return False

        target_x, target_y = DIR.get_coords_in_direction_from(direction, self._x, self._y)

        if self._level.cell_is_passable(target_x, target_y):
            if self._level.move_entity_from_to(self, self._x, self._y, target_x, target_y):
                self._current_moves -= 1
                return True

        return False