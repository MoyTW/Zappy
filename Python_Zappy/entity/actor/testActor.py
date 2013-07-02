__author__ = 'Travis Moy'

import unittest
import entity.actor.Actor as Actor
import entity.actor.effects.Effect as Effect
import entity.tool.Tool as Tool
import loader.oldLoaderLevel as LoaderLevel
from z_defs import DIR
import entity.actor.senses.SenseSeismic as SenseSeismic


class StunEffect(Effect.Effect):
    def apply(self):
        self._target.stun()
    def unapply(self):
        self._target.unstun()


class TestActor(unittest.TestCase):

    def setUp(self):
        self.loader = LoaderLevel.oldLoaderLevel('loader/test_levels')

    def tearDown(self):
        self.loader = None

    def test_turn_begin(self):
        actor = Actor.Actor(None, _max_energy=70, _energy_regen=5, _max_moves=5)
        actor._current_moves = 2
        actor._current_energy = 68

        effect = StunEffect(3, actor)
        actor.apply_status_effect(effect)

        actor.turn_begin()
        self.assertTrue(actor._stunned)
        self.assertEqual(actor._current_energy, 70)
        self.assertEqual(actor._current_moves, 5)

    def test_turn_end(self):
        tool = Tool.Tool(None, [])
        tool._turns_until_ready = 5
        actor = Actor.Actor(None, _tools=[tool])
        actor._stunned = True
        effect = Effect.Effect(5, actor)
        actor.apply_status_effect(effect)
        stuneffect = StunEffect(1, actor)
        actor.apply_status_effect(stuneffect)

        actor.turn_end()
        self.assertFalse(actor._stunned)
        self.assertEqual(tool._turns_until_ready, 4)
        self.assertEqual(effect._duration, 4)

    def test_inheritance(self):
        actor = Actor.Actor('blue', 2, _image_name='test_entity.png')
        self.assertEqual(actor._level, 'blue')
        self.assertEqual(actor.entity_image.width, 100)

    def test_detect_entities(self):
        level = self.loader.get_level(2)
        sense = SenseSeismic.SenseSeismic(1)
        actor = Actor.Actor(level, 1, _senses=[sense])
        level.place_entity_at(actor, 1, 1)

        actor.detect_entities()
        self.assertEqual(len(actor._detected_entities), 6)

        level.move_entity_from_to(actor, 1, 1, 4, 1)
        actor.detect_entities()
        self.assertEqual(len(actor._detected_entities), 0)

    '''
    def test_use_tool(self):
        tools = [DummyTool.DummyTool('0'), DummyTool.DummyTool('1')]
        actor = Actor.Actor(2, None, tools=tools)
        self.assertTrue(actor.use_tool_on(tools[0], (3, 5)))
        self.assertEqual(tools[0].use_on_called_with, (3, 5))
        self.assertFalse(actor.use_tool_on(DummyTool.DummyTool('3'), (1, 1)))
    '''

    def test_attempt_move(self):
        level = self.loader.get_level(4)
        actor = Actor.Actor(level, _max_moves=4)
        level.place_entity_at(actor, 1, 1)

        self.assertTrue(actor.attempt_move(DIR.N))
        self.assertEqual(actor._current_moves, 3)

        self.assertFalse(actor.attempt_move(DIR.N))
        self.assertEqual(actor._current_moves, 3)

        self.assertFalse(actor.attempt_move(DIR.E))
        self.assertEqual(actor._current_moves, 3)

        self.assertTrue(actor.attempt_move(DIR.S))
        self.assertEqual(actor._current_moves, 2)

        self.assertTrue(actor.attempt_move(DIR.E))
        self.assertEqual(actor._current_moves, 1)

        self.assertFalse(actor.attempt_move(DIR.S))
        self.assertEqual(actor._current_moves, 1)

        self.assertTrue(actor.attempt_move(DIR.W))
        self.assertEqual(actor._current_moves, 0)

        self.assertFalse(actor.attempt_move(DIR.N))

suite = unittest.TestLoader().loadTestsFromTestCase(TestActor)
unittest.TextTestRunner(verbosity=2).run(suite)