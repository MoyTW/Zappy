__author__ = 'Travis Moy'

import unittest
import zappyui.UIController


class DummyKeybinds(object):
    def __init__(self):
        self.binds = dict()
        self.binds['self'] = 'self_order'
        self.binds['new'] = 'new_order'
        self.binds['close'] = 'close_order'
        self.binds['complete'] = 'complete_order'

    def get_order(self, key):
        try:
            return self.binds[key]
        except KeyError:
            return None


class DummyScreen(object):
    def __init__(self, id):
        self.id = id

    def handle_order(self, order):
        if order == 'self_order':
            return self
        elif order == 'new_order':
            return DummyScreen(self.id + 1)
        elif order == 'complete_order':
            return True
        elif order == 'close_order':
            return None

    def close_on_child_completion(self):
        if self.id == 0 or self.id == 1:
            return False
        return True

    def __repr__(self):
        return "DummyScreen#{0}".format(self.id)


# I don't really know how to test the setup_callbacks() function.
# Also, how do I test draw()?
class TestUIController(unittest.TestCase):
    def setUp(self):
        self.none_controller = zappyui.UIController.UIController(None, DummyScreen(0), keybinds=DummyKeybinds())

    def tearDown(self):
        self.none_controller = None

    def test_handle_keys_screen_completion(self):
        self.none_controller._handle_keys('new', None)
        self.none_controller._handle_keys('new', None)
        self.none_controller._handle_keys('new', None)
        self.none_controller._handle_keys('new', None)
        self.none_controller._handle_keys('complete', None)
        self.assertEqual(len(self.none_controller._screen_history), 1)

    # I'm unsure how to test this, really. This is the best I can think of off the top of my head.
    def test_handle_keys(self):
        self.none_controller._handle_keys('new', None)
        self.assertEqual(len(self.none_controller._screen_history), 1)
        self.none_controller._handle_keys('close', None)
        self.assertEqual(len(self.none_controller._screen_history), 0)

        # Load it with a new one, to make sure something is in history.
        self.none_controller._handle_keys('new', None)

        previous_screen = self.none_controller._screen_head
        self.none_controller._handle_keys('self', None)
        self.assertEqual(previous_screen, self.none_controller._screen_head)

        previous_screen = self.none_controller._screen_head
        self.none_controller._handle_keys('should_do_nothing', None)
        self.assertEqual(previous_screen, self.none_controller._screen_head)

    def test_handle_new_screen(self):
        old_head = self.none_controller._screen_head
        self.assertEqual(len(self.none_controller._screen_history), 0, "The list is not empty to start with! What is "
                                                                       "this sorcery!?")
        self.none_controller._handle_new_screen("Blue!")
        self.assertEqual(len(self.none_controller._screen_history), 1)
        self.assertEqual(self.none_controller._screen_history[0], old_head)
        self.assertEqual(self.none_controller._screen_head, "Blue!")

    def test_close_head_screen(self):
        # To make sure it doesn't exit when the function is called.
        self.none_controller._screen_history.append("Filler!")
        self.none_controller._close_head_screen()
        self.assertEqual(self.none_controller._screen_head, "Filler!")
        self.assertEqual(len(self.none_controller._screen_history), 0)
        # I want to test that it attempts to call - or does call - pyglet.app.exit(). How would I do such a thing?

suite = unittest.TestLoader().loadTestsFromTestCase(TestUIController)
unittest.TextTestRunner(verbosity=2).run(suite)