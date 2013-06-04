from zappyui.UIScreens import UIScreen

__author__ = 'Travis Moy'

from zappyui.Orders import ORDERS


class UIScreenLevel(UIScreen.UIScreen):

    def __init__(self, camera, level_controller, window_viewport_info, factory_screens):
        self._control = level_controller
        self._window_info = window_viewport_info
        self._factory = factory_screens
        self._camera = camera

        print self._camera._upper_right

        self._init_camera(level_controller)

    def _init_camera(self, level_controller):
        level = level_controller.get_level()
        self._camera.center_on((level.get_width() / 2), (level.get_height() / 2))
        self._camera.center_on_entity(self._control.get_zappy())

    def handle_order(self, order):
        return_screen = self

        if order == ORDERS.UP or order == ORDERS.DOWN or order == ORDERS.LEFT or order == ORDERS.RIGHT:
            return_screen = self._move(order)
        elif order == ORDERS.CONFIRM:
            return_screen = self._open_select_tool()
        elif order == ORDERS.ITEMS:
            return_screen = self._use_item()
        elif order == ORDERS.LOOK:
            return_screen = self._open_free_look()
        elif order == ORDERS.MENU:
            return_screen = self._open_level_menu()

        return return_screen

    def draw(self):
        self._camera.draw()

    def draw_if_not_head(self):
        return True

    def _draw_sidebar(self):
        pass

    # If UP/DOWN/LEFT/RIGHT
    def _move(self, order):
        self._control.zappy_attempt_move(ORDERS.to_direction(order))
        self._camera.center_on(*self._control.get_zappy_x_y())
        return self

    # If CONFIRM
    def _open_select_tool(self):
        return self._factory.create_ScreenSelectTool()

    # If ITEMS
    def _use_item(self):
        self._control.zappy_use_item()
        return self

    # If LOOK
    def _open_free_look(self):
        return self._factory.create_ScreenFreeLook()

    # If MENU
    def _open_level_menu(self):
        return self._factory.create_ScreenLevelMenu()