__author__ = 'Travis Moy'

import Tool
from z_defs import RANK
import entity.actor.effects.EffectStun as EffectStun
import warnings


'''
Lets you stun enemies; weak for less than average, powerful, terrifying (15?8?4?2?)
What do we need to do to implement this?
  Some method of skipping turns, or causing turns to be skipped.
      -Status Effects, like Blind, Stunned, Deafened? Create a at_end_of_turn() function in Actor, called after? Or a
front-loaded one, like at_beginning_of_turn() function? Or possibly both?
'''


class ToolZapGun(Tool.Tool):
    def __init__(self, _eid, _level, **kwargs):
        kwargs['_list_target_types'] = [self.TYPE_ACTOR]
        kwargs['_requires_LOS'] = True
        super(ToolZapGun, self).__init__(_eid=_eid, _level=_level, **kwargs)

    def _effects_of_use_on_entity(self, _target_eid):
        """
        :type _target_eid: int
        :rtype: bool
        """
        try:
            rank = _target_eid.rank
            stun_duration = 0
            if rank == RANK.WEAK:
                stun_duration = 15
            elif rank == RANK.AVERAGE:
                stun_duration = 8
            elif rank == RANK.POWERFUL:
                stun_duration = 4
            elif rank == RANK.TERRIFYING:
                stun_duration = 2
            _target_eid.apply_status_effect(EffectStun.EffectStun(_duration=stun_duration, _target=_target_eid))
        except AttributeError as e:
            warnings.warn(e.message)

'''
Status effects:
Hit the Bantha with Stun: 3 turns
Beginning: Checks for status; stunned (take_action() replaced by "return True")
    Bantha's turn: Stunned
    End: Stunned -= 1 -> 2 turns (take_action() restored to old state)
Beginning: Checks for status; stunned (take_action() replaced by "return True")
    Bantha's turn: Stunned
    End: Stunned -= 1 -> 1 turns (take_action() restored to old state)
Beginning: Checks for status; stunned (take_action() replaced by "return True")
    Bantha's turn: Stunned
    End: Stunned -= 1 -> 0 turns (take_action() restored to old state)
Bantha's turn: Can act
'''