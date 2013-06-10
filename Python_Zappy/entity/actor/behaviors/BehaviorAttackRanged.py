__author__ = 'Travis Moy'

import Behavior
from z_algs import Z_ALGS


class BehaviorAttackRanged(Behavior.Behavior):

    def __init__(self, _strength, _range):
        self._strength = _strength
        self._range = _range

    def _can_execute(self, level, adversary):
        has_moves = adversary.get_current_moves() > 0
        zap_x, zap_y = level.get_player_actor().get_coords()
        adv_x, adv_y = adversary.get_coords()
        return has_moves and Z_ALGS.check_los(zap_x, zap_y,
                                              adv_x, adv_y,
                                              self._range + 1,
                                              level.cell_is_transparent)

    def _execute(self, level, adversary):
        zappy = level.get_player_actor()
        zappy.deal_damage(1)
        adversary.use_moves(1)
        print adversary, "used a ranged attack! Player has taken 1 damage! Player's hp:", zappy.get_current_hp()
        return True