__author__ = 'Travis Moy'

import Tool


'''
Lets you stun enemies; weak for less than average, powerful, terrifying (15?8?4?2?)
What do we need to do to implement this?
  Some method of skipping turns, or causing turns to be skipped.
      -Status Effects, like Blind, Stunned, Deafened? Create a at_end_of_turn() function in Actor, called after? Or a
front-loaded one, like at_beginning_of_turn() function? Or possibly both?
'''
class ZapGun(Tool.Tool):
    pass

'''
If you put CD updates at end of turn:
Turn 0: You blast an enemy with a CD 3 ability.
  End turn 0: CD = 2
Turn 1:
  End turn 1: CD = 1
Turn 2:
  End turn 2: CD = 0
Turn 3:
  CD = 0 at start, you may use again.
'''

'''
CD Updates at beginning of turn:
Turn 0: Blast enemy with CD 3.
Turn 1: CD = 2
Turn 2: CD = 1
Turn 3: CD = 0, usable again.
'''

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