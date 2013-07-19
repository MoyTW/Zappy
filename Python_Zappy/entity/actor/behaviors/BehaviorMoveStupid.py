__author__ = 'Travis Moy'

import Behavior
from z_defs import DIR
import math

import level.commands.CompoundCmd as cmpd
from level.commands.command_fragments import LevelMoveEntity

# Attempts to move horizontally towards the player. If it cannot, attempts to move vertically towards the player.
# If it cannot, does nothing.
class BehaviorMoveStupid(Behavior.Behavior):

    # Tries to move horizontally; else tries to move vertically; else fails.
    def _execute_effects(self, _target_eid, _level_view, _user):
        """
        :type _target_eid: int
        :type _level_view: level.LevelView.LevelView
        :type _user: entity.actor.Adversary.Adversary
        :rtype: bool
        """
        zappy = _target_eid
        moved = False

        if zappy in _user._detected_entities:
            atz_x, atz_y = (_level_view.entity_coords(_target_eid)[i] - _user.get_coords()[i] for i in range(2))
            if math.sqrt(atz_x * atz_x + atz_y * atz_y) > 1:  # This prevents the adversary from moving ONTO Zappy.
                # Check for horizontal
                if atz_x < 0:
                    moved = self._try_to_move(DIR.W, _level_view, _user)
                elif atz_x > 0:
                    moved = self._try_to_move(DIR.E, _level_view, _user)

                # Check for vertical
                if not moved and atz_y < 0:  # We want to move down
                    moved = self._try_to_move(DIR.S, _level_view, _user)
                elif not moved and atz_y > 0:  # We want to move up
                    moved = self._try_to_move(DIR.N, _level_view, _user)

        return moved

    def _try_to_move(self, direction, level, adversary):
        """
        :type direction: int
        :type level: level.LevelView.LevelView
        :type adversary: entity.actor.Adversary.Adversary
        """
        adv_x, adv_y = adversary.get_coords()
        coords_to_next = DIR.get_coords_in_direction_from(direction, adv_x, adv_y)
        if level.cell_is_passable(*coords_to_next):
            cmd_desc = "{0} has moved without foresight to ({1}, {2})".format(level.entity_coords(adversary.eid),
                                                                              *coords_to_next)
            command = cmpd.CompoundCmd(cmd_desc, LevelMoveEntity(adversary.eid, level, adv_x, adv_y, *coords_to_next))
            level.add_command(command)
            return True
        else:
            return False