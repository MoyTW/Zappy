__author__ = 'Travis Moy'

import unittest
import zappyui.FactoryScreens
from dummies.DummyWindow import DummyWindow


class TestFactoryScreens(unittest.TestCase):
    def setUp(self):
        self.width = 640
        self.height = 480
        self.default_factory = zappyui.FactoryScreens.FactoryScreens(DummyWindow(self.width, self.height))

    def tearDown(self):
        self.default_factory = None

    #def test_set_level_controller(self):
    #    self.default_factory.set_level_controller()

suite = unittest.TestLoader().loadTestsFromTestCase(TestFactoryScreens)
unittest.TextTestRunner(verbosity=2).run(suite)
