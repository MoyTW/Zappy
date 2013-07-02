__author__ = 'Travis Moy'

import Behavior
from z_algs import Z_ALGS


class BehaviorAttackRanged(Behavior.Behavior):

    def __init__(self, _move_cost=1, _strength=1, _range=5):
        super(BehaviorAttackRanged, self).__init__(_move_cost)
        self._strength = _strength
        self._range = _range

    def _special_can_execute(self, _target, _level, _adversary):
        zap_x, zap_y = _target.get_coords()
        adv_x, adv_y = _adversary.get_coords()
        return Z_ALGS.check_los(zap_x, zap_y, adv_x, adv_y, self._range + 1, _level.cell_is_transparent)

    def _execute_effects(self, _target, _level, _adversary):
        _target.deal_damage(1)
        print _adversary.get_name(), "used a ranged attack on", _target.get_name(), "for", self._strength,\
            "damage! Target's hp:", _target.current_hp
        return True