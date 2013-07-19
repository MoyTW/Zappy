__author__ = 'Travis Moy'

import Tool
import entity.actor.effects.EffectEnrage as EffectEnrage
import entity.actor.effects.EffectBlind as EffectBlind
from z_defs import RANK
import warnings

import level.commands.CompoundCmd as cmpd
from level.commands.command_fragments import EntityDealDamage
from level.commands.command_fragments import ActorApplyStatusEffect


'''
    Can trigger collapses, break open pits, etc, etc, from a longer range than the Waldos and with greater force. Can
also do thinks like kill weak enemies, blind average ones, and irritate powerful and terrifying ones.

How to manage?
    - If enemy, check strength (I need to add this in). Then, apply status effect.
    - Instead of "triggering" Environmentals, it "attacks" them.
'''


class ToolSamplingLaser(Tool.Tool):

    def __init__(self, _eid, _level, _damage=5, _blind_duration=14, _enrage_duration=7, **kwargs):
        """
        :type _eid: int
        :type _level: level.LevelView.LevelView
        :type _damage: int
        """
        self._damage = _damage
        self._blind_duration = _blind_duration
        self._enrage_duration = _enrage_duration
        kwargs['_list_target_types'] = [self.TYPE_ENTITY]
        kwargs['_requires_LOS'] = True
        super(ToolSamplingLaser, self).__init__(_eid=_eid, _level=_level, **kwargs)

    def _effects_of_use_on_entity(self, _target_eid):
        """
        :type _target_eid: int
        :rtype: bool
        """
        done = self._use_on_actor(_target_eid)
        if not done:
            done = self._use_on_env(_target_eid)
        return done

    # Returns True on completion, False on failure
    #
    # If RANK == WEAK, kill
    # If RANK == AVERAGE, blind
    # If RANK == POWERFUL or RANK == TERRIFYING, enrage
    def _use_on_actor(self, _target):
        """
        :type _target: int
        :rtype: bool
        """
        try:
            rank = self._level.act_rank(_target)
            if rank == RANK.WEAK:
                #_target.deal_damage(_target.current_hp)
                cmd_desc = "{0} blasts the {1}, dealing lethal damage to the weak " \
                           "foe!".format(self.entity_name, self._level.ent_name(_target))
                command = cmpd.CompoundCmd(cmd_desc,
                                           EntityDealDamage(_target, self._level,
                                                            self._level.des_curr_hp(_target)))
            elif rank == RANK.AVERAGE:
                #_target.apply_status_effect(EffectBlind.EffectBlind(self._blind_duration, _target))
                cmd_desc = "{0} blasts the {1}, in the eyes, blinding it for {1} " \
                           "rounds!".format(self.entity_name, self._level.ent_name(_target), self._blind_duration)
                command = cmpd.CompoundCmd(cmd_desc,
                                           ActorApplyStatusEffect(eid=_target,
                                                                  lvl_view=self._level,
                                                                  effect=EffectBlind.EffectBlind,
                                                                  duration=self._blind_duration))
            elif rank == RANK.POWERFUL or rank == RANK.TERRIFYING:
                #_target.apply_status_effect(EffectEnrage.EffectEnrage(self._enrage_duration, _target, self.user))
                cmd_desc = "{0} blasts the {1}, but it does nothing but make it" \
                           "angry!".format(self.entity_name, self._level.ent_name(_target), self._blind_duration)
                command = cmpd.CompoundCmd(cmd_desc,
                                           ActorApplyStatusEffect(eid=_target,
                                                                  lvl_view=self._level,
                                                                  effect=EffectEnrage.EffectEnrage,
                                                                  duration=self._blind_duration,
                                                                  _enrager=self.user.eid))
            else:  # This is Just In Case, I guess? I'm not sure why I put it there. Probably just to be safe...?
                return False

            self._level.add_command(command)
            return True
        except AttributeError as e:
            warnings.warn(e)
            return False

    # Returns True on completion, False on failure
    #
    # Deals damage to the targeted envrionmental
    def _use_on_env(self, _target):
        """
        :type _target: int
        :rtype: bool
        """
        try:
            cmd_desc = "{0} blasts the {1}, for {2} damage!".format(self.entity_name, self._level.ent_name(_target),
                                                                    self._damage)
            command = cmpd.CompoundCmd(cmd_desc, EntityDealDamage(_target, self._level, self._damage))
            self._level.add_command(command)
            return True
        except AttributeError as e:
            warnings.warn(e)
            return False