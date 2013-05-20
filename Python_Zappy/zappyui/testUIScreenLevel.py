__author__ = 'Travis Moy'

import unittest
import zappyui.UIScreenLevel


class TestUIScreenLevel(unittest.TestCase):
    pass

suite = unittest.TestLoader().loadTestsFromTestCase(TestUIScreenLevel)
unittest.TextTestRunner(verbosity=2).run(suite)