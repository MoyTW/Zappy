__author__ = 'Travis Moy'

import Behavior
from z_algs import Z_ALGS


class BehaviorAttackRanged(Behavior.Behavior):

    def __init__(self, _move_cost=1, _strength=1, _range=5):
        super(BehaviorAttackRanged, self).__init__(_move_cost)
        self._strength = _strength
        self._range = _range

    def _special_can_execute(self, _target_eid, _level_view, _user):
        zap_x, zap_y = _target_eid.get_coords()
        adv_x, adv_y = _user.get_coords()
        return Z_ALGS.check_los(zap_x, zap_y, adv_x, adv_y, self._range + 1, _level_view.cell_is_transparent)

    def _execute_effects(self, _target_eid, _level_view, _user):
        _target_eid.deal_damage(1)
        print _user.entity_name, "used a ranged attack on", _target_eid.entity_name, "for", self._strength,\
            "damage! Target's hp:", _target_eid.current_hp
        return True