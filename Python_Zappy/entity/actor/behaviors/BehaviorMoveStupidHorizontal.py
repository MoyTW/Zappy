__author__ = 'Travis Moy'

import Behavior
from z_defs import DIR
import math


class BehaviorMoveStupidHorizontal(Behavior.Behavior):

    def _execute_effects(self, _target_eid, _level_view, _user_eid):
        zappy = _target_eid
        moved = False
        if zappy in _user_eid._detected_entities:
            atz_x, atz_y = (zappy.get_coords()[i] - _user_eid.get_coords()[i] for i in range(2))
            if math.sqrt(atz_x * atz_x + atz_y * atz_y) > 1:  # This prevents the adversary from moving ONTO Zappy.
                # Check for horizontal
                if atz_x < 0:
                    moved = self._try_to_move(DIR.W, _level_view, _user_eid)
                elif atz_x > 0:
                    moved = self._try_to_move(DIR.E, _level_view, _user_eid)

        return moved

    def _try_to_move(self, direction, level, adversary):
        adv_x, adv_y = adversary.get_coords()
        coords_to_next = DIR.get_coords_in_direction_from(direction, adv_x, adv_y)
        if level.cell_is_passable(*coords_to_next):
            return level.move_entity_from_to(adversary, adv_x, adv_y, *coords_to_next)
        else:
            return False