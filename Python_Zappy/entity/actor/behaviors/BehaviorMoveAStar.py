__author__ = 'Travis Moy'

import Behavior
from z_algs import Z_ALGS
import level.commands.CompoundCmd as cmpd
from level.commands.command_fragments import LevelMoveEntity


class BehaviorMoveAStar(Behavior.Behavior):

    def _execute_effects(self, _target_eid, _level_view, _user):
        """
        :type _target_eid: int
        :type _level_view: level.LevelView.LevelView
        :type _user: entity.actor.Adversary.Adversary
        :rtype: bool
        """
        path = Z_ALGS.a_star_from_to(origin=_user.get_coords(),
                                     destination=_level_view.get_entity_coords(_target_eid),
                                     level=_level_view)
        if len(path) > 0:
            adv_x, adv_y = _user.get_coords()
            tar_x, tar_y = path[0]

            cmd_desc = "Using A*, {0} has moved to ({1}, {2})!".format(_level_view.get_entity_name(_target_eid),
                                                                       tar_x, tar_y)
            command = cmpd.CompoundCmd(cmd_desc, LevelMoveEntity(_target_eid, _level_view, adv_x, adv_y, tar_x, tar_y))
            _level_view.add_command(command)

            return True
        else:
            return False