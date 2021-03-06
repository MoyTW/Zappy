from zappyui.UIScreens import UIScreen

__author__ = 'Travis Moy'

from zappyui.Orders import ORDERS


class UIScreenLevel(UIScreen.UIScreen):

    def __init__(self, camera, level_controller, window_viewport_info, factory_screens):
        self._control = level_controller
        self._window_info = window_viewport_info
        self._factory = factory_screens
        self._camera = camera

        self._init_camera()

    def _init_camera(self):
        self._camera.center_on((self._control.level_width / 2), (self._control.level_height / 2))
        self._camera.center_on_eid(self._control.zappy_eid)

    def handle_order(self, order):
        return_screen = self

        if order == ORDERS.UP or order == ORDERS.DOWN or order == ORDERS.LEFT or order == ORDERS.RIGHT:
            return_screen = self._move(order)
        elif order == ORDERS.CANCEL:
            return_screen = self._end_turn()
        elif order == ORDERS.CONFIRM:
            return_screen = self._open_select_tool()
        elif order == ORDERS.ITEMS:
            return_screen = self._use_item()
        elif order == ORDERS.LOOK:
            return_screen = self._open_free_look()
        elif order == ORDERS.MENU:
            return_screen = self._open_level_menu()

        if self._control.level_completed:
            return_screen = None

        return return_screen

    def _on_destruct_return_screen(self):
        if self._control.level_completed:
            return self._factory.create_ScreenLevelEnd()

    def draw(self):
        self._camera.draw()

    def close_on_child_completion(self):
        return self._control.level_completed

    def draw_if_not_head(self):
        return True

    def _draw_sidebar(self):
        pass

    # If UP/DOWN/LEFT/RIGHT
    def _move(self, order):
        self._control.zappy_attempt_move(ORDERS.to_direction(order))
        self._camera.center_on(*self._control.get_zappy_x_y())
        return self

    # If CANCEL
    def _end_turn(self):
        self._control.turn_has_ended()
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