__author__ = 'Travis Moy'

import unittest
import dummies.DummyTool
import TemplateTool
import TemplateActor
import entity.actor.Actor as Actor
import entity.actor.sense as senses


class TestTemplateActor(unittest.TestCase):

    def setUp(self):
        template_tool_0 = TemplateTool.TemplateTool(_tool_name='dummy', _range=5, _energy_cost=2)
        template_tool_None = TemplateTool.TemplateTool(_tool_name='blatooie', _range=5, _energy_cost=2)
        self.template_tools_list = [template_tool_0, template_tool_None]

    def tearDown(self):
        self.template_tools_list = None

    def test_create_tool_list(self):
        dummy_tool = dummies.DummyTool.DummyTool(_range=5, _energy_cost=2, _level=None)
        template_actor = TemplateActor.TemplateActor(5, _tools=self.template_tools_list)

        tool_list = template_actor._create_tool_list(None, None)
        if tool_list is None:
            self.assertEqual(False, "TemplateActor.create_tool_list() returned None!")
        self.assertEqual(len(tool_list), 1)
        self.assertEqual(dummy_tool, tool_list[0])

    def test_create_instance(self):
        max_moves = 2
        tools_list = self.template_tools_list
        sense_list = [senses.SenseSeismic.SenseSeismic(3)]
        image_name = 'image'
        level_parameter = None

        template_actor = TemplateActor.TemplateActor(_max_moves=max_moves, _tools=tools_list, _senses=sense_list,
                                                     _image_name=image_name)

        actor = Actor.Actor(level=level_parameter, max_moves=max_moves,
                            tools=template_actor._create_tool_list(level_parameter, None), senses=sense_list,
                            image_name=image_name)
        created_actor = template_actor.create_instance(level=level_parameter, entity_index=None)

        if created_actor is None:
            self.assertTrue(False, "template_actor.create_instance is returning None!")

        self.assertEqual(actor._max_moves, created_actor._max_moves)
        self.assertEqual((actor._x, actor._y), (created_actor._x, created_actor._y))
        self.assertEqual(actor._tools[0], created_actor._tools[0])
        self.assertEqual(actor._senses[0], created_actor._senses[0])
        self.assertEqual(actor._image_name, created_actor._image_name)
        self.assertEqual(actor._level, created_actor._level)


suite = unittest.TestLoader().loadTestsFromTestCase(TestTemplateActor)
unittest.TextTestRunner(verbosity=2).run(suite)