__author__ = 'Travis Moy'

import UIScreen
import zappyui.Camera
from zappyui.Orders import ORDERS


class UIScreenLevel(UIScreen.UIScreen):
    def __init__(self, level_controller, factory_screens):
        self._control = level_controller
        self._factory = factory_screens

        self._camera = zappyui.Camera.Camera(level_controller.get_level())

    def handle_order(self, order):
        return_screen = self

        if order == ORDERS.UP or order == ORDERS.DOWN or order == ORDERS.LEFT or order == ORDERS.RIGHT:
            return_screen = self._move(order)
        elif order == ORDERS.CONFIRM:
            return_screen = self._open_select_tools()
        elif order == ORDERS.ITEMS:
            return_screen = self._use_item()
        elif order == ORDERS.LOOK:
            return_screen = self._open_free_look()
        elif order == ORDERS.MENU:
            return_screen = self._open_level_menu()

        return return_screen

    def draw(self):
        pass

    # If UP/DOWN/LEFT/RIGHT
    def _move(self, order):
        pass

    # If CONFIRM
    def _open_select_tools(self):
        pass

    # If ITEMS
    def _use_item(self):
        pass

    # If LOOK
    def _open_free_look(self):
        pass

    # If MENU
    def _open_level_menu(self):
        pass