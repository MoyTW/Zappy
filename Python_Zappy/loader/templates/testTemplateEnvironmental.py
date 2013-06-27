__author__ = 'Travis Moy'

import unittest
import loader.templates.TemplateEnvironmental as TemplateEnvironmental
import entity.environmentals.Environmental as Environmental
import entity.environmentals.EnvDoor as EnvDoor
from z_json import JSONCONVERTER

class TestTemplateEnvironmental(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_create_instance(self):
        template = TemplateEnvironmental.TemplateEnvironmental('environmental', _entity_name='test', _image_name='timg',
                                                               _max_hp=3)
        comp_env = Environmental.Environmental('lvl', _entity_name='test', _image_name='timg', _max_hp=3)
        instance = template.create_instance('lvl', None)
        self.assertEqual(comp_env, instance)

    def test_extra_args(self):
        template = TemplateEnvironmental.TemplateEnvironmental('door', _entity_name='door',
                                                               _open_image_location='cells/floor.png',
                                                               _closed_image_location='cells/wall.png',
                                                               _open=True)
        comp_env = EnvDoor.EnvDoor(None, _entity_name='door', _open_image_location='cells/floor.png',
                                   _closed_image_location='cells/wall.png', _open=True)
        json = JSONCONVERTER.simple_to_json(template)
        print "JSON BEFORE LOADING", json
        template = JSONCONVERTER.simple_to_custom_object(json)
        print "TEMPLATE", template.__dict__
        instance = template.create_instance(None, None)
        self.assertEqual(comp_env._entity_name, instance._entity_name)
        self.assertEqual(comp_env._open_image_location, instance._open_image_location)
        self.assertEqual(comp_env._closed_image_location, instance._closed_image_location)
        self.assertEqual(comp_env._is_open, instance._is_open)

    def test_vars_not_input_are_default(self):
        template = TemplateEnvironmental.TemplateEnvironmental('environmental')
        comp_env = Environmental.Environmental(None)
        instance = template.create_instance(None, None)
        self.assertEqual(comp_env, instance)

suite = unittest.TestLoader().loadTestsFromTestCase(TestTemplateEnvironmental)
unittest.TextTestRunner(verbosity=2).run(suite)