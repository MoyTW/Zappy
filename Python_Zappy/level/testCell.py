__author__ = 'Travis Moy'

import unittest
import pyglet
import level.Cell


class DummyEntity(object):
    def __init__(self, image, priority):
        self._image = image
        self._priority = priority

    def get_image(self):
        return self._image

    def get_priority(self):
        return self._priority


class TestCell(unittest.TestCase):
    def setUp(self):
        pyglet.resource.path = ['@level.Cell', '.']
        pyglet.resource.reindex()

        self.teststr = "This is a test string!"
        self.default_image_path = 'test_images/defaultcell.png'
        self.floor_image_path = 'test_images/floor.png'
        self.default_image = pyglet.resource.image(self.default_image_path)
        self.floor_image = pyglet.resource.image(self.floor_image_path)

        self.default_cell = level.Cell.Cell(self.default_image_path)

    def tearDown(self):
        self.default_cell = None

    def test_load_image(self):
        self.assertEquals(self.default_image, self.default_cell._image)

        self.default_cell._load_image(self.floor_image_path)
        self.assertEquals(self.floor_image, self.default_cell._image)

    def test_get_cell_image(self):
        self.assertEquals(self.default_image, self.default_cell.get_cell_image())

    def test_get_passable(self):
        self.assertEquals(True, self.default_cell.get_passable())
        impassable = level.Cell.Cell(self.default_image_path, _passable=False)
        self.assertEquals(False, impassable.get_passable())

    def test_add_entity(self):
        self.default_cell.add_entity(self.teststr)
        self.assertEquals(len(self.default_cell._contains), 1)
        self.assertTrue(self.teststr in self.default_cell._contains)

    def test_remove_entity(self):
        self.default_cell.add_entity(self.teststr)
        self.assertTrue(self.default_cell.remove_entity(self.teststr))
        self.assertEquals(len(self.default_cell._contains), 0)
        self.assertTrue(self.teststr not in self.default_cell._contains)

        teststr2 = "Another test string!"
        self.assertFalse(self.default_cell.remove_entity(teststr2))
        self.assertEquals(len(self.default_cell._contains), 0)

    def test_contains_entity(self):
        self.assertFalse(self.default_cell.contains_entity(self.teststr))
        self.default_cell.add_entity(self.teststr)
        self.assertTrue(self.default_cell.contains_entity(self.teststr))

    # I'm an idiot. The Cell should return its own image as priority -1, as well.
    def test_get_display_images(self):
        dummy0 = DummyEntity("0", 0)
        dummy1 = DummyEntity("1", 5)
        dummy2 = DummyEntity("2", 2)
        dummy3 = DummyEntity("3", 2)

        self.default_cell.add_entity("This shouldn't trip it up!")
        self.default_cell.add_entity(dummy0)
        self.default_cell.add_entity(dummy1)
        self.default_cell.add_entity(dummy2)
        self.default_cell.add_entity(dummy3)

        display_map = self.default_cell.get_display_images()
        if display_map is None:
            self.assertFalse(True, "self.default_cell.get_display_images() is not returning anything!")

        self.assertEquals(len(display_map), 4)
        self.assertEquals(len(display_map.keys()), 4)
        try:
            self.assertEquals(display_map[-1][0], self.default_cell._image)
            self.assertEquals(display_map[0][0], dummy0._image)
            self.assertEquals(display_map[5][0], dummy1._image)
            self.assertEquals(display_map[2][0], dummy2._image)
            self.assertEquals(display_map[2][1], dummy3._image)
        except KeyError:
            self.assertFalse(True, "It's not fully populating the display_map! There's a missing entry!")


    def test_get_all_entities(self):
        self.assertEquals(self.default_cell._contains, self.default_cell.get_all_entities())

# Not currently using the code, but it's very nifty. I changed the structure, though, so it's invalid.
# Still, tossing it seems such a shame! Archived for possible future usage.
'''
from pyglet.window import key

    # It's running it twice - once near the beginning, and then once again. I don't know why.
    # I assume I have some fundamental misunderstanding of the unittest framework here...
    # You have to hit 'y' twice for it to register as passed - if you hit 'y' once and another key, it fails.
    def test_get_display_image(self):
        # Set up the cell here
        display_cell = level.Cell.Cell('test_images/floor.png')

        # Retrieve the image
        display_image = display_cell.get_display_image()
        # Check that it's not None
        self.assertTrue(display_image is not None)

        # Setup and create the viewing interface
        self.good = False
        width = 640
        height = 480

        self.window = pyglet.window.Window(width=width, height=height)

        labels = list()
        labels.append(pyglet.text.Label('TEST: Cell.get_display_image()', font_size=30, x=width // 2, y=height - 60,
                                        anchor_x='center', anchor_y='center'))
        labels.append(pyglet.text.Label('This screen will appear twice.', font_size=20, x=width // 2, y=height - 120,
                                        anchor_x='center', anchor_y='center'))
        labels.append(pyglet.text.Label("Press 'y' if the icon looks good.", font_size=20, x=width // 2, y=120,
                                        anchor_x='center', anchor_y='center'))
        labels.append(pyglet.text.Label('Press any other key if it does not.', font_size=20, x=width // 2, y=80,
                                        anchor_x='center', anchor_y='center'))

        @self.window.event
        def on_draw():
            sprite = pyglet.sprite.Sprite(display_image)
            sprite.set_position(width / 2 - 32, height / 2 - 32)
            sprite.draw()
            for label in labels:
                label.draw()

        @self.window.event
        def on_key_press(symbol, modifiers):
            if symbol == key.Y:
                self.good = True
            else:
                self.good = False
            pyglet.app.exit()

        pyglet.app.run()

        # Check to see if the viewer approves
        self.assertTrue(self.good)
'''

suite = unittest.TestLoader().loadTestsFromTestCase(TestCell)
unittest.TextTestRunner(verbosity=2).run(suite)