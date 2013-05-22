__author__ = 'Travis Moy'

import zappyui.UIScreens as Screens


class FactoryScreens(object):
    def __init__(self, window):
        self._window = window

    def create_ScreenLevel(self, level_controller):
        return Screens.UIScreenLevel.UIScreenLevel(level_controller, self._window, self)