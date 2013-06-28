__author__ = 'Travis Moy'

import Tool
import entity.environmentals.Environmental as Environmental
from z_defs import RANK


'''
    Can trigger collapses, break open pits, etc, etc, from a longer range than the Waldos and with greater force. Can
also do thinks like kill weak enemies, blind average ones, and irritate powerful and terrifying ones.

How to manage?
    - If enemy, check strength (I need to add this in). Then, apply status effect.
    - Instead of "triggering" Environmentals, it "attacks" them.
'''


class ToolSamplingLaser(Tool.Tool):
    def __init__(self, _level, _strength=5, **kwargs):
        self._strength = _strength
        kwargs['_list_target_types'] = [self.TYPE_ENTITY]
        kwargs['_requires_LOS'] = True
        super(ToolSamplingLaser, self).__init__(_level, **kwargs)

    def _effects_of_use_on_entity(self, _target):
        if not self._use_on_actor(_target):
            self._use_on_env(_target)

    # Returns True on completion, False on failure
    #
    # If RANK == WEAK, kill
    # If RANK == AVERAGE, blind
    # If RANK == POWERFUL or RANK == TERRIFYING, enrage
    def _use_on_actor(self, _target):
        pass

    # Returns True on completion, False on failure
    #
    # Deals damage to the targeted envrionmental
    def _use_on_env(self, _target):
        pass