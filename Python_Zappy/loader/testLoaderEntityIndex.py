__author__ = 'Travis Moy'

import unittest
import LoaderEntityIndex
import pyglet


class TestLoaderEntityIndex(unittest.TestCase):
    PATH_TO_TEST_ENTITIES = "test_entities/"

    def setUp(self):
        self._default_level = None
        self._custom_loader = pyglet.resource.Loader('@loader')
        self._index = LoaderEntityIndex.LoaderEntityIndex(None)

    def tearDown(self):
        self._default_level = None
        self._custom_loader = None
        self._index = None

    def test_load_entity_by_name(self):
        self.assertTrue(False)

    # What happens if entity cannot be found?
    def test_create_entity_by_name(self):
        self.assertTrue(False)

suite = unittest.TestLoader().loadTestsFromTestCase(TestLoaderEntityIndex)
unittest.TextTestRunner(verbosity=2).run(suite)
