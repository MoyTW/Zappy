__author__ = 'Travis Moy'

import Tool
import entity.actor.effects.EffectEnrage as EffectEnrage
import entity.actor.effects.EffectBlind as EffectBlind
from z_defs import RANK


'''
    Can trigger collapses, break open pits, etc, etc, from a longer range than the Waldos and with greater force. Can
also do thinks like kill weak enemies, blind average ones, and irritate powerful and terrifying ones.

How to manage?
    - If enemy, check strength (I need to add this in). Then, apply status effect.
    - Instead of "triggering" Environmentals, it "attacks" them.
'''


class ToolSamplingLaser(Tool.Tool):
    def __init__(self, _level, _damage=5, _blind_duration=14, _enrage_duration=7, **kwargs):
        self._damage = _damage
        self._blind_duration = _blind_duration
        self._enrage_duration = _enrage_duration
        kwargs['_list_target_types'] = [self.TYPE_ENTITY]
        kwargs['_requires_LOS'] = True
        super(ToolSamplingLaser, self).__init__(_level, **kwargs)

    def _effects_of_use_on_entity(self, _target):
        done = self._use_on_actor(_target)
        if not done:
            done = self._use_on_env(_target)
        return done

    # Returns True on completion, False on failure
    #
    # If RANK == WEAK, kill
    # If RANK == AVERAGE, blind
    # If RANK == POWERFUL or RANK == TERRIFYING, enrage
    def _use_on_actor(self, _target):
        try:
            rank = _target.rank
            if rank == RANK.WEAK:
                _target.deal_damage(_target.current_hp)
            elif rank == RANK.AVERAGE:
                _target.apply_status_effect(EffectBlind.EffectBlind(self._blind_duration, _target))
            elif rank == RANK.POWERFUL or rank == RANK.TERRIFYING:
                _target.apply_status_effect(EffectEnrage.EffectEnrage(self._enrage_duration, _target, self.user))
            else:
                return False
            return True
        except AttributeError:
            return False

    # Returns True on completion, False on failure
    #
    # Deals damage to the targeted envrionmental
    def _use_on_env(self, _target):
        try:
            _target.deal_damage(self._damage)
            return True
        except AttributeError:
            return False