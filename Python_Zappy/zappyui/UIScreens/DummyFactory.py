__author__ = 'Travis Moy'


class DummyFactory(object):

    def create_ScreenSelectTool(self):
        return "ScreenSelectTool"

    def create_ScreenFreeLook(self):
        return "ScreenFreeLook"

    def create_ScreenLevelMenu(self):
        return "ScreenLevelMenu"

    def create_ScreenLevel(self, level_controller):
        return "ScreenLevel"
