__author__ = 'Travis Moy'

import Actor


class Adversary(Actor.Actor):
    def __init__(self, level, max_hp=1, max_moves=1, tools=None, senses=None, image_name=None, behaviors=None):
        super(Adversary, self).__init__(level=level, max_hp=max_hp, max_moves=max_moves, tools=tools,
                                        senses=senses, image_name=image_name)

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