__author__ = 'Travis Moy'

import unittest
import loader.TemplateTool as TemplateTool
import entity.tool.Tool as Tool


class TestTemplateTool(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_create_instance(self):
        template = TemplateTool.TemplateTool('tool', _range=5, _cooldown=0, _energy_cost=2, _image_name=None)
        result = Tool.Tool('lvl', _list_target_types=list(), _range=5, _energy_cost=2, _cooldown=0, _image_name=None)
        instance = template.create_instance(level='lvl', entity_index=None)
        self.assertEqual(result, instance)

    def test_create_instance_not_in_dict(self):
        template = TemplateTool.TemplateTool('zoo', _range=0, _cooldown=0, _energy_cost=2, _image_name=None)
        instance = template.create_instance(level='lvl', entity_index=None)
        self.assertEqual(None, instance)

suite = unittest.TestLoader().loadTestsFromTestCase(TestTemplateTool)
unittest.TextTestRunner(verbosity=2).run(suite)