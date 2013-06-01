__author__ = 'Travis Moy'

import unittest
import os
import pyglet
import loaderExceptions
import LoaderEntityIndex
import dummies.DummyTemplate
from z_json import JSONCONVERTER


class TestLoaderEntityIndex(unittest.TestCase):
    PATH_TO_TEST_ENTITIES = "test_entities/"

    def setUp(self):
        self._default_level = None
        self._custom_loader = pyglet.resource.Loader('@loader')
        self._index = LoaderEntityIndex.LoaderEntityIndex(None)

        self.filename = 'test_file.json'
        self.template = dummies.DummyTemplate.DummyTemplate(name="Test", integer=10)
        json_string = JSONCONVERTER.simple_to_json(self.template)

        this_path = os.path.dirname(__file__) + '/' + self.PATH_TO_TEST_ENTITIES + self.filename
        file = open(this_path, 'w')
        file.write(json_string)
        file.close()

    def tearDown(self):
        self._default_level = None
        self._custom_loader = None
        self._index = None
        self.filename = None
        self.template = None

    # What happens if entity cannot be found?
    # Throw an exception, CouldNotFindJSONFile
    def test_load_entity_by_name(self):
        self._index._load_template_by_name(self.filename)
        self.assertTrue(self.filename in self._index._template_dict)
        self.assertEqual(self._index._template_dict[self.filename], self.template)

    def test_load_entity_by_name_cannot_find(self):
        threw = False
        try:
            self._index._load_template_by_name('no_such_file.json')
        except loaderExceptions.CouldNotFindJSONFile:
            threw = True
        self.assertTrue(threw, "_load_entity_by_name() did not throw the a CouldNotFindJSONFile exception when no such"
                               "file exists!")

    # What happens if entity cannot be found?
    # Throw an exception, CouldNotFindJSONFile
    def test_create_entity_by_name_not_loaded(self):
        self.assertEqual(self._index.create_entity_by_name(self.filename), self.template)

    def test_create_entity_by_name_loaded(self):
        self._index._load_template_by_name(self.filename)
        self.assertEqual(self._index.create_entity_by_name(self.filename), self.template)

    def test_create_entity_by_name_cannot_find(self):
        threw = False
        try:
            self._index.create_entity_by_name('no_such_file.json')
        except loaderExceptions.CouldNotFindJSONFile:
            threw = True
        self.assertTrue(threw, "create_entity_by_name() did not throw the a CouldNotFindJSONFile exception when no such"
                               "file exists!")

suite = unittest.TestLoader().loadTestsFromTestCase(TestLoaderEntityIndex)
unittest.TextTestRunner(verbosity=2).run(suite)
