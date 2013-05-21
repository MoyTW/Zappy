__author__ = 'Travis Moy'

#from pyglet.window import key
#from zappyui.Orders import ORDERS


def DEFAULT_KEYBINDS():
    return dict()


# Transforms keypresses into orders
class Keybinds(object):

    def __init__(self, binds=DEFAULT_KEYBINDS()):
        self._binds = binds
    
    def handle_keys(self, symbol, modifiers):
        pass