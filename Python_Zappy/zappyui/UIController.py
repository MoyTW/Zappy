__author__ = 'Travis Moy'

import Keybinds


class UIController(object):

    def __init__(self, window, base_screen, keybinds=Keybinds.Keybinds()):
        self._window = window
        self._screen_head = base_screen
        self._screen_history = list()
        self._keybinds = keybinds

    def _handle_keys(self, symbol, modifiers):
        pass

    def _draw(self):
        pass

    def _handle_new_screen(self, head):
        pass

    def _close_head_screen(self):
        pass

    def _setup_callbacks(self):
        pass