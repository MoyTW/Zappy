__author__ = 'Travis Moy'

#from pyglet.window import key
#from zappyui.Orders import ORDERS

# OKAY. SO. Here's what I've got so far.
# You can uncomment EITHER the __init__(self, binds="Blue!") def, OR the DEFAULT_KEYBINDS def. If you uncomment both,
# it explodes, even if the init def doesn't reference the DEFAULT_KEYBINDS def.
# Curiously, an __init__(self): taking no default parameters doesn't bug out. It can take a parameter, but if you make
# a default value...

def DEFAULT_KEYBINDS():
    return dict()


# Transforms keypresses into orders
class Keybinds(object):
    pass

    #def __init__(self, blue):
    #    self.what = "WHAT"
    #    self.blue = blue
    def __init__(self, blue=5):
        self.what = "WHAT"
        self.blue = blue
    #def __init__(self, binds="Blue!"):
    #    self._binds = binds
        
    # OKAY hold on a moment. When I put in binds=DEFAULT_KEYBINDS(), what is happening?
    # Is it binding it to the dictionary created by the function DEFAULT_KEYBINDS? YES IT IS, BUT IT RUNS IT ONCE AT THE
    # START AND THEN USES THAT FOR ALL FUTURE OBJECTS
    # Or is it binding to the result returned by DEFAULT_KEYBINDS()?
    # Remember you've had Issues with Python initializers before!

    # Wait, hold on. I *thought* python naming could go however you liked, case-wise, but am I accidentally mucking up
    # the function definition there? NO YOU'RE NOT.

    #def __init__(self, binds=DEFAULT_KEYBINDS()):
    #    self._binds = binds
    
    #def handle_keys(self, symbol, modifiers):
    #    pass