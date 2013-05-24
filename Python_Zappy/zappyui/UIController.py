__author__ = 'Travis Moy'

import Keybinds
import pyglet


class UIController(object):

    def __init__(self, window, base_screen, keybinds=Keybinds.Keybinds()):
        self._window = window
        self._screen_head = base_screen
        self._screen_history = list()
        self._keybinds = keybinds

        if self._window is not None:
            self._setup_callbacks()

    def _handle_keys(self, symbol, modifiers):
        order = self._keybinds.get_order(symbol)

        # Make sure the symbol is a valid key
        if order is None:
            return

        order_result = self._screen_head.handle_order(order)
        if order_result != self._screen_head:
            if order_result is None or order_result is False:
                self._close_head_screen()
            elif order_result is True:
                self._close_head_screen()
                while self._screen_head.close_on_child_completion() and len(self._screen_history) > 0:
                    self._close_head_screen()
            else:
                self._handle_new_screen(order_result)

    def _draw(self):
        self._screen_head.draw()

    def _handle_new_screen(self, head):
        self._screen_history.append(self._screen_head)
        self._screen_head = head

    def _close_head_screen(self):
        if len(self._screen_history) == 0:
            pyglet.app.exit()
        else:
            self._screen_head = self._screen_history[-1]
            self._screen_history.pop(-1)

    # Gamepad support?
    def _setup_callbacks(self):
        @self._window.event
        def on_key_press(symbol, modifiers):
            self._handle_keys(symbol, modifiers)

        @self._window.event
        def on_draw():
            self._window.clear()
            self._draw()