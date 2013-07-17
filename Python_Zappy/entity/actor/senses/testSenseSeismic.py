__author__ = 'Travis Moy'

import unittest
import entity.actor.senses.SenseSeismic as SenseSeismic
import dummies.DummyLoaderEntityIndex
import loader.oldLoaderLevel


class TestSenseSeismic(unittest.TestCase):

    def setUp(self):
        self.loader_level = loader.oldLoaderLevel.oldLoaderLevel('loader/test_levels')
        self.loader_level._entity_index = dummies.DummyLoaderEntityIndex.DummyLoaderEntityIndex()
        self.level_view = self.loader_level.get_level(2).view
        self.sense = SenseSeismic.SenseSeismic(1)

    def tearDown(self):
        self.loader_level = None
        self.sense = None
        self.level_view = None

    def test_detect_entities(self):
        detected = self.sense.detect_entities(0, 0, self.level_view)
        self.assertEqual(len(detected), 2)
        detected = self.sense.detect_entities(1, 1, self.level_view)
        self.assertEqual(len(detected), 6)
        detected = self.sense.detect_entities(4, 2, self.level_view)
        self.assertEqual(len(detected), 0)

suite = unittest.TestLoader().loadTestsFromTestCase(TestSenseSeismic)
unittest.TextTestRunner(verbosity=2).run(suite)