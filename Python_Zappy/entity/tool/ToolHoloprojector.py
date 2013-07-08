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

    def __init__(self, _eid, _level, _holo_name='Hologram', _hp=999, _threat=9, **kwargs):
        self._holo_name = _holo_name
        self._hp = _hp
        self._threat = _threat
        kwargs['_list_target_types'] = [self.TYPE_LOCATION]
        kwargs['_requires_LOS'] = True
        super(ToolHoloprojector, self).__init__(_eid=_eid, _level=_level, **kwargs)

    def _effects_of_use_on_location(self, _x, _y):
        user_faction = self.user.faction
        holo = Actor.Actor(0, self._level, _entity_name=self._holo_name, _max_hp=self._hp, _faction=user_faction,
                           _base_threat=self._threat)
        holo.apply_status_effect(EffectDeath.EffectDeath(5, holo))
        self._level.place_entity_at(holo, _x, _y)