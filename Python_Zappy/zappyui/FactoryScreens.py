__author__ = 'Travis Moy'

import z_defs
import zappyui.UIScreens as Screens
import zappyui.Camera
import zappyui.uiExceptions as uiexcept


class ViewportInfo(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height


class FactoryScreens(object):
    def __init__(self, window, loader_level, level_controller=None):
        self._window = window
        self._loader_level = loader_level

        # Blah blah my convenience.
        self._window_viewport = None
        self._level_viewport = None
        self._init_viewport_infos(window)

        # Blah blah my convenience.
        self._camera = None
        self._level_controller = None
        self.set_level_controller(level_controller)

    def set_level_controller(self, level_controller):
        if level_controller is None:
            self._level_controller = None
            self._camera = None
            return

        self._level_controller = level_controller
        self._camera = zappyui.Camera.Camera(self._level_controller.get_level(),
                                             upper_right=(self._window.width - z_defs.SIDEBAR_WIDTH,
                                                          self._window.height))

    def create_ScreenMenuBase(self):
        return Screens.UIScreenMenuBase.UIScreenMenuBase(self._window_viewport, self)

    def create_ScreenMenuLevel(self):
        return Screens.UIScreenMenuLevel.UIScreenMenuLevel(self._loader_level, self._window_viewport, self)

    def create_ScreenFreeLook(self):
        if self._level_controller is None:
            raise uiexcept.LevelNotLoadedException("Factory was asked to create a in-level screen, but no level was "
                                                   "loaded! The programmer has made a fatal oversight!")
        return Screens.UIScreenFreeLook.UIScreenFreeLook(self._camera)

    def create_ScreenLevel(self):
        if self._level_controller is None:
            raise uiexcept.LevelNotLoadedException("Factory was asked to create a in-level screen, but no level was "
                                                   "loaded! The programmer has made a fatal oversight!")
        return Screens.UIScreenLevel.UIScreenLevel(self._camera, self._level_controller, self._window_viewport, self)

    def create_ScreenLevelMenu(self):
        pass

    def create_ScreenSelectTool(self):
        if self._level_controller is None:
            raise uiexcept.LevelNotLoadedException("Factory was asked to create a in-level screen, but no level was "
                                                   "loaded! The programmer has made a fatal oversight!")
        return Screens.UIScreenSelectTool.UIScreenSelectTool(self._level_controller, self._level_viewport, self)

    def create_ScreenUseTool(self):
        pass

    def _init_viewport_infos(self, window):
        self._window_viewport = ViewportInfo(window.width, window.height)
        self._level_viewport = ViewportInfo(window.width - z_defs.SIDEBAR_WIDTH, window.height)