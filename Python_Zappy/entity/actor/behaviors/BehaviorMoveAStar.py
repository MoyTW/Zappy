__author__ = 'Travis Moy'

import Behavior
from z_algs import Z_ALGS


class BehaviorMoveAStar(Behavior.Behavior):

    def _execute_effects(self, _target, _level, _user):
        path = Z_ALGS.a_star_from_to(origin=_user.get_coords(), destination=_target.get_coords(), level=_level)
        if len(path) > 0:
            adv_x, adv_y = _user.get_coords()
            tar_x, tar_y = path[0]
            _level.move_entity_from_to(_user, adv_x, adv_y, tar_x, tar_y)
            return True
        else:
            return False