__author__ = 'Travis Moy'

import Behavior
import math


class BehaviorAttackMelee(Behavior.Behavior):

    def __init__(self, _strength=1):
        self._strength = _strength

    def _can_execute(self, level, adversary):
        if adversary.get_current_moves() > 0:
            adjacent = self._are_adjacent(level.get_player_actor(), adversary)
            return adjacent

    def _execute(self, level, adversary):
        player_actor = level.get_player_actor()
        player_actor.deal_damage(self._strength)
        adversary.use_moves(1)
        return True

    def _are_adjacent(self, zappy, adversary):
        atz_x, atz_y = (zappy.get_coords()[i] - adversary.get_coords()[i] for i in range(2))
        return math.sqrt(atz_x * atz_x + atz_y * atz_y) == 1.0