__author__ = 'Travis Moy'

import UIScreen
import pyglet
from zappyui.Orders import ORDERS


class UIScreenMenuBase(UIScreen.UIScreen):
    ASSETS_PATH = 'images/menu_level/'

    def __init__(self):
        pass

    def handle_order(self, order):
        pass

    def draw(self):
        pass