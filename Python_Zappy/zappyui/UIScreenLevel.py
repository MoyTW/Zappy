__author__ = 'Travis Moy'

import UIScreen
import zappyui.Camera


class UIScreenLevel(UIScreen.UIScreen):
    camera = zappyui.Camera.Camera()

    def handle_order(self, order):
        return self

    def draw(self):
        pass
