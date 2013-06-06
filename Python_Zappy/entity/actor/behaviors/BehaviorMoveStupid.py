__author__ = 'Travis Moy'

import Behavior


# Attempts to move horizontally towards the player. If it cannot, attempts to move vertically towards the player.
# If it cannot, does nothing.
class BehaviorMoveStupid(Behavior.Behavior):

    def attempt_to_execute(self, level, adversary):
        pass

    # Executes if you have a move
    def _can_execute(self, level, adversary):
        pass

    # Tries to move horizontally; else tries to move vertically; else fails.
    def _execute(self, level, adversary):
        pass