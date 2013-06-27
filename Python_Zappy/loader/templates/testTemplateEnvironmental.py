__author__ = 'Travis Moy'

import unittest
import loader.templates.TemplateEnvironmental as TemplateEnvironmental
import entity.environmentals.Environmental as Environmental
import entity.environmentals.EnvDoor as EnvDoor
from z_json import JSONCONVERTER


class KwargsTest(object):
    def __init__(self, _test_str='test_str_val', **kwargs):
        self._test_str = _test_str

       # This is super dumb.
        if '_additional_args' in kwargs:
            self._additional_args = kwargs['_additional_args']
        else:
            self._additional_args = kwargs


class TestTemplateEnvironmental(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_kwargs(self):
        kwt = KwargsTest(test0=0, test1=1)
        print "kwt.__dict__", kwt.__dict__
        json = JSONCONVERTER.simple_to_json(kwt)
        print "JSON of kwt", json
        jkwt = JSONCONVERTER.simple_to_custom_object(json)
        print "jkwt.__dict__", jkwt.__dict__
        self.assertEqual(kwt.__dict__, jkwt.__dict__)

        kwt1 = KwargsTest(_additional_args={'_additional_args': {'a': 13, 'b': 5}}, _asdf='asdf')
        print 'kwt1.__dict__', kwt1.__dict__

        kwt1 = KwargsTest(_a={'_zurg': {'a': 13, 'b': 5}}, _asdf='asdf')
        print 'kwt1.__dict__', kwt1.__dict__

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
                                   _closed_image_location='cells/wall.png', _is_open=True)
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