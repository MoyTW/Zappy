__author__ = 'Travis Moy'

import unittest
import pyglet
import zappyui.FactoryScreens as FactoryScreens
import loader.LoaderLevelV1 as LoaderLevelV1
from zappyui.Orders import ORDERS


class TestUIScreen(unittest.TestCase):
    def setUp(self):
        width = 640
        height = 480
        self.window = pyglet.window.Window(width=width, height=height)
        self.loader = LoaderLevelV1.LoaderLevelV1('zappyui/UIScreens/tests/test_levels')
        self.factory = FactoryScreens.FactoryScreens(self.window, self.loader)
        self._setUp()

    def _setUp(self):
        pass

    def tearDown(self):
        self.factory = None
        self.window = None
        self.loader = None
        self.screen = None
        self._tearDown()

    def _tearDown(self):
        pass

    def test_handle_orders_all_orders_for_exceptions(self):
        for i in range(0, ORDERS.num_orders()):
            self.screen.handle_orders(i)

    def test_draw(self):
        self.screen.draw()