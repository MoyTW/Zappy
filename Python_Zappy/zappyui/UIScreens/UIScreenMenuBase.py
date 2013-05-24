__author__ = 'Travis Moy'

import zappyui.UIScreens.UIScreen as UIScreen
import pyglet
from zappyui.Orders import ORDERS


# This is the Base screen, which is at the bottom of this history.
class UIScreenMenuBase(UIScreen.UIScreen):
    ASSETS_PATH = 'images/base_menu/'
    BUTTON_DISTANCE = 65

    def __init__(self, window_viewport, selection=1):
        self._viewport = window_viewport
        self._selection = selection
        self._possible_selections = ['player', 'levels', 'options', 'exit']

        self._center_pixel = (self._viewport.width / 2, self._viewport.height / 2)

        self._init_images()
        self._init_sprites()

    # Must be called before _init_sprites
    def _init_images(self):
        loader = pyglet.resource.Loader(['@assets'])
        self.background_image = loader.image(self.ASSETS_PATH + 'background.png')
        self.select_frame_image = loader.image(self.ASSETS_PATH + 'select_frame.png')

        self.button_images = list()
        self.button_images.append(loader.image(self.ASSETS_PATH + 'player.png'))
        self.button_images.append(loader.image(self.ASSETS_PATH + 'levels.png'))
        self.button_images.append(loader.image(self.ASSETS_PATH + 'options.png'))
        self.button_images.append(loader.image(self.ASSETS_PATH + 'exit.png'))

    # Must be called after _init_images
    def _init_sprites(self):
        self._background_sprite = pyglet.sprite.Sprite(self.background_image,
                                                       x=self._center_pixel[0] - self.background_image.width / 2,
                                                       y=self._center_pixel[1] - self.background_image.height / 2)

        self._static_sprites = list()
        offset = -1
        for image in self.button_images:
            self._static_sprites.append(pyglet.sprite.Sprite(image,
                                                             x=self._center_pixel[0] - image.width / 2,
                                                             y=self._center_pixel[1] - image.height / 2 -
                                                             self.BUTTON_DISTANCE * offset))
            offset += 1

        self._selection_sprite = pyglet.sprite.Sprite(self.select_frame_image,
                                                      x=self._center_pixel[0] - self.select_frame_image.width / 2,
                                                      y=self._center_pixel[1] - self.select_frame_image.height / 2)

    def handle_order(self, order):
        if order == ORDERS.UP or order == ORDERS.DOWN:
            return self._change_selection(order)
        return self

    def _change_selection(self, order):
        if order == ORDERS.UP:
            self._selection -= 1
            if self._selection < 0:
                self._selection = len(self._possible_selections) - 1
        elif order == ORDERS.DOWN:
            self._selection += 1
            print len(self._possible_selections)
            if self._selection >= len(self._possible_selections):
                self._selection = 0
        self._reposition_selection_sprite()
        return self

    def _reposition_selection_sprite(self):
        y = self._center_pixel[1] - self.select_frame_image.height / 2 + self.BUTTON_DISTANCE
        y -= self._selection * self.BUTTON_DISTANCE
        self._selection_sprite.y = y

    def draw(self):
        self._background_sprite.draw()
        for sprite in self._static_sprites:
            sprite.draw()
        self._selection_sprite.draw()