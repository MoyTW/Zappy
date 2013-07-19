__author__ = 'Travis Moy'

import Behavior
import math
import level.commands.CompoundCmd as cmpd
from level.commands.command_fragments import EntityDealDamage


class BehaviorAttackMelee(Behavior.Behavior):
    def __init__(self, _move_cost=1, _strength=1):
        """
        :type _move_cost: int
        :type _strength: int
        """
        super(BehaviorAttackMelee, self).__init__(_move_cost)
        self.strength = _strength

    def _special_can_execute(self, _target_eid, _level_view, _user):
        """
        :type _target_eid: int
        :type _level_view: level.LevelView.LevelView
        :type _user: entity.actor.Adversary.Adversary
        :rtype: bool
        """
        #atz_x, atz_y = (_target_eid.get_coords()[i] - _user.get_coords()[i] for i in range(2))
        atz_x, atz_y = (_level_view.entity_coords(_target_eid)[i] - _user.get_coords()[i] for i in range(2))
        return math.sqrt(atz_x * atz_x + atz_y * atz_y) <= 1.0

    def _execute_effects(self, _target_eid, _level_view, _user):
        """
        :type _target_eid: int
        :type _level_view: level.LevelView.LevelView
        :type _user: entity.actor.Adversary.Adversary
        :rtype: bool
        """
        cmd_desc = "{0} melees {1} for {2} damage!".format(_user.entity_name, _level_view.entity_name(_target_eid),
                                                           self.strength)
        command = cmpd.CompoundCmd(cmd_desc, EntityDealDamage(_target_eid, _level_view, self.strength))
        _level_view.add_command(command)
        return True

