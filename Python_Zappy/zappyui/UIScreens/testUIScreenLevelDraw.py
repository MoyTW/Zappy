__author__ = 'Travis Moy'

from pyglet.window import key
import unittest
import pyglet
import loader.LoaderLevel
import zappyui.UIScreens.UIScreenLevel as UIScreenLevel
import zappyui.UIScreens.DummyController as DummyController
import zappyui.UIScreens.DummyFactory as DummyFactory


class DummyWindowInfo(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height


class TestUIScreenLevel(unittest.TestCase):
    def setUp(self):
        pyglet.resource.path = ['@zappyui', '.']
        pyglet.resource.reindex()

        self.width = 640
        self.height = 480

        temp_loader = loader.LoaderLevel.LoaderLevel('zappyui/test_assets')
        self.default_level = temp_loader.get_level(0)

        self.default_screen = UIScreenLevel.UIScreenLevel(DummyController.DummyController(self.default_level),
                                                          DummyWindowInfo(self.width, self.height),
                                                          DummyFactory.DummyFactory())

    def tearDown(self):
        pass

    def test_screen_draw_expected_failure(self):
        '''
        self.good = True
        window = pyglet.window.Window(width=self.width, height=self.height)

        header = pyglet.text.Label('TEST: UIScreenLevel.draw()', font_size=30, x=self.width // 2, y=self.height - 60,
                                   anchor_x='center', anchor_y='center')

        @window.event
        def on_draw():
            window.clear()
            self.default_screen.draw()
            header.draw()

        @window.event
        def on_key_press(symbol, modifiers):
            if symbol != key.Y:
                self.good = False
            pyglet.app.exit()

        pyglet.app.run()

        self.assertTrue(self.good, "User did not accept results of test.")
        '''
        self.assertTrue(False, "Not yet implemented to my satisfaction.")


#suite = unittest.TestLoader().loadTestsFromTestCase(TestUIScreenLevel)
#unittest.TextTestRunner(verbosity=2).run(suite)