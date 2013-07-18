__author__ = 'Travis Moy'

import unittest
import loader.oldLoaderLevel
import entity.actor.Adversary as Adversary
import entity.actor.behaviors.BehaviorMoveStupid as BehaviorMoveStupid
import entity.actor.senses.SenseSeismic as SenseSeismic


class TestBehaviorMoveStupid(unittest.TestCase):

    def setUp(self):
        self.loader_level = loader.oldLoaderLevel.oldLoaderLevel('entity/actor/behaviors/behavior_test_levels')
        self.level = self.loader_level.get_level(0)
        self.adversary = Adversary.Adversary(99, self.level.view, _senses=[SenseSeismic.SenseSeismic(5)])
        self.behavior = BehaviorMoveStupid.BehaviorMoveStupid(_move_cost=1)

    def tearDown(self):
        self.loader_level = None
        self.level = None
        self.adversary = None
        self.behavior = None

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
        self.adversary.turn_begin()
        if not self.behavior._execute(self.level.player_actor.eid, self.level.view, self.adversary):
            print "Failed to move."
            return 0, 0

        cmpd_move_cmd = self.level.command_log[-2]
        new_x, new_y = cmpd_move_cmd[0].target
        print "(", x, y, ") -> (", new_x, new_y, ")"
        self.level.remove_entity_from(self.adversary, x, y)

        delta_x = new_x - x
        delta_y = new_y - y

        return delta_x, delta_y

suite = unittest.TestLoader().loadTestsFromTestCase(TestBehaviorMoveStupid)
unittest.TextTestRunner(verbosity=2).run(suite)