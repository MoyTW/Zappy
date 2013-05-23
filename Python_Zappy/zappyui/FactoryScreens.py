__author__ = 'Travis Moy'

import z_defs


class ViewportInfo(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height


class FactoryScreens(object):
    def __init__(self, window, level_controller=None):
        self._window = window
        self._sidebar_width = z_defs.SIDEBAR_WIDTH

        # Blah blah my convenience.
        self._window_viewport = None
        self._level_viewport = None
        self._init_viewport_infos(window)

        # Blah blah my convenience.
        self._camera = None
        self._level_controller = None
        self.set_level_controller(level_controller)

    def set_level_controller(self, level_controller):
        pass

    def create_ScreenLevel(self):
        pass
        #return Screens.UIScreenLevel.UIScreenLevel(level_controller, self._window_viewport, self)

    def create_ScreenSelectTool(self):
        pass

    def create_ScreenUseTool(self):
        pass

    def _init_viewport_infos(self, window):
        self._window_viewport = ViewportInfo(window.width, window.height)
        self._level_viewport = ViewportInfo(window.width - self._sidebar_width, window.height)