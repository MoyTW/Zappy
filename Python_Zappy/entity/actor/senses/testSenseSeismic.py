__author__ = 'Travis Moy'

import unittest
import entity.actor.senses.SenseSeismic as SenseSeismic
import loader.oldLoaderLevel


class HasEID(object):
    def __init__(self, eid=0):
        self.eid = eid
    def __eq__(self, other):
        try:
            return self.eid == other.eid
        except AttributeError:
            return False

class DummyLoaderEntityIndex(object):
    def create_entity_by_name(self, name, level):
        if name == 'TestObj':
            return HasEID(0)
        else:
            pass


class TestSenseSeismic(unittest.TestCase):

    def setUp(self):
        self.loader_level = loader.oldLoaderLevel.oldLoaderLevel('loader/test_levels')
        self.loader_level._entity_index = DummyLoaderEntityIndex()
        self.level_view = self.loader_level.get_level(2).view
        self.sense = SenseSeismic.SenseSeismic(1)

    def tearDown(self):
        self.loader_level = None
        self.sense = None
        self.level_view = None

    def test_detect_entities(self):
        detected = self.sense.detect_entities(0, 0, self.level_view)
        self.assertEqual(len(detected), 2)
        self.assertEqual(detected, [0, 0])
        detected = self.sense.detect_entities(1, 1, self.level_view)
        self.assertEqual(len(detected), 6)
        self.assertEqual(detected, [0, 0, 0, 0, 0, 0])
        detected = self.sense.detect_entities(4, 2, self.level_view)
        self.assertEqual(len(detected), 0)
        self.assertEqual(detected, [])

suite = unittest.TestLoader().loadTestsFromTestCase(TestSenseSeismic)
unittest.TextTestRunner(verbosity=2).run(suite)