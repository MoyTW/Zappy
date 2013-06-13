__author__ = 'Travis Moy'

import Effect


# How do we handle stuns?
# Most straightforward way is just having a "is_stunned" in Actor, and if so, not taking the action...
class EffectStun(Effect.Effect):

    def apply(self):
        self._target.stun()

    def unapply(self):
        self._target.unstun()