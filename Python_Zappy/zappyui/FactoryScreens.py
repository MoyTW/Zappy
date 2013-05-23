__author__ = 'Travis Moy'

import zappyui.UIScreens as Screens


class ViewportInfo(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height


class FactoryScreens(object):
    def __init__(self, window, level_controller=None):
        self._window = window
        self._sidebar_width = Screens.UIScreenLevel.sidebar_width
        self._level_controller = level_controller

        # Blah blah my convenience.
        self._window_viewport = None
        self._level_viewport = None
        self._init_viewport_infos(window)

    def _init_viewport_infos(self, window):
        self._window_viewport = ViewportInfo(window.width, window.height)
        self._level_viewport = ViewportInfo(window.width - self._sidebar_width, window.height)

    def set_level_controller(self):
        pass

    def create_ScreenLevel(self):
        pass
        #return Screens.UIScreenLevel.UIScreenLevel(level_controller, self._window_viewport, self)

    def create_ScreenSelectTool(self):
        pass

    def create_ScreenUseTool(self):
        pass