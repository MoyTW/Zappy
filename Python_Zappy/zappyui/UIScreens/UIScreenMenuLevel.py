__author__ = 'Travis Moy'

import UIScreen
import pyglet
from zappyui.Orders import ORDERS


# Init must take - what?
# At some point we've got to integrate player history in here, too.
class UIScreenMenuLevel(UIScreen.UIScreen):
    ASSETS_PATH = 'images/menu_level/'
    IMAGE_SIZE = 300

    def __init__(self, loader_level, factory):
        self._loader_level = loader_level
        self._factory = factory

        self._num_levels = self._loader_level.get_num_levels()

    def handle_order(self, order):
        pass

    def draw(self):
        pass