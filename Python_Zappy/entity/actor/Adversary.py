__author__ = 'Travis Moy'

import Actor


class Adversary(Actor.Actor):
    def __init__(self, level, behaviors=None, max_moves=1, x=-1, y=-1, tools=None, senses=None, image_name=None):
        super(Adversary, self).__init__(level=level, max_moves=max_moves, x=x, y=y, tools=tools, senses=senses,
                                        image_name=image_name)

        self._behaviors = behaviors

    # Adversary.take_action() is called for each Adversary on the level.
    # The function will iterate through the behaviors in-order until it has exhausted the list, or the entity runs out
    # of moves.
    def take_action(self):
        pass