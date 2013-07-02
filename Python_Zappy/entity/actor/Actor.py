__author__ = 'Travis Moy'

from entity.actor.Faction import FACTIONS
import entity.Entity as Entity
from z_defs import DIR, RANK
import warnings
import entity.Destructible as Destructible


class Actor(Entity.Entity, Destructible.Destructible):
    PRIORITY = 3

    def __init__(self, _level, _entity_name='Default Actor Name', _max_hp=1, _max_moves=1, _max_energy=100,
                 _energy_regen=10, _tools=None, _senses=None, _image_name=None, _rank=RANK.AVERAGE,
                 _faction=FACTIONS.DEFAULT, _base_threat=1, **kwargs):
        super(Actor, self).__init__(_entity_name=_entity_name, _image_name=_image_name, _max_hp=_max_hp,
                                    _level=_level, **kwargs)

        self._max_moves = _max_moves
        self._current_moves = _max_moves
        self._max_energy = _max_energy
        self._current_energy = _max_energy
        self._energy_regen = _energy_regen
        self._rank = _rank
        self._faction = _faction
        self._base_threat = _base_threat

        if _tools is None:
            self._tools = list()
        else:
            self._tools = _tools
        if _senses is None:
            self._senses = list()
        else:
            self._senses = _senses

        # Entities will always spawn "clean" - can be changed in the future but I don't see the need to do so...
        # Maybe I'll change my mind.
        self._stunned = False
        self._status_effects = list()

        # Set by self.detect_entities()
        self._detected_entities = list()

# Accessors
    def get_senses(self):
        return self._senses

    def get_threat(self):
        return self._base_threat

    def get_faction(self):
        return self._faction

    def get_faction_name(self):
        return self._faction.get_faction_name()

    def is_stunned(self):
        return self._stunned

    def unstun(self):
        self._stunned = False

    def stun(self):
        self._stunned = True

    def use_energy(self, _amount):
        self._current_energy -= _amount
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

    def get_current_moves(self):
        return self._current_moves

    def get_tools(self):
        return self._tools

    def is_player_controlled(self):
        return self._faction == FACTIONS.PLAYER

    def has_moves(self):
        return self._current_moves > 0

    def use_moves(self, _moves):
        self._current_moves -= _moves

    def replenish_moves(self):
        self._current_moves = self._max_moves

    def init_tool_list(self, _tool_list):
        self._tools = _tool_list

    def add_tool(self, _tool):
        _tool.set_user(self)
        self._level.remove_entity_from(_tool, *_tool.get_coords())
        self._tools.append(_tool)

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
    def apply_status_effect(self, _effect):
        self._status_effects.append(_effect)

    # Unapplies and removes the status effect.
    def remove_status_effect(self, _effect):
        self._status_effects.remove(_effect)

    def detect_entities(self):
        self._detected_entities = list()
        for sense in self._senses:
            self._detected_entities.extend(sense.detect_entities(self._x, self._y, self._level))
        if self in self._detected_entities:
            self._detected_entities.remove(self)

    def attempt_move(self, _direction):
        if self._current_moves <= 0:
            return False

        target_x, target_y = DIR.get_coords_in_direction_from(_direction, self._x, self._y)

        if self._level.cell_is_passable(target_x, target_y):
            if self._level.move_entity_from_to(self, self._x, self._y, target_x, target_y):
                self._current_moves -= 1
                return True

        return False