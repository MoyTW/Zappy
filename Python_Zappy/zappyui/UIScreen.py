__author__ = 'Travis Moy'

import warnings


class UIScreen(object):

    def handle_keys(self, symbol, modifiers, previous_mode):
        warnings.warn("UIScreen.handle_keys() was called! This shouldn't happen - something has gone horribly wrong!")
        return self

    def draw(self):
        warnings.warn("UIScreen.draw() was called! This shouldn't happen - something has gone horribly wrong!")
