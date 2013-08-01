__author__ = 'Travis Moy'

from z_defs import DIR


class orders(object):
    # The maximum number of orders I want to deal with is 12.
    UP, DOWN, LEFT, RIGHT, CONFIRM, CANCEL, ITEMS, LOOK, MENU = range(0, 9)

    def num_orders(self):
        return 9

    def to_direction(self, order):
        if order == ORDERS.UP:
            return DIR.N
        elif order == ORDERS.RIGHT:
            return DIR.E
        elif order == ORDERS.DOWN:
            return DIR.S
        elif order == ORDERS.LEFT:
            return DIR.W
        else:
            return None

    def is_direction(self, order):
        if order == ORDERS.UP or order == ORDERS.RIGHT or order == ORDERS.DOWN or order == ORDERS.LEFT:
            return True
        else:
            return False

ORDERS = orders()