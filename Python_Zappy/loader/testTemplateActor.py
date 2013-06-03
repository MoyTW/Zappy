__author__ = 'Travis Moy'

import unittest
import dummies.DummyTool
import TemplateTool
import TemplateActor


class TestTemplateActor(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_create_tool_list(self):
        dummy_tool = dummies.DummyTool.DummyTool(_range=5, _energy_cost=2, _level=None)
        template_tool_0 = TemplateTool.TemplateTool(_tool_name='dummy', _range=5, _energy_cost=2)
        template_tool_None = TemplateTool.TemplateTool(_tool_name='blatooie', _range=5, _energy_cost=2)
        template_actor = TemplateActor.TemplateActor(5, _tools=[template_tool_None, template_tool_0])

        tool_list = template_actor._create_tool_list(None, None)
        if tool_list is None:
            self.assertEqual(False, "TemplateActor.create_tool_list() returned None!")
        self.assertEqual(len(tool_list), 1)
        self.assertEqual(dummy_tool, tool_list[0])

    def test_create_instance(self):
        self.assertTrue(False)

suite = unittest.TestLoader().loadTestsFromTestCase(TestTemplateActor)
unittest.TextTestRunner(verbosity=2).run(suite)