__author__ = 'Travis Moy'

import Behavior
from z_defs import DIR


class BehaviorMoveStupidHorizontal(Behavior.Behavior):

    def _can_execute(self, level, adversary):
        if adversary.get_current_moves() > 0:
            return True
        else:
            return False

    def _execute(self, level, adversary):
        zappy = level.get_player_actor()
        if zappy in adversary.get_detected_entities():
            moved = False
            atz_x, atz_y = (zappy.get_coords()[i] - adversary.get_coords()[i] for i in range(2))

            # Check for horizontal
            if atz_x < 0:
                moved = self._try_to_move(DIR.W, level, adversary)
            elif atz_x > 0:
                moved = self._try_to_move(DIR.E, level, adversary)

            if moved:
                adversary.use_moves(1)
            return moved
        else:
            return False

    def _try_to_move(self, direction, level, adversary):
        adv_x, adv_y = adversary.get_coords()
        coords_to_next = DIR.get_coords_in_direction_from(direction, adv_x, adv_y)
        if level.cell_is_passable(*coords_to_next):
            return level.move_entity_from_to(adversary, adv_x, adv_y, *coords_to_next)
        else:
            return False