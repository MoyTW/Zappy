__author__ = 'Travis Moy'

import Tool
import entity.actor.Actor as Actor
import entity.actor.effects.EffectDeath as EffectDeath


# How does the holoprojector work?
# We will need to change how the targeting works for the Adversaries.
#   First off, they can't just look for the player. They have to look for objects not aligned to themselves. That means
# adding in a faction-style system.
#   Secondly, they have to be able to evaluate targets over other targets. That is, have a method for choosing targets
# in a deterministic (sp?) manner. That would be something like a "targeting priority" embedded in Actor objects, or
# a "threat" counter that can go up and down based on actions.
#   The way the holoprojector would work would be to create a new Actor with a higher priority than Zappy, thereby
# distracting the enemies.
class ToolHoloprojector(Tool.Tool):
    HOLO_NAME = 'Hologram'
    HOLO_HP = 999
    HOLO_THREAT = 9

    def __init__(self, *args, **kwargs):
        kwargs['_list_target_types'] = [self.TYPE_LOCATION]
        kwargs['_requires_LOS'] = True
        super(ToolHoloprojector, self).__init__(*args, **kwargs)

    def _effects_of_use_on_location(self, _x, _y):
        user_faction = self._user.get_faction()
        holo = Actor.Actor(self._level, _entity_name=self.HOLO_NAME, _max_hp=self.HOLO_HP, _faction=user_faction,
                           _base_threat=self.HOLO_THREAT)
        holo.apply_status_effect(EffectDeath.EffectDeath(5, holo))
        self._level.place_entity_at(holo, _x, _y)