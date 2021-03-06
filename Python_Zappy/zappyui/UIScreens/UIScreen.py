__author__ = 'Travis Moy'

import warnings


class UIScreen(object):

    # handle_order handles, well, orders.
    #
    # There are 3 valid return values: self, new UIScreen subclass, and None.
    #
    # If fulfilling the order does not require it to change screens, it returns self.
    #
    # If by fulfilling the order it does it returns the new screen. For example, if the user is on the Level screen and
    # hits the Inventory button,it will return the Inventory screen. If the user is on the Menu screen and selects the
    # Keybindings screen, it'll return the Keybindings screen.
    #
    # If by fulfilling the order, the current screen is closed (exit Menu screen and return to Level for example), the
    # function should return None.
    def handle_order(self, order):
        warnings.warn("UIScreen.handle_order() was called! This shouldn't happen - something has gone horribly wrong!")
        return self

    def activate(self):
        self._active = True
        self._on_activate()

    def deactivate(self):
        self._active = False
        self._on_deactivate()

    def destruct_returns_screen(self):
        self._on_destruct()
        return self._on_destruct_return_screen()

    def _on_activate(self):
        pass

    def _on_deactivate(self):
        pass

    def _on_destruct(self):
        pass

    def _on_destruct_return_screen(self):
        pass

    def draw_if_not_head(self):
        return False

    def draw(self):
        warnings.warn("UIScreen.draw() was called! This shouldn't happen - something has gone horribly wrong!")

    def close_on_child_completion(self):
        return False