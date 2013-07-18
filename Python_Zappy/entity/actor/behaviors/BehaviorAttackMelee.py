__author__ = 'Travis Moy'

import Behavior
import math


class BehaviorAttackMelee(Behavior.Behavior):

    def __init__(self, _move_cost=1, _strength=1):
        """
        :type _move_cost: int
        :type _strength: int
        """
        super(BehaviorAttackMelee, self).__init__(_move_cost)
        self._strength = _strength

    def _special_can_execute(self, _target_eid, _level_view, _user):
        """
        :type _target_eid: int
        :type _level_view: level.LevelView.LevelView
        :type _user: int
        :rtype: bool
        """
        atz_x, atz_y = (_target_eid.get_coords()[i] - _user.get_coords()[i] for i in range(2))
        return math.sqrt(atz_x * atz_x + atz_y * atz_y) <= 1.0

    def _execute_effects(self, _target_eid, _level_view, _user):
        """
        :type _target_eid: int
        :type _level_view: level.LevelView.LevelView
        :type _user: int
        :rtype: bool
        """
        _target_eid.deal_damage(self._strength)
        return True

