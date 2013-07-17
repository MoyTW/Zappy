__author__ = 'Travis Moy'

import Behavior
from z_algs import Z_ALGS


class BehaviorMoveAStar(Behavior.Behavior):

    def _execute_effects(self, _target_eid, _level_view, _user_eid):
        path = Z_ALGS.a_star_from_to(origin=_user_eid.get_coords(), destination=_target_eid.get_coords(), level=_level_view)
        if len(path) > 0:
            adv_x, adv_y = _user_eid.get_coords()
            tar_x, tar_y = path[0]
            _level_view.move_entity_from_to(_user_eid, adv_x, adv_y, tar_x, tar_y)
            return True
        else:
            return False