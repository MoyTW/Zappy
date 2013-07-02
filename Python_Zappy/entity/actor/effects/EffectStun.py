__author__ = 'Travis Moy'

import Effect


# How do we handle stuns?
# Most straightforward way is just having a "is_stunned" in Actor, and if so, not taking the action...
class EffectStun(Effect.Effect):

    EFFECT_NAME = 'Stun'
    EFFECT_DESCRIPTION = 'Target is unable to take any action for the duration of the stun.'

    def _apply_effects(self):
        self._target.is_stunned = True

    def _unapply_effects(self):
        self._target.is_stunned = False