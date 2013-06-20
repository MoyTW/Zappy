__author__ = 'Travis Moy'

import Behavior
import math


class BehaviorAttackMelee(Behavior.Behavior):

    def __init__(self, _move_cost=1, _strength=1):
        super(BehaviorAttackMelee, self).__init__(_move_cost)
        self._strength = _strength

    def _special_can_execute(self, _target, _level, _adversary):
        return self._are_adjacent(_target, _adversary)

    def _execute_effects(self, _target, _level, _adversary):
        _target.deal_damage(self._strength)
        return True

    def _are_adjacent(self, zappy, adversary):
        atz_x, atz_y = (zappy.get_coords()[i] - adversary.get_coords()[i] for i in range(2))
        return math.sqrt(atz_x * atz_x + atz_y * atz_y) == 1.0