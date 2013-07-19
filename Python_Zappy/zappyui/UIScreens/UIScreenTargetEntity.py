__author__ = 'Travis Moy'

import UIScreen
from zappyui.Orders import ORDERS
import pyglet


class UIScreenTargetEntity(UIScreen.UIScreen):
    ASSETS_PATH = 'images/target_entity/'
    IMAGE_SIZE = 64
    GAP_SIZE = 16
    FONT_SIZE = 24

    _border_batch = pyglet.graphics.Batch()
    _entity_batch = pyglet.graphics.Batch()

    def __init__(self, _entity_list, _tool, _camera, _level_controller, _viewport_info, _selection=0):
        self._camera = _camera
        self._entity_list = _entity_list
        self._tool = _tool
        self._control = _level_controller
        self._viewport = _viewport_info

        self._selection = _selection

        self._center_point = (self._viewport.width / 2, self._viewport.height / 2)

        self._sprites = list()
        self._leftmost_point = [0, 0]
        self._init_images()
        self._gen_sprites()

        self._selection_sprite = pyglet.sprite.Sprite(self._selection_image)
        self._selection_label = pyglet.text.Label("No Entity Selected",
                                                  font_size=self.FONT_SIZE,
                                                  y=self._leftmost_point[1] + self.IMAGE_SIZE + self.GAP_SIZE * 3)
        self._update_selection_sprite_and_text()

    def _on_activate(self):
        self._camera.disable_cursor()

    def _on_deactivate(self):
        self._camera.enable_cursor()

    def draw(self):
        if self._active:
            self._border_batch.draw()
            self._entity_batch.draw()
            self._selection_sprite.draw()
        self._selection_label.draw()

    def handle_order(self, order):
        if order == ORDERS.CANCEL:
            return self._cancel()
        elif ORDERS.is_direction(order):
            return self._move_selection(order)
        elif order == ORDERS.CONFIRM:
            return self._confirm_entity()
        else:
            return self

    def _cancel(self):
        return None

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
        self._selection_label.text = self._entity_list[self._selection].ent_name
        self._selection_label.x = self._center_point[0] - (self._selection_label.content_width / 2)

    def _gen_sprites(self):
        self._sprites = list()

        num_entities = len(self._entity_list)
        if num_entities % 2:  # Odd
            self._leftmost_point[0] = self._center_point[0] - (self.IMAGE_SIZE / 2) - \
                                     ((self.IMAGE_SIZE + self.GAP_SIZE) * (num_entities / 2))
        else:  # Even
            self._leftmost_point[0] = self._center_point[0] - (self.GAP_SIZE / 2) + self.GAP_SIZE - \
                                     ((self.IMAGE_SIZE + self.GAP_SIZE) * (num_entities / 2))
        self._leftmost_point[1] = (self._viewport.height - (self._viewport.height / 3))  # - self.IMAGE_SIZE

        for i in range(num_entities):
            entity = self._entity_list[i]
            entity_x = self._leftmost_point[0] + ((self.IMAGE_SIZE + self.GAP_SIZE) * i)
            entity_y = self._leftmost_point[1]
            border_x = entity_x - self.GAP_SIZE / 2
            border_y = entity_y - self.GAP_SIZE / 2
            self._sprites.append(pyglet.sprite.Sprite(entity.entity_image, x=entity_x, y=entity_y, batch=self._entity_batch))

            # Select which border and create
            if num_entities == 1:
                self._sprites.append(pyglet.sprite.Sprite(self._single_border_image, x=border_x, y=border_y,
                                                          batch=self._border_batch))
            elif i == 0:
                self._sprites.append(pyglet.sprite.Sprite(self._left_border_image, x=border_x, y=border_y,
                                                          batch=self._border_batch))
            elif i == num_entities - 1:
                self._sprites.append(pyglet.sprite.Sprite(self._right_border_image, x=border_x, y=border_y,
                                                          batch=self._border_batch))
            else:
                self._sprites.append(pyglet.sprite.Sprite(self._center_border_image, x=border_x, y=border_y,
                                                          batch=self._border_batch))

    def _confirm_entity(self):
        entity = self._entity_list[self._selection]
        if self._tool.can_use_on_entity(entity):
            self._control.zappy_use_tool_on_entity(self._tool, entity)
            return True
        else:
            print "CANNOT USE TOOL!"
            return self

    def _move_selection(self, order):
        if order == ORDERS.LEFT:
            self._selection -= 1
            if self._selection < 0:
                self._selection = len(self._entity_list) - 1
        elif order == ORDERS.RIGHT:
            self._selection += 1
            if self._selection >= len(self._entity_list):
                self._selection = 0
        self._update_selection_sprite_and_text()
        return self