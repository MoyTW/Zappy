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

    def tearDown(self):
        pass

    # It's running it twice - once near the beginning, and then once again. I don't know why.
    # I assume I have some fundamental misunderstanding of the unittest framework here...
    def test_pyglet(self):
        self.good = False
        width = 640
        height = 480

        self.default_cell = level.Cell.Cell(image_file=self.default_image_path)
        self.window = pyglet.window.Window(width=width, height=height)

        labels = list()
        labels.append(pyglet.text.Label('This screen will appear twice.', font_size=20, x=width // 2, y=height - 40,
                                        anchor_x='center', anchor_y='center'))
        labels.append(pyglet.text.Label('Press y if the icon looks good.', font_size=20, x=width // 2, y=height - 80,
                                        anchor_x='center', anchor_y='center'))
        labels.append(pyglet.text.Label('Press any other key if it does not.', font_size=20,
                                        x=width // 2, y=height - 120, anchor_x='center', anchor_y='center'))

        @self.window.event
        def on_draw():
            sprite = pyglet.sprite.Sprite(self.default_cell._image)
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
        self.assertTrue(self.good)

suite = unittest.TestLoader().loadTestsFromTestCase(TestCell)
unittest.TextTestRunner(verbosity=2).run(suite)