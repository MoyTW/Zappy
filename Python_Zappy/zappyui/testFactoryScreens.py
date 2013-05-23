__author__ = 'Travis Moy'

import unittest
import FactoryScreens


class DummyWindow(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height


class TestFactoryScreens(unittest.TestCase):
    def setUp(self):
        self.width = 640
        self.height = 480
        self.default_factory = FactoryScreens.FactoryScreens(DummyWindow(640, 480))

    def tearDown(self):
        self.default_factory = None

suite = unittest.TestLoader().loadTestsFromTestCase(TestFactoryScreens)
unittest.TextTestRunner(verbosity=2).run(suite)