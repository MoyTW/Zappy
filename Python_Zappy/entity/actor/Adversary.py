__author__ = 'Travis Moy'

import Actor
from z_defs import RANK


class Adversary(Actor.Actor):
    def __init__(self, _level, _entity_name='Default Adversary Name', max_hp=1, max_moves=1, tools=None, senses=None,
                 _image_name=None, behaviors=None, rank=RANK.AVERAGE):
        super(Adversary, self).__init__(_level=_level, max_hp=max_hp, max_moves=max_moves, tools=tools,
                                        senses=senses, _image_name=_image_name, rank=rank, _entity_name=_entity_name)

        if behaviors is None:
            self._behaviors = list()
        else:
            self._behaviors = behaviors

    # Adversary.take_action() is called for each Adversary on the level.
    # First, it uses its senses to detect entities.
    #
    # Then, the function will iterate through the behaviors in-order until the entity runs out of moves, or zero
    # behaviors in the list fire.
    #
    # Returns True if any action was taken and False if no actions were taken.
    def take_action(self):
        self.detect_entities()

        if self.is_stunned():
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

            while not behavior_executed and current_behavior < len(self._behaviors):
                behavior_executed = self._behaviors[current_behavior].attempt_to_execute(self._level, self)
                current_behavior += 1

            if behavior_executed:
                any_behavior_executed = True

        return any_behavior_executed