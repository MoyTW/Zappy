__author__ = 'Travis Moy'

import unittest
import level.control.Command as cmd
import level.control.command_fragments as cf


class TestCommand(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_get_fragment_descriptions(self):
        dmg_e = cf.DamageEntity('src', 5, 'trg')
        command = cmd.Command("Blue Command!", cf.DamageEntity('src', 5, 'trg'))
        self.assertEqual([dmg_e.get_description(cmd.PRINT_BRIEF)], command.get_fragment_descriptions(cmd.PRINT_BRIEF))
        self.assertEqual([dmg_e.get_description(cmd.PRINT_NORMAL)], command.get_fragment_descriptions(cmd.PRINT_NORMAL))
        self.assertEqual([], command.get_fragment_descriptions(cmd.PRINT_VERBOSE))

suite = unittest.TestLoader().loadTestsFromTestCase(TestCommand)
unittest.TextTestRunner(verbosity=2).run(suite)
