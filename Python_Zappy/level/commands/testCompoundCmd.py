__author__ = 'Travis Moy'

import unittest
import level.commands.CompoundCmd as cmd
import level.commands.Command as c


class DummyFragment(object):
    def __init__(self, description, wordiness, exec_func):
        self.description = description
        self.wordiness = wordiness
        self.exec_func = exec_func

    def execute(self, *args, **kwargs):
        self.exec_func(*args, **kwargs)

    def get_description(self, wordiness):
        if self.wordiness <= wordiness:
            return self.description


class TestCompoundCmd(unittest.TestCase):
    def setUp(self):

        self.cmd_twenty = cmd.CompoundCmd("Adds 10 and Multiplies by 2",
                                          DummyFragment("Adds 10", c.PRINT_DEBUG, lambda x: x.add(10)),
                                          DummyFragment("Multiplies by 2", c.PRINT_DEBUG, lambda x: x.mult(2)))

        self.cmd_ten = cmd.CompoundCmd("Multiplies by 2, adds 10",
                                       DummyFragment("Multiplies by 2", c.PRINT_DEBUG, lambda x: x.mult(2)),
                                       DummyFragment("Adds 10", c.PRINT_DEBUG, lambda x: x.add(10)))

    def tearDown(self):
        self.cmd_twenty = None
        self.cmd_ten = None

    def test_init(self):
        des_cmd = "This is a Compound Command!"
        cmd_test = cmd.CompoundCmd(des_cmd, 0, 1, 2, 3, 4)
        self.assertEqual(cmd_test.description, des_cmd)
        self.assertEqual(cmd_test.fragments, (0, 1, 2, 3, 4))

    def test_executes_in_order(self):
        class num(object):
            def __init__(self, v):
                self.v = v

            def add(self, n):
                self.v += n

            def mult(self, n):
                self.v *= n

        should_end_up_as_twenty = num(0)
        self.cmd_twenty.execute(should_end_up_as_twenty)
        self.assertEqual(should_end_up_as_twenty.v, 20)

        should_end_up_as_ten = num(0)
        self.cmd_ten.execute(should_end_up_as_ten)
        self.assertEqual(should_end_up_as_ten.v, 10)

    def test_get_description(self):
        self.assertEqual(self.cmd_ten.get_description(c.PRINT_BRIEF), "Multiplies by 2, adds 10")
        self.assertEqual(self.cmd_ten.get_description(c.PRINT_DEBUG),
                         "Multiplies by 2, adds 10\n\tMultiplies by 2\n\tAdds 10")

suite = unittest.TestLoader().loadTestsFromTestCase(TestCompoundCmd)
unittest.TextTestRunner(verbosity=2).run(suite)