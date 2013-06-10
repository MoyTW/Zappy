__author__ = 'Travis Moy'

import unittest
import loader.LoaderLevel
import entity.actor.Adversary as Adversary
import entity.actor.behaviors.BehaviorMoveStupid as BehaviorMoveStupid
import entity.actor.senses.SenseSeismic as SenseSeismic


class TestBehaviorMoveStupid(unittest.TestCase):

    def setUp(self):
        self.loader_level = loader.LoaderLevel.LoaderLevel('entity/actor/behaviors/behavior_test_levels')
        self.level = self.loader_level.get_level(0)
        self.adversary = Adversary.Adversary(self.level, senses=[SenseSeismic.SenseSeismic(5)])
        self.behavior = BehaviorMoveStupid.BehaviorMoveStupid()

    def tearDown(self):
        self.loader_level = None
        self.level = None
        self.adversary = None
        self.behavior = None

    def test_can_execute(self):
        self.assertTrue(self.behavior._can_execute(self.level, self.adversary))
        self.adversary.use_moves(self.adversary.get_current_moves())
        self.assertFalse(self.behavior._can_execute(self.level, self.adversary))

    def test_uses_movement_points(self):
        self.level.place_entity_at(self.adversary, 0, 0)
        self.adversary.detect_entities()
        start_moves = self.adversary.get_current_moves()
        self.assertTrue(self.behavior.attempt_to_execute(self.level, self.adversary))
        self.assertLess(self.adversary.get_current_moves(), start_moves)

    def test_execute(self):
        data = self._gen_test_data()
        for d in data:
            result = self.run_test_data(*d[0])
            self.assertEqual(result, d[1], "Data: {0} Result: {1}".format(d, result))

    # Data is: [(x, y), (expected_horizontal, expected_vertical)]
    def _gen_test_data(self):
        data = [
            [(1, 0), (0, 1)],
            [(3, 3), (-1, 0)],
            [(3, 4), (0, -1)],
            [(1, 3), (1, 0)],
            [(1, 4), (0, -1)],
            [(1, 1), (0, 0)],
            [(0, 1), (1, 0)],
            [(0, 0), (1, 0)]
        ]
        return data

    def run_test_data(self, x, y):
        self.level.place_entity_at(self.adversary, x, y)
        self.adversary.detect_entities()
        self.behavior._execute(self.level, self.adversary)
        new_x, new_y = self.adversary.get_coords()
        self.level.remove_entity_from(self.adversary, new_x, new_y)

        delta_x = new_x - x
        delta_y = new_y - y

        return delta_x, delta_y

suite = unittest.TestLoader().loadTestsFromTestCase(TestBehaviorMoveStupid)
unittest.TextTestRunner(verbosity=2).run(suite)