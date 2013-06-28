__author__ = 'Travis Moy'

import Effect


class EffectEnrage(Effect.Effect):

    EFFECT_NAME = 'Enrage'
    EFFECT_DESCRIPTION = 'While this status effect is active, the target will relentlessly pursue the enemy which' \
                         'enraged it. Note: Zappy cannot be enraged!'

    def __init__(self, _duration, _target, _enrager, _application_behavior=Effect.Effect.STACKS):
        super(EffectEnrage, self).__init__(_duration=_duration, _target=_target,
                                           _application_behavior=_application_behavior)
        self._enrager = _enrager

        self._old_select_target_func = None

    def _apply_effects(self):
        if self._target.select_target != self._select_target_override:
            self._old_select_target_func = self._target.select_target
            self._target.select_target = self._select_target_override

    def _unapply_effects(self):
        self._target.select_target = self._old_select_target_func

    def _select_target_override(self):
        return self._enrager