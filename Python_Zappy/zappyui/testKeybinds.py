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
        binds = zappyui.Keybinds.DEFAULT_KEYBINDS()
        self.assertEqual(binds[key.UP], ORDERS.UP)
        self.assertEqual(binds[key.DOWN], ORDERS.DOWN)
        self.assertEqual(binds[key.LEFT], ORDERS.LEFT)
        self.assertEqual(binds[key.RIGHT], ORDERS.RIGHT)
        self.assertEqual(binds[key.ENTER], ORDERS.CONFIRM)
        self.assertEqual(binds[key.BACKSPACE], ORDERS.CANCEL)

    def test_key_is_bound(self):
        self.assertTrue(self.default_keybinds.key_is_bound(key.UP))
        self.assertTrue(self.default_keybinds.key_is_bound(key.DOWN))
        self.assertTrue(self.default_keybinds.key_is_bound(key.LEFT))
        self.assertFalse(self.default_keybinds.key_is_bound(key.F7))

    def test_get_orders(self):
        self.assertEqual(self.default_keybinds.get_order(key.UP), ORDERS.UP)
        self.assertEqual(self.default_keybinds.get_order(key.RIGHT), ORDERS.RIGHT)
        self.assertEqual(self.default_keybinds.get_order(key.LEFT), ORDERS.LEFT)
        self.assertEqual(self.default_keybinds.get_order(key.F7), None)

    def test_bind_unbound_key(self):
        size = len(self.default_keybinds._binds)
        self.default_keybinds.bind_key(key.F7, ORDERS.UP)
        try:
            self.assertEqual(self.default_keybinds._binds[key.F7], ORDERS.UP)
        except KeyError as e:
            self.assertFalse(True, "binds[key.F7] threw a KeyError: {0}".format(e.message))
        self.assertEqual(size + 1, len(self.default_keybinds._binds))

    def test_bind_bound_key(self):
        size = len(self.default_keybinds._binds)
        self.default_keybinds.bind_key(key.UP, ORDERS.CONFIRM)
        self.assertEqual(self.default_keybinds._binds[key.UP], ORDERS.CONFIRM)
        self.assertEqual(size, len(self.default_keybinds._binds))

    def test_unbind_key_in_dict(self):
        size = len(self.default_keybinds._binds)
        self.assertTrue(self.default_keybinds.unbind_key(key.DOWN))
        try:
            self.default_keybinds._binds[key.DOWN]
            self.assertTrue(False, "key.DOWN is still in they dictionary!")
        except KeyError:
            pass
        self.assertEqual(size - 1, len(self.default_keybinds._binds))

    def test_unbind_key_not_in_dict(self):
        size = len(self.default_keybinds._binds)
        self.assertFalse(self.default_keybinds.unbind_key(key.F7))
        self.assertEqual(size, len(self.default_keybinds._binds))

suite = unittest.TestLoader().loadTestsFromTestCase(TestKeybinds)
unittest.TextTestRunner(verbosity=2).run(suite)