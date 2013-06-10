__author__ = 'Travis Moy'

import UIScreen


class UIScreenLevelEnd(UIScreen.UIScreen):

    def __init__(self, level_controller):
        self._control = level_controller
        self._level = level_controller.get_level()

    def draw(self):
        print "Level {0} has ended!".format(self._level.get_name())

    def handle_order(self, order):
        return True

