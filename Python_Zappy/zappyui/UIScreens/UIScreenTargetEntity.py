__author__ = 'Travis Moy'

import UIScreen
from zappyui.Orders import ORDERS


class UIScreenTargetEntity(UIScreen.UIScreen):
    def __init__(self, _entity_list, _tool, _level_controller):
        self._entity_list = _entity_list
        self._tool = _tool
        self._control = _level_controller

    def draw(self):
        pass

    def handle_order(self, order):
        pass

    def _cancel(self):
        return None