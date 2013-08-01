__author__ = 'Travis Moy'

import level.LevelController as LevelController
import zappyui.UIScreens.tests.parentTestUIScreen as parent


class TestUIScreenSelectTool(parent.TestUIScreen):
    def _setUp(self):
        level = self.loader.get_level(0)
        level_controller = LevelController.LevelController(level)
        self.factory.set_level_controller(level_controller)
        self.screen = self.factory.create_ScreenSelectTool()

    def _tearDown(self):
        self.screen = None