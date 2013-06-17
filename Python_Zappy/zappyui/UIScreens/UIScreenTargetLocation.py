__author__ = 'Travis Moy'

import UIScreen
from zappyui.Orders import ORDERS


class UIScreenTargetLocation(UIScreen.UIScreen):
    def __init__(self, _tool, _camera, _level_controller, _factory_screens):
        self._tool = _tool
        self._camera = _camera
        self._level_controller = _level_controller
        self._factory = _factory_screens

        self._zappy = _level_controller.get_zappy()

        self._start_tile = self._camera.get_center_tile()

    def draw(self):
        self._camera.draw()

    def handle_order(self, order):
        if ORDERS.is_direction(order):
            return self._move_camera(order)
        elif order == ORDERS.CONFIRM:
            return self._select_target()
        elif order == ORDERS.CANCEL:
            return self._cancel()

    def _move_camera(self, order):
        self._camera.step(ORDERS.to_direction(order))
        return self

    def _cancel(self):
        self._camera.center_on(*self._start_tile)
        return None

    def _select_target(self):
        tar_x, tar_y = self._camera.get_center_tile()
        print "Attempted to target", self._camera.get_center_tile()
        if self._tool.can_use_on_location(tar_x, tar_y, self._zappy):
            self._tool.use_on_location(tar_x, tar_y, self._zappy)
        elif self._tool.targets_entities():
            print "Tool targets entities, not locations!"
        elif self._tool.targets_actors():
            print "Tool targets actors, not entities or locations!"
        return self