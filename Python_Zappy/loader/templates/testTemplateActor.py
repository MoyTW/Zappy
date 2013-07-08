__author__ = 'Travis Moy'

import unittest
import loader.LoaderEntityIndex as EntityIndex
import loader.templates.TemplateTool as TemplateTool
import loader.templates.TemplateActor as TemplateActor
import entity.actor.Actor as Actor
import entity.actor.senses as senses


class TestTemplateActor(unittest.TestCase):

    def setUp(self):
        template_tool_0 = TemplateTool.TemplateTool(_tool_class='tool', _range=5, _cooldown=0, _energy_cost=2,
                                                    _image_name=None)
        template_tool_None = TemplateTool.TemplateTool(_tool_class='blatooie', _range=5, _cooldown=0, _energy_cost=2,
                                                       _image_name=None)
        self.template_tools_list = [template_tool_0, template_tool_None]

    def tearDown(self):
        self.template_tools_list = None

    def test_user_is_set(self):
        template_actor = TemplateActor.TemplateActor(_tools=self.template_tools_list)
        created_actor = template_actor.create_instance(0, level=None, entity_index=EntityIndex.LoaderEntityIndex())
        try:
            self.assertEqual(created_actor._tools[0].user, created_actor)
        except IndexError:
            self.assertFalse(True, "created_actor.tools[0] is out of range!")

    def test_create_instance(self):
        max_moves = 2
        tools_list = self.template_tools_list
        sense_list = [senses.SenseSeismic.SenseSeismic(3)]
        image_name = 'image'
        level_parameter = None
        index = EntityIndex.LoaderEntityIndex()

        template_actor = TemplateActor.TemplateActor(_max_moves=max_moves, _tools=tools_list, _senses=sense_list,
                                                     _image_name=image_name)

        actor = Actor.Actor(0, _level=level_parameter, _max_moves=max_moves, _senses=sense_list, _image_name=image_name)

        actor_tools = index.create_tool_list(tools_list, actor, level_parameter)
        actor.init_tool_list(actor_tools)
        index.reset_entity_ids()

        created_actor = template_actor.create_instance(0, level=level_parameter, entity_index=index)

        if created_actor is None:
            self.assertTrue(False, "template_actor.create_instance is returning None!")

        self.assertEqual(actor._max_moves, created_actor._max_moves)
        self.assertEqual((actor._x, actor._y), (created_actor._x, created_actor._y))
        self.assertEqual(actor._senses[0], created_actor._senses[0])
        self.assertEqual(actor._image_name, created_actor._image_name)
        self.assertEqual(actor._level, created_actor._level)
        self.assertEqual(sorted(actor._tools), sorted(created_actor._tools))


suite = unittest.TestLoader().loadTestsFromTestCase(TestTemplateActor)
unittest.TextTestRunner(verbosity=2).run(suite)