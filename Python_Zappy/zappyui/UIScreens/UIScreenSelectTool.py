__author__ = 'Travis Moy'

import pyglet
import UIScreen
from zappyui.Orders import ORDERS


class UIScreenSelectTool(UIScreen.UIScreen):
    ASSETS_PATH = 'images/select_tool/'
    IMAGE_SIZE = 64
    GAP_SIZE = 16

    _border_batch = pyglet.graphics.Batch()
    _tools_batch = pyglet.graphics.Batch()

    def __init__(self, level_controller, viewport_info, factory_screens, selection=0):
        self._control = level_controller
        self._viewport = viewport_info
        self._factory = factory_screens
        self._selection = selection

        self._center_point = (viewport_info.width / 2, viewport_info.height / 2)

        self._tools_list = None
        self._init_tools(level_controller)

        self._sprites = list()
        self._init_images()
        self.gen_sprites()

    def _init_images(self):
        loader = pyglet.resource.Loader('@assets')
        self._center_border_image = loader.image("{0}center_border.png".format(self.ASSETS_PATH))
        self._single_border_image = loader.image("{0}single_border.png".format(self.ASSETS_PATH))
        self._left_border_image = loader.image("{0}left_border.png".format(self.ASSETS_PATH))
        self._right_border_image = loader.image("{0}right_border.png".format(self.ASSETS_PATH))

    def gen_sprites(self):
        self._sprites = list()

        num_tools = len(self._tools_list)
        leftmost_point = [0, 0]
        if num_tools % 2:  # Odd
            leftmost_point[0] = self._center_point[0] - (self.IMAGE_SIZE / 2) - \
                                ((self.IMAGE_SIZE + self.GAP_SIZE) * (num_tools / 2))
        else:  # Even
            leftmost_point[0] = self._center_point[0] - (self.GAP_SIZE / 2) - \
                                ((self.IMAGE_SIZE + self.GAP_SIZE) * (num_tools / 2))
        leftmost_point[1] = (self._viewport.height / 3) - self.IMAGE_SIZE

        for i in range(num_tools):
            tool = self._tools_list[i]
            tool_x = leftmost_point[0] + ((self.IMAGE_SIZE + self.GAP_SIZE) * i)
            tool_y = leftmost_point[1]
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

    def close_on_child_completion(self):
        return True

    def _select_tool(self):
        tool = self._tools_list[self._selection]
        return self._factory.create_ScreenUseTool(tool)

    def _move_selection(self, order):
        if order == ORDERS.LEFT:
            self._selection -= 1
            if self._selection < 0:
                self._selection = len(self._tools_list) - 1
        elif order == ORDERS.RIGHT:
            self._selection += 1
            if self._selection >= len(self._tools_list):
                self._selection = 0
        return self

    def _cancel(self):
        return None