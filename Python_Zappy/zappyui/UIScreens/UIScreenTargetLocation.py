__author__ = 'Travis Moy'

import UIScreen
from zappyui.Orders import ORDERS
import entity.actor.Actor as Actor


class UIScreenTargetLocation(UIScreen.UIScreen):
    def __init__(self, _tool, _camera, _level_controller, _factory_screens):
        self._tool = _tool
        self._camera = _camera
        self._control = _level_controller
        self._factory = _factory_screens

        self._zappy = _level_controller.get_zappy()

        self._start_tile = self._camera.get_center_tile()

    def draw(self):
        self._camera.draw()

    def handle_order(self, order):
        if ORDERS.is_direction(order):
            return self._move_camera(order)
        elif order == ORDERS.CONFIRM:
            return self._select_target()
        elif order == ORDERS.CANCEL:
            return self._cancel()

    def close_on_child_completion(self):
        return True

    def _move_camera(self, order):
        self._camera.step(ORDERS.to_direction(order))
        return self

    def _cancel(self):
        self._camera.center_on(*self._start_tile)
        return None

    def _select_target(self):
        tar_x, tar_y = self._camera.get_center_tile()
        print "Attempted to target", self._camera.get_center_tile()

        if self._tool.can_use_on_location(tar_x, tar_y):
            self._control.zappy_use_tool_on_location(self._tool, tar_x, tar_y)
            return True
        elif self._tool.targets_entities() or self._tool.targets_actors():
            entity_list = self._control.get_entities_at(tar_x, tar_y)

            # First, weed out tools that aren't helpful
            if self._tool.targets_actors and not self._tool.targets_entities():
                entity_list = [x for x in entity_list if isinstance(x, Actor.Actor)]

            # Check to see if there are targets
            if entity_list is not None and len(entity_list) > 0:
                # Call the factory and return the new screen
                print "Entity List:", entity_list
            else:
                return self

        return self