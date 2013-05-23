__author__ = 'Travis Moy'

import zappyui.UIScreens.UIScreen as UIScreen
import pyglet


# This is the Base screen, which is at the bottom of this history.
class UIScreenMenuBase(UIScreen.UIScreen):
    IMAGE_PATH = 'images/base_menu/'
    loader = pyglet.resource.Loader('[@assets]')
    background_image = loader.image(IMAGE_PATH + 'background.png')
    exit_image = loader.image('exit.png')
    levels_image = loader.image('levels.png')
    options_image = loader.image('options.png')
    player_image = loader.image('player.png')
    select_frame_image = loader.image('select_frame.png')

    def __init__(self, window_viewport, selection=1):
        self._viewport = window_viewport
        self._selection = selection

        self._center_pixel = (self._viewport.width / 2, self._viewport.height / 2)

    def _init_sprites(self):
        self._background_sprite = pyglet.sprite.Sprite(self.background_image, x=self._center_pixel[0] -
                                                       self.background_image.width / 2)

    def handle_order(self, order):
        pass

    def _change_selection(self, order):
        pass

    def draw(self):
        pass