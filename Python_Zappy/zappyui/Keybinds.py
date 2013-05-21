__author__ = 'Travis Moy'

#from pyglet.window import key
#from zappyui.Orders import ORDERS

# OKAY. SO. Here's what I've got so far.
# You can uncomment EITHER the __init__(self, binds="Blue!") def, OR the DEFAULT_KEYBINDS def. If you uncomment both,
# it explodes, even if the init def doesn't reference the DEFAULT_KEYBINDS def.
# Curiously, an __init__(self): taking no default parameters doesn't bug out. It can take a parameter, but if you make
# a default value...

# You can ALSO stop it from bugging out if you put a 'pass' (and nothing else) in DEFAULT_KEYBINDS, but...hmm.

# So, ANY function in Keybinds which takes a default parameter, combined with the definition of DEFAULT_KEYBINDS which
# does something, is causing the error.

# I guess the question is "Why does what I do in Keybinds.py influence my testCameraSetLevel"?

# Let's see if I can't narrow down what's going on in scratch_paper.


def DEFAULT_KEYBINDS():
    return dict()


# Transforms keypresses into orders
class ZAPPY_Keybinds(object):
    pass

    def function_with_default_param(self, fancifully_named_input="ZOO"):
        self._thing = fancifully_named_input

    #def __init__(self, blue):
    #    self.what = "WHAT"
    #    self.blue = blue

    #def __init__(self, blue=5):
    #    self.what = "WHAT"
    #    self.blue = blue

    #def __init__(self, binds="Blue!"):
    #    self._binds = binds

    #def __init__(self, binds=DEFAULT_KEYBINDS()):
    #    self._binds = binds

########################################################################################################################
    #def handle_keys(self, symbol, modifiers):
    #    pass