__author__ = 'Travis Moy'

import unittest
import TemplateTool
import dummies.DummyTool


class TestTemplateTool(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_create_instance(self):
        template = TemplateTool.TemplateTool('dummy', 5, _energy_cost=2)
        dummy = dummies.DummyTool.DummyTool(_range=5, _level='lvl', _energy_cost=2)
        instance = template.create_instance(level='lvl', entity_index=None)
        self.assertEqual(dummy, instance)

    def test_create_instance_not_in_dict(self):
        template = TemplateTool.TemplateTool('zoo', 5, _energy_cost=2)
        instance = template.create_instance(level='lvl', entity_index=None)
        self.assertEqual(None, instance)

suite = unittest.TestLoader().loadTestsFromTestCase(TestTemplateTool)
unittest.TextTestRunner(verbosity=2).run(suite)