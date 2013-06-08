__author__ = 'Travis Moy'

import Behavior
from z_defs import DIR


# Attempts to move horizontally towards the player. If it cannot, attempts to move vertically towards the player.
# If it cannot, does nothing.
class BehaviorMoveStupid(Behavior.Behavior):

    # Executes if you have a move
    def _can_execute(self, level, adversary):
        if adversary.get_current_moves() > 0:
            return True
        else:
            return False

    # Tries to move horizontally; else tries to move vertically; else fails.
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

            # Check for vertical
            if not moved and atz_y < 0:  # We want to move down
                moved = self._try_to_move(DIR.S, level, adversary)
            elif not moved and atz_y > 0:  # We want to move up
                moved = self._try_to_move(DIR.N, level, adversary)

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