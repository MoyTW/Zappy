__author__ = 'Travis Moy'

import Effect


# On apply, iterate through senses, call sense.blind()
# On unapply, iterate through senses, call sense.unblind()
class EffectBlind(Effect.Effect):

    def __init__(self, _duration, _target, _application_behavior=Effect.Effect.STACKS):
        super(EffectBlind, self).__init__(_duration=_duration, _target=_target,
                                          _application_behavior=_application_behavior)

        self._sight_holding = list()

    # Iterate through senses, checking for SenseSight objects. Rip all that you find into _sight_holding.
    def _apply_effects(self):
        pass

    # Add all the senses stripped from the Actor back in.
    def _unapply_effects(self):
        pass