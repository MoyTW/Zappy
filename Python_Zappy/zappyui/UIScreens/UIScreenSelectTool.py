__author__ = 'Travis Moy'

import UIScreen
from zappyui.Orders import ORDERS


class UIScreenSelectTool(UIScreen.UIScreen):
    def __init__(self, level_controller, viewport_info, factory_screens, selection=0):
        self._control = level_controller
        self._viewport = viewport_info
        self._factory = factory_screens
        self._selection = selection

        self._tools_list = None
        self._init_tools(level_controller)

    def _init_tools(self, level_controller):
        self._tools_list = level_controller.zappy_get_tools()

    def handle_order(self, order):
        if order == ORDERS.LEFT or order == ORDERS.RIGHT:
            return self._move_selection(order)
        elif order == ORDERS.CONFIRM:
            return self._select_tool()
        elif order == ORDERS.CANCEL:
            return self._cancel()

    def draw(self):
        print "In ScreenSelectTool now."

    def close_on_child_completion(self):
        return True

    def _select_tool(self):
        tool = self._tools_list[self._selection]
        return self._factory.create_ScreenUseTool(tool)

    def _move_selection(self, order):
        if order == ORDERS.LEFT:
            self._selection -= 1
            if self._selection < 0:
                self._selection = len(self._tools_list - 1)
        elif order == ORDERS.RIGHT:
            self._selection += 1
            if self._selection >= len(self._tools_list):
                self._selection = 0
        return self

    def _cancel(self):
        return None