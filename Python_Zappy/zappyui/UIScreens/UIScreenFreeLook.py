__author__ = 'Travis Moy'

import UIScreen
from zappyui.Orders import ORDERS


class UIScreenFreeLook(UIScreen.UIScreen):
    def __init__(self, camera):
        self._camera = camera

    def draw(self):
        self._camera.draw()

    def handle_order(self, order):
        if ORDERS.is_direction(order):
            return self._move_camera(order)
        elif order == ORDERS.CANCEL:
            return self._cancel()

    def _move_camera(self, order):
        self._camera.step(ORDERS.to_direction(order))
        return self

    def _cancel(self):
        return None