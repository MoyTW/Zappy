__author__ = 'Travis Moy'

import unittest
import collections

import dummies.DummyFactory as DummyFactory
import dummies.DummyController as DummyController
import zappyui.UIScreens.UIScreenLevel as UIScreenLevel
import loader
import z_defs
import zappyui.Camera


DummyInfo = collections.namedtuple('DummyInfo', 'width height')


class TestUIScreenLevel(unittest.TestCase):
    def setUp(self):
        temp_loader = loader.LoaderLevel.LoaderLevel('zappyui/test_assets')
        self.dummy_control = DummyController.DummyController(temp_loader.get_level(0))

        self.width = 640
        self.height = 480

        camera = zappyui.Camera.Camera(self.dummy_control.get_level(), lower_left=(0, 0),
                                       upper_right = (self.width - z_defs.SIDEBAR_WIDTH, self.height))

        self.default_screen = UIScreenLevel.UIScreenLevel(camera, self.dummy_control, DummyInfo(0, 0),
                                                          DummyFactory.DummyFactory())

    def tearDown(self):
        pass

    def test_move(self):
        self.assertEqual(self.default_screen, self.default_screen._move("TestOrder"))
        try:
            self.assertEqual(self.dummy_control.zappy_attempt_move_called_with, "TestOrder")
        except AttributeError:
            self.assertFalse(True, "test_move is not calling the controller at all!")

    def test_open_select_tool(self):
        self.assertEqual("ScreenSelectTool", self.default_screen._open_select_tool())

    def test_use_item(self):
        self.assertEqual(self.default_screen, self.default_screen._use_item())
        try:
            self.assertTrue(self.dummy_control.zappy_use_item_called)
        except AttributeError:
            self.assertFalse(True, "use_item is not calling the controller at all!")

    def test_open_free_look(self):
        self.assertEqual("ScreenFreeLook", self.default_screen._open_free_look())

    def test_open_level_menu(self):
        self.assertEqual("ScreenLevelMenu", self.default_screen._open_level_menu())


suite = unittest.TestLoader().loadTestsFromTestCase(TestUIScreenLevel)
unittest.TextTestRunner(verbosity=2).run(suite)