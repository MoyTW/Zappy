__author__ = 'Travis Moy'

import Actor
from z_defs import RANK
from entity.actor.Faction import FACTIONS
import warnings


class Adversary(Actor.Actor):
    def __init__(self, _level, _entity_name='Default Adversary Name', _max_hp=1, _max_moves=1, _tools=None,
                 _senses=None, _image_name=None, _behaviors=None, _rank=RANK.AVERAGE, _faction=FACTIONS.ADVERSARY,
                 _base_threat=1, **kwargs):
        super(Adversary, self).__init__(_level=_level, _max_hp=_max_hp, _max_moves=_max_moves, _tools=_tools,
                                        _senses=_senses, _image_name=_image_name, _rank=_rank,
                                        _entity_name=_entity_name, _faction=_faction, _base_threat=_base_threat,
                                        **kwargs)

        if _behaviors is None:
            self._behaviors = list()
        else:
            self._behaviors = _behaviors

    def select_target(self):
        hostiles = list()
        for entity in self._detected_entities:
            try:
                if self._faction.is_hostile_to(entity.get_faction_name()):
                    hostiles.append(entity)
            except AttributeError:
                pass
        hostiles.sort(cmp=lambda x, y: cmp(x.threat, y.threat), reverse=True)

        if len(hostiles) > 0:
            return hostiles[0]
        else:
            return None

    # Adversary.take_action() is called for each Adversary on the level.
    # First, it uses its senses to detect entities.
    #
    # Then, the function will iterate through the behaviors in-order until the entity runs out of moves, or zero
    # behaviors in the list fire.
    #
    # Returns True if any action was taken and False if no actions were taken.
    def take_action(self):
        if self.is_stunned:
            return False

        # This is kind of ugly and awkward, but any_behavior_executed is whether ANY behavior fires.
        # behavior_executed is the controller for the outside loop.
        any_behavior_executed = False
        behavior_executed = True

        while behavior_executed:
            # Try to execute. If at any time it executes, stop and restart - behavior_executed = True.
            # If it does not execute, behavior_executed = False.
            current_behavior = 0
            behavior_executed = False
            target = self.select_target()

            while not behavior_executed and current_behavior < len(self._behaviors):
                behavior_executed = self._behaviors[current_behavior].attempt_to_execute(target,
                                                                                         self._level, self)
                current_behavior += 1

            if behavior_executed:
                any_behavior_executed = True

        return any_behavior_executed