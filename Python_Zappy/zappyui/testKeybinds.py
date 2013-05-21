__author__ = 'Travis Moy'

import unittest
import zappyui.Keybinds
from pyglet.window import key
from zappyui.Orders import ORDERS


class TestKeybinds(unittest.TestCase):
    def setUp(self):
        self.default_keybinds = zappyui.Keybinds.Keybinds()

    def tearDown(self):
        self.default_keybinds = None

    def test_default_keybinds(self):
        binds = self.default_keybinds._binds
        self.assertEqual(binds[key.LEFT], ORDERS.LEFT)
        self.assertTrue(False)

    def test_bind_key(self):
        self.assertTrue(False)

    def test_unbind_key(self):
        self.assertTrue(False)

suite = unittest.TestLoader().loadTestsFromTestCase(TestKeybinds)
unittest.TextTestRunner(verbosity=2).run(suite)