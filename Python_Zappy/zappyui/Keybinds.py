__author__ = 'Travis Moy'

from zappyui.Orders import ORDERS
from pyglet.window import key


def DEFAULT_KEYBINDS():
    binds = dict()
    binds[key.UP] = ORDERS.UP
    binds[key.RIGHT] = ORDERS.RIGHT
    binds[key.LEFT] = ORDERS.LEFT
    binds[key.DOWN] = ORDERS.DOWN
    binds[key.ENTER] = ORDERS.CONFIRM
    binds[key.BACKSPACE] = ORDERS.CANCEL
    return binds


# Transforms keypresses into orders
# Inputs map to orders. Inputs cannot be multiply bound.
class Keybinds(object):

    def __init__(self, binds="DEFAULT_KEYBINDS"):
        # Necessary to prevent default Keybind objects from interfering with each other.
        # Not that I'm planning to have more than one, but never hurts to be flexible.
        if binds == 'DEFAULT_KEYBINDS':
            self._binds = DEFAULT_KEYBINDS()
        else:
            self._binds = binds

    def key_is_bound(self, key):
        pass

    def bind_key(self, key, order):
        pass

    def unbind_key(self, key):
        pass

    def handle_keys(self, symbol, modifiers):
        pass