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
        json = JSONCONVERTER.simple_to_json(kwt)
        jkwt = JSONCONVERTER.simple_to_custom_object(json)
        self.assertEqual(kwt.__dict__, jkwt.__dict__)

    def test_create_instance(self):
        template = TemplateEnvironmental.TemplateEnvironmental('environmental', _entity_name='test', _image_name='timg',
                                                               _max_hp=3)
        comp_env = Environmental.Environmental(0, 'lvl', _entity_name='test', _image_name='timg', _max_hp=3)
        instance = template.create_instance(0, 'lvl', None)
        del comp_env.entity_image
        del instance.entity_image
        self.assertEqual(comp_env.__dict__, instance.__dict__)

    def test_extra_args(self):
        template = TemplateEnvironmental.TemplateEnvironmental('door', _entity_name='door',
                                                               _open_image_location='cells/floor.png',
                                                               _closed_image_location='cells/wall.png',
                                                               _is_open=True)
        comp_env = EnvDoor.EnvDoor(0, None, _entity_name='door', _open_image_location='cells/floor.png',
                                   _closed_image_location='cells/wall.png', _is_open=True)
        json = JSONCONVERTER.simple_to_json(template)
        template = JSONCONVERTER.simple_to_custom_object(json)
        instance = template.create_instance(0, None, None)
        self.assertEqual(comp_env.entity_name, instance.entity_name)
        self.assertEqual(comp_env._open_image_location, instance._open_image_location)
        self.assertEqual(comp_env._closed_image_location, instance._closed_image_location)
        self.assertEqual(comp_env._is_open, instance._is_open)

    def test_vars_not_input_are_default(self):
        template = TemplateEnvironmental.TemplateEnvironmental('environmental')
        comp_env = Environmental.Environmental(0, None)
        instance = template.create_instance(0, None, None)
        del comp_env.entity_image
        del instance.entity_image
        self.assertEqual(comp_env.__dict__, instance.__dict__)

suite = unittest.TestLoader().loadTestsFromTestCase(TestTemplateEnvironmental)
unittest.TextTestRunner(verbosity=2).run(suite)