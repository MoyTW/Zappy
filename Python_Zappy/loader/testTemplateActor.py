__author__ = 'Travis Moy'

import unittest


class TestTemplateActor(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_create_sense(self):
        self.assertFalse(True)

    def test_create_tool(self):
        self.assertTrue(False)

    def test_create_instance(self):
        self.assertTrue(False)

suite = unittest.TestLoader().loadTestsFromTestCase(TestTemplateActor)
unittest.TextTestRunner(verbosity=2).run(suite)