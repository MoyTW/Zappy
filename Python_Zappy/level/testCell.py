__author__ = 'Travis Moy'

import unittest
import pyglet
import level.Cell
from pyglet.window import key


class TestCell(unittest.TestCase):
    def setUp(self):
        pyglet.resource.path = ['@level.Cell', '.']
        pyglet.resource.reindex()

        self.default_image_path = 'test_images/defaultcell.png'
        self.floor_image_path = 'test_images/floor.png'
        self.default_image = pyglet.resource.image(self.default_image_path)
        self.floor_image = pyglet.resource.image(self.floor_image_path)

        self.default_cell = level.Cell.Cell(self.default_image_path)

    def tearDown(self):
        pass

    def test_load_image(self):
        self.assertEquals(self.default_image, self.default_cell._image)

        self.default_cell._load_image(self.floor_image_path)
        self.assertEquals(self.floor_image, self.default_cell._image)

    def test_get_cell_image(self):
        self.assertEquals(self.default_image, self.default_cell.get_cell_image())

    def test_get_passable(self):
        self.assertEquals(True, self.default_cell.get_passable())
        impassable = level.Cell.Cell(passable=False)
        self.assertEquals(False, impassable.get_passable())

    def test_add_entity(self):
        self.assertFalse(True)

    def test_remove_entity(self):
        self.assertFalse(True)

    def test_contains_entity(self):
        self.assertFalse(True)

    def test_get_all_cell_images(self):
        self.assertFalse(True)

    def test_get_all_entities(self):
        self.assertFalse(True)

# Not currently using the code, but it's very nifty. I changed the structure, though, so it's invalid.
# Still, tossing it seems such a shame! Archived for possible future usage.
'''
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