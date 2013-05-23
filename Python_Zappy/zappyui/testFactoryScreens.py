__author__ = 'Travis Moy'

import unittest
import zappyui.FactoryScreens
from dummies.DummyWindow import DummyWindow
from dummies.DummyController import DummyController
from z_defs import SIDEBAR_WIDTH


class TestFactoryScreens(unittest.TestCase):
    def setUp(self):
        self.width = 640
        self.height = 480
        self.dummy_control = DummyController(None)
        self.default_factory = zappyui.FactoryScreens.FactoryScreens(DummyWindow(self.width, self.height))

    def tearDown(self):
        self.default_factory = None

    def test_set_level_controller_not_none(self):
        self.default_factory.set_level_controller(self.dummy_control)
        self.assertEqual(self.default_factory._level_controller, self.dummy_control)
        self.assertTrue(self.default_factory._camera is not None)
        self.assertEqual(self.default_factory._camera._upper_right, (self.width - SIDEBAR_WIDTH, self.height))

    def test_set_level_controller_none(self):
        self.default_factory.set_level_controller(self.dummy_control)
        self.default_factory.set_level_controller(None)
        self.assertEqual(self.default_factory._level_controller, None)
        self.assertEqual(self.default_factory._camera, None)

suite = unittest.TestLoader().loadTestsFromTestCase(TestFactoryScreens)
unittest.TextTestRunner(verbosity=2).run(suite)
