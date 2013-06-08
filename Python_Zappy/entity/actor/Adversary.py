__author__ = 'Travis Moy'

import Actor


class Adversary(Actor.Actor):
    def __init__(self, level, behaviors=None, max_moves=1, x=-1, y=-1, tools=None, senses=None, image_name=None):
        super(Adversary, self).__init__(level=level, max_moves=max_moves, x=x, y=y, tools=tools, senses=senses,
                                        image_name=image_name)

        if behaviors is None:
            self._behaviors = list()
        else:
            self._behaviors = behaviors

    # Adversary.take_action() is called for each Adversary on the level.
    # First, it uses its senses to detect entities.
    #
    # Then, the function will iterate through the behaviors in-order until it has exhausted the list, or the entity
    # runs out of moves.
    #
    # Returns True if any action was taken and False if no actions were taken.
    def take_action(self):
        pass