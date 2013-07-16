__author__ = 'Travis Moy'

import entity.tool.Tool as Tool
import unittest
import os
import pyglet
import loader.loaderExceptions
import loader.LoaderEntityIndex
import dummies.DummyTemplate
from z_json import JSONCONVERTER
import entity.Entity
import loader.templates.TemplateTool as TemplateTool


class TestLoaderEntityIndex(unittest.TestCase):

    def setUp(self):
        self._default_level = None
        self._custom_loader = pyglet.resource.Loader('@loader')
        self._index = loader.LoaderEntityIndex.LoaderEntityIndex()
        self._index._loader = self._custom_loader
        self._default_entity = entity.Entity.Entity(0, self._default_level)

        self.filename = 'test_entities/test_file.json'
        self.template = dummies.DummyTemplate.DummyTemplate(name="Test", integer=10)
        json_string = JSONCONVERTER.simple_to_json(self.template)

        this_path = os.path.dirname(__file__) + '/' + self.filename
        f = open(this_path, 'w')
        f.write(json_string)
        f.close()

    def tearDown(self):
        self._default_level = None
        self._custom_loader = None
        self._index = None
        self._default_entity = None
        self.filename = None
        self.template = None

    def test_eid(self):
        self.assertEqual(self._index.create_entity_by_name("No Such Entity", self._default_level).eid, 0)
        self.assertEqual(self._index.create_entity_by_name("No Such Entity", self._default_level).eid, 1)

    def test_create_tool_list_template(self):
        tool_template = TemplateTool.TemplateTool('tool', _entity_name='test', _cooldown=5, _energy_cost=13)
        dummy_tool = Tool.Tool(-1, self._default_level, _entity_name='test', _cooldown=5, _energy_cost=13)

        tool_list = self._index.create_tool_list([tool_template], None, self._default_level)
        if tool_list is None:
            self.assertTrue(False, "TemplateActor.create_tool_list() returned None!")

        self.assertEqual(len(tool_list), 1)
        del dummy_tool.entity_image
        comp_tool = tool_list[0]
        del comp_tool.entity_image
        self.assertEqual(dummy_tool.__dict__, comp_tool.__dict__)

    def test_create_tool_list_name(self):
        dummy_tool = Tool.Tool(-1, self._default_level, _entity_name="Test", _cooldown=9, _energy_cost=9)

        tool_list = self._index.create_tool_list(['test_entities/TestTool.json'], None, self._default_level)
        if tool_list is None:
            self.assertTrue(False, "TemplateActor.create_tool_list() returned None!")

        self.assertEqual(len(tool_list), 1)
        del dummy_tool.entity_image
        comp_tool = tool_list[0]
        del comp_tool.entity_image
        self.assertEqual(dummy_tool.__dict__, comp_tool.__dict__)

    def test_load_entity_by_name(self):
        try:
            self._index._load_template_by_name(self.filename)
        except loader.loaderExceptions.CouldNotFindJSONFile as e:
            self.assertFalse(True, e.message)
        self.assertTrue(self.filename in self._index._template_dict)
        self.assertEqual(self._index._template_dict[self.filename], self.template)

    # If it cannot be found, load None into the dict
    def test_load_entity_by_name_cannot_find(self):
        self._index._load_template_by_name('no_such_file.json')
        self.assertEqual(self._index._template_dict['no_such_file.json'], None)

    def test_create_entity_by_name_not_loaded(self):
        self.assertEqual(self._index.create_entity_by_name(self.filename, None), self.template.__repr__())

    def test_create_entity_by_name_loaded(self):
        self._index._load_template_by_name(self.filename)
        self.assertEqual(self._index.create_entity_by_name(self.filename, None), self.template.__repr__())

    # Creates a default entity
    def test_create_entity_by_name_cannot_find(self):
        try:
            created_entity = self._index.create_entity_by_name('no_such_file.json', None)
            self.assertEqual(created_entity._image_name, self._default_entity._image_name)
            self.assertEqual(created_entity._level, self._default_entity._level)
        except AttributeError:
            self.assertFalse("create_entity_by_name() is returning None.")

suite = unittest.TestLoader().loadTestsFromTestCase(TestLoaderEntityIndex)
unittest.TextTestRunner(verbosity=2).run(suite)
