__author__ = 'Travis Moy'

import Tool
import entity.actor.Actor as Actor
import entity.actor.effects.EffectDeath as EffectDeath
import warnings

import level.commands.CompoundCmd as cmpd
from level.commands.command_fragments import LevelPlaceAndAssignEntityID

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
        """
        :type _eid: int
        :type _level: level.LevelView.LevelView
        :type _holo_name: str
        :type _hp: int
        :type _threat: int
        """
        warnings.warn("ToolHoloprojector's created Actors always have ID=-1!")
        self._holo_name = _holo_name
        self._hp = _hp
        self._threat = _threat
        kwargs['_list_target_types'] = [self.TYPE_LOCATION]
        kwargs['_requires_LOS'] = True
        super(ToolHoloprojector, self).__init__(_eid=_eid, _level=_level, **kwargs)

    # How do we handle the entity creation?
    #
    # We've got a few options I can think of:
    #
    #   Provide a function which lets us manipulate Level's entity ID attribute directly (won't do this because if I'm
    #   going to make Commands to get rid of direct access I'm drat well not putting it back in!)
    #
    #   Provide a Command to create an Actor with the specified parameters (probably using **kwargs because I don't want
    #   a Command with a zillion different parameters I'll have to update if I ever change Actor's constructor again).
    #   This would be like, CreateAndPlaceActor.
    #
    #   Provide a Command that takes an Actor, but which reassigns its id. So, you create an Actor in the Holoprojector,
    #   and pass it to the command, which then goes out to the Level and reassigns its id and then places it. So, like,
    #   PlaceNewlyCreatedEntity or something.
    #
    #   We'll go with the last one.

    def _effects_of_use_on_location(self, _x, _y):
        """
        :type _x: int
        :type _y: int
        :rtype: bool
        """
        holo = Actor.Actor(-1, self._level, _entity_name=self._holo_name, _max_hp=self._hp, _faction=self.user.faction,
                           _base_threat=self._threat)
        holo.apply_status_effect(EffectDeath.EffectDeath(5, holo))
        cmd_desc = "The holoprojector creates an image at ({0}, {1})!".format(_x, _y)
        command = cmpd.CompoundCmd(cmd_desc, LevelPlaceAndAssignEntityID(holo, _x, _y))
        self._level.add_command(command)