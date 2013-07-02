__author__ = 'Travis Moy'

import Behavior
from z_defs import DIR
import math


# Attempts to move horizontally towards the player. If it cannot, attempts to move vertically towards the player.
# If it cannot, does nothing.
class BehaviorMoveStupid(Behavior.Behavior):

    # Tries to move horizontally; else tries to move vertically; else fails.
    def _execute_effects(self, _target, _level, _adversary):
        zappy = _target
        moved = False

        if zappy in _adversary._detected_entities:
            atz_x, atz_y = (zappy.get_coords()[i] - _adversary.get_coords()[i] for i in range(2))
            if math.sqrt(atz_x * atz_x + atz_y * atz_y) > 1:  # This prevents the adversary from moving ONTO Zappy.
                # Check for horizontal
                if atz_x < 0:
                    moved = self._try_to_move(DIR.W, _level, _adversary)
                elif atz_x > 0:
                    moved = self._try_to_move(DIR.E, _level, _adversary)

                # Check for vertical
                if not moved and atz_y < 0:  # We want to move down
                    moved = self._try_to_move(DIR.S, _level, _adversary)
                elif not moved and atz_y > 0:  # We want to move up
                    moved = self._try_to_move(DIR.N, _level, _adversary)

        return moved

    def _try_to_move(self, direction, level, adversary):
        adv_x, adv_y = adversary.get_coords()
        coords_to_next = DIR.get_coords_in_direction_from(direction, adv_x, adv_y)
        if level.cell_is_passable(*coords_to_next):
            return level.move_entity_from_to(adversary, adv_x, adv_y, *coords_to_next)
        else:
            return False