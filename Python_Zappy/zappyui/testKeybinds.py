__author__ = 'Travis Moy'

import unittest
# IF YOU IMPORT zappyui.Keybinds, the test messes up.
# ...okay. I'm confused, and how the heck do I diagnose what's going wrong?
#import zappyui.Keybinds
#from pyglet.window import key


class TestKeybinds(unittest.TestCase):

    def setUp(self):
        pass
        #self.default_keybinds = zappyui.Keybinds.Keybinds()

    def tearDown(self):
        pass
        #self.default_keybinds = None

    def test_does_this_mess_up_tests(self):
        pass

    def test_default_orders(self):
        pass

suite = unittest.TestLoader().loadTestsFromTestCase(TestKeybinds)
unittest.TextTestRunner(verbosity=2).run(suite)