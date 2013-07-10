__author__ = 'Travis Moy'

import Effect
import entity.actor.senses.SenseSight as SenseSight


# On apply, iterate through senses, call sense.blind()
# On unapply, iterate through senses, call sense.unblind()
class EffectBlind(Effect.Effect):

    EFFECT_NAME = 'Blind'
    EFFECT_DESCRIPTION = 'While this status effect is active, the target cannot see and must rely on other senses!'

    def __init__(self, _duration, _target, _application_behavior=Effect.Effect.STACKS):
        super(EffectBlind, self).__init__(_duration=_duration, _target=_target,
                                          _application_behavior=_application_behavior)

        self._sight_holding = list()

    # Iterate through senses, checking for SenseSight objects. Rip all that you find into _sight_holding.
    def _apply_effects(self):
        senses = self._target.get_senses()
        for sense in senses[:]:  # I'm really only using this because I never use slice notation. It's a copy, FYI.
            if isinstance(sense, SenseSight.SenseSight):
                self._sight_holding.append(sense)
                senses.remove(sense)

    # Add all the senses stripped from the Actor back in.
    def _unapply_effects(self):
        senses = self._target.get_senses()
        for sense in self._sight_holding:
            senses.append(sense)