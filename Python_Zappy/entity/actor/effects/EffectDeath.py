__author__ = 'Travis Moy'

import Effect


class EffectDeath(Effect.Effect):

    EFFECT_NAME = 'Death'
    EFFECT_DESCRIPTION = 'When this status effect expires, the target will take massive damage and prompty expire.'

    def _unapply_effects(self):
        self._target.deal_damage(9999)