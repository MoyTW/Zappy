__author__ = 'Travis Moy'

import Behavior
from z_algs import Z_ALGS
import level.commands.CompoundCmd as cmpd
from level.commands.command_fragments import EntityDealDamage


class BehaviorAttackRanged(Behavior.Behavior):

    def __init__(self, _move_cost=1, _strength=1, _range=5):
        """
        :type _move_cost: int
        :type _strength: int
        :type _range: int
        """
        super(BehaviorAttackRanged, self).__init__(_move_cost)
        self.strength = _strength
        self.range = _range

    def _special_can_execute(self, _target_eid, _level_view, _user):
        """
        :type _target_eid: int
        :type _level_view: level.LevelView.LevelView
        :type _user: entity.actor.Adversary.Adversary
        :rtype: bool
        """
        zap_x, zap_y = _level_view.ent_coords(_target_eid)
        adv_x, adv_y = _user.get_coords()
        in_los = Z_ALGS.check_los(zap_x, zap_y, adv_x, adv_y, self.range + 1, _level_view.cell_is_transparent)
        in_rng = Z_ALGS.check_in_range(zap_x, zap_y, adv_x, adv_y, self.range)
        return in_los and in_rng

    def _execute_effects(self, _target_eid, _level_view, _user):
        """
        :type _target_eid: int
        :type _level_view: level.LevelView.LevelView
        :type _user: entity.actor.Adversary.Adversary
        :rtype: bool
        """
        cmd_desc = "{0} used a ranged attack on {1} for {2} damage!".format(_user.entity_name,
                                                                            _level_view.ent_name(_target_eid),
                                                                            self.strength)
        command = cmpd.CompoundCmd(cmd_desc, EntityDealDamage(_target_eid, _level_view, self.strength))
        _level_view.add_command(command)
        return True