__author__ = 'Travis Moy'

import pyglet
import UIScreen
from zappyui.Orders import ORDERS


class UIScreenSelectTool(UIScreen.UIScreen):
    ASSETS_PATH = 'images/select_tool/'
    IMAGE_SIZE = 64
    GAP_SIZE = 16
    FONT_SIZE = 24

    _border_batch = pyglet.graphics.Batch()
    _tools_batch = pyglet.graphics.Batch()

    def __init__(self, _camera, level_controller, viewport_info, factory_screens, selection=0):
        self._camera = _camera
        self._control = level_controller
        self._viewport = viewport_info
        self._factory = factory_screens
        self._selection = selection

        self._center_point = (viewport_info.width / 2, viewport_info.height / 2)
        self.activate()

        self._tools_list = None
        self._init_tools(level_controller)

        self._sprites = list()
        self._leftmost_point = [0, 0]
        self._init_images()
        self._gen_sprites()

        self._selection_sprite = pyglet.sprite.Sprite(self._selection_image)
        self._selection_label = pyglet.text.Label("No Tool Selected",
                                                  font_size=self.FONT_SIZE,
                                                  y=self._leftmost_point[1] - self.GAP_SIZE * 3)
        self._update_selection_sprite_and_text()

    def handle_order(self, order):
        if order == ORDERS.LEFT or order == ORDERS.RIGHT:
            return self._move_selection(order)
        elif order == ORDERS.CONFIRM:
            return self._select_tool()
        elif order == ORDERS.CANCEL:
            return self._cancel()
        else:
            return self

    def draw(self):
        self._border_batch.draw()
        self._tools_batch.draw()
        if self._active:
            self._selection_sprite.draw()
        self._selection_label.draw()

    def activate(self):
        self._active = True
        self._camera.disable_cursor()

    def deactivate(self):
        self._active = False
        self._camera.enable_cursor()

    def close_on_child_completion(self):
        return True

    def draw_if_not_head(self):
        return True

    def _init_images(self):
        loader = pyglet.resource.Loader('@assets')
        self._selection_image = loader.image("{0}selection.png".format(self.ASSETS_PATH))
        self._center_border_image = loader.image("{0}center_border.png".format(self.ASSETS_PATH))
        self._single_border_image = loader.image("{0}single_border.png".format(self.ASSETS_PATH))
        self._left_border_image = loader.image("{0}left_border.png".format(self.ASSETS_PATH))
        self._right_border_image = loader.image("{0}right_border.png".format(self.ASSETS_PATH))

    def _update_selection_sprite_and_text(self):
        self._selection_sprite.x = self._leftmost_point[0] + ((self.IMAGE_SIZE + self.GAP_SIZE) * self._selection)
        self._selection_sprite.y = self._leftmost_point[1]
        self._selection_label.text = self._tools_list[self._selection].get_name()
        self._selection_label.x = self._center_point[0] - (self._selection_label.content_width / 2)

    def _gen_sprites(self):
        self._sprites = list()

        num_tools = len(self._tools_list)
        if num_tools % 2:  # Odd
            self._leftmost_point[0] = self._center_point[0] - (self.IMAGE_SIZE / 2) - \
                                     ((self.IMAGE_SIZE + self.GAP_SIZE) * (num_tools / 2))
        else:  # Even
            self._leftmost_point[0] = self._center_point[0] - (self.GAP_SIZE / 2) + self.GAP_SIZE - \
                                     ((self.IMAGE_SIZE + self.GAP_SIZE) * (num_tools / 2))
        self._leftmost_point[1] = (self._viewport.height / 3) - self.IMAGE_SIZE

        for i in range(num_tools):
            tool = self._tools_list[i]
            tool_x = self._leftmost_point[0] + ((self.IMAGE_SIZE + self.GAP_SIZE) * i)
            tool_y = self._leftmost_point[1]
            border_x = tool_x - self.GAP_SIZE / 2
            border_y = tool_y - self.GAP_SIZE / 2
            self._sprites.append(pyglet.sprite.Sprite(tool.get_image(), x=tool_x, y=tool_y, batch=self._tools_batch))

            # Select which border and create
            if num_tools == 1:
                self._sprites.append(pyglet.sprite.Sprite(self._single_border_image, x=border_x, y=border_y,
                                                          batch=self._border_batch))
            elif i == 0:
                self._sprites.append(pyglet.sprite.Sprite(self._left_border_image, x=border_x, y=border_y,
                                                          batch=self._border_batch))
            elif i == num_tools - 1:
                self._sprites.append(pyglet.sprite.Sprite(self._right_border_image, x=border_x, y=border_y,
                                                          batch=self._border_batch))
            else:
                self._sprites.append(pyglet.sprite.Sprite(self._center_border_image, x=border_x, y=border_y,
                                                          batch=self._border_batch))

    def _init_tools(self, level_controller):
        self._tools_list = level_controller.zappy_get_tools()

    def _select_tool(self):
        tool = self._tools_list[self._selection]
        return self._factory.create_ScreenTargetLocation(tool)

    def _move_selection(self, order):
        if order == ORDERS.LEFT:
            self._selection -= 1
            if self._selection < 0:
                self._selection = len(self._tools_list) - 1
        elif order == ORDERS.RIGHT:
            self._selection += 1
            if self._selection >= len(self._tools_list):
                self._selection = 0
        self._update_selection_sprite_and_text()
        return self

    def _cancel(self):
        return None