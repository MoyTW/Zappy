__author__ = 'Travis Moy'


class orders(object):
    # The maximum number of orders I want to deal with is 12.
    UP, DOWN, LEFT, RIGHT, CONFIRM, CANCEL, ITEMS, LOOK, MENU = range(0, 9)

ORDERS = orders()