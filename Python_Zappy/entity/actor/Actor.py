__author__ = 'Travis Moy'

import entity.Entity as Entity
from z_defs import DIR, RANK
import warnings


class Actor(Entity.Entity):
    _priority = 3

    def __init__(self, _level, _entity_name='Default Actor Name', max_hp=1, max_moves=1, max_energy=100, energy_regen=10,
                 tools=None, senses=None, _image_name=None, rank=RANK.AVERAGE, player_controlled=False):
        super(Actor, self).__init__(_entity_name=_entity_name, _image_name=_image_name, _level=_level)
        warnings.warn("Actor cannot yet apply status effects. turn_begin() and turn_end are passing.")

        self._max_hp = max_hp
        self._current_hp = self._max_hp
        self._max_moves = max_moves
        self._current_moves = max_moves
        self._max_energy = max_energy
        self._current_energy = max_energy
        self._energy_regen = energy_regen
        self._rank = rank
        self._player_controlled = player_controlled

        if tools is None:
            self._tools = list()
        else:
            self._tools = tools
        if senses is None:
            self._senses = list()
        else:
            self._senses = senses

        # Entities will always spawn "clean" - can be changed in the future but I don't see the need to do so...
        # Maybe I'll change my mind.
        self._stunned = False
        self._status_effects = list()

        # Set by self.detect_entities()
        self._detected_entities = list()

# Accessors
    def is_stunned(self):
        return self._stunned

    def unstun(self):
        self._stunned = False

    def stun(self):
        self._stunned = True

    def use_energy(self, amount):
        self._current_energy -= amount
        if self._current_energy < 0:
            warnings.warn("An Actor has overspent their energy! (Actor._current_energy < 0). This should not happen!")

    def get_current_energy(self):
        return self._current_energy

    def get_max_energy(self):
        return self._max_energy

    def get_status_effects(self):
        return self._status_effects

    def get_rank(self):
        return self._rank

    def get_detected_entities(self):
        return self._detected_entities

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
        return self._current_hp <= 0

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

    # At the begnning of the turn:
    #   Replenish the movement points
    #   Apply each status effect, in turn (this done because if you are, for example, deafened, but you somehow acquire
    # a new hearing sense within the turn, you will be made unable to use it, as is proper)
    def turn_begin(self):
        self._current_moves = self._max_moves
        self._current_energy += self._energy_regen
        if self._current_energy > self._max_energy:
            self._current_energy = self._max_energy
        for status_effect in self._status_effects:
            status_effect.apply()

    # At the end of the turn:
    #   Lower all CD timers (Tools and Status Effects)
    #   Check for expired status effects; umapply and remove expired
    def turn_end(self):
        for tool in self._tools:
            tool.turn_passed()
        for status_effect in self._status_effects:
            status_effect.turn_passed()
            if status_effect.has_expired():
                status_effect.unapply()
                self.remove_status_effect(status_effect)

    # Note that status effects don't take effect until the beginning of the Actor's turn.
    #   I suppose that you could theoretically blind yourself and then still use your sight, but...that's kind of silly
    # and really, why would you blind yourself? I don't see the need to prevent that.
    def apply_status_effect(self, effect):
        self._status_effects.append(effect)

    # Unapplies and removes the status effect.
    def remove_status_effect(self, effect):
        self._status_effects.remove(effect)

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