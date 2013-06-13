__author__ = 'Travis Moy'

import Tool
from z_defs import RANK
import entity.actor.effects.EffectStun as EffectStun


'''
Lets you stun enemies; weak for less than average, powerful, terrifying (15?8?4?2?)
What do we need to do to implement this?
  Some method of skipping turns, or causing turns to be skipped.
      -Status Effects, like Blind, Stunned, Deafened? Create a at_end_of_turn() function in Actor, called after? Or a
front-loaded one, like at_beginning_of_turn() function? Or possibly both?
'''


class ZapGun(Tool.Tool):
    def __init__(self, _level, _range=5, _energy_cost=15, _cooldown=2, _image_name=None):
        super(ZapGun, self).__init__(_level, [self.TYPE_ACTOR], _range=_range, _energy_cost=_energy_cost,
                                     _cooldown=_cooldown, _image_name=_image_name)

    def _effects_of_use_on_entity(self, _target, _user, _level):
        try:
            rank = _target.get_rank()
            stun_duration = 0
            if rank == RANK.WEAK:
                stun_duration = 15
            elif rank == RANK.AVERAGE:
                stun_duration = 8
            elif rank == RANK.POWERFUL:
                stun_duration = 4
            elif rank == RANK.TERRIFYING:
                stun_duration = 2
            _target.apply_status_effect(EffectStun.EffectStun(_duration=stun_duration, _target=_target))
        except AttributeError as e:
            print e.message

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