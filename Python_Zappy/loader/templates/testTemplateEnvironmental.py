__author__ = 'Travis Moy'

import unittest
import loader.templates.TemplateEnvironmental as TemplateEnvironmental
import entity.environmentals.Environmental as Environmental
import entity.environmentals.EnvCollapsible as EnvCollapsible


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

    def test_vars_not_input_are_default(self):
        template = TemplateEnvironmental.TemplateEnvironmental('environmental')
        comp_env = Environmental.Environmental('lvl')
        instance = template.create_instance('lvl', None)
        self.assertEqual(comp_env, instance)

suite = unittest.TestLoader().loadTestsFromTestCase(TestTemplateEnvironmental)
unittest.TextTestRunner(verbosity=2).run(suite)