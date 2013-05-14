__author__ = 'Travis Moy'


class CellImages:
    def __init__(self, cell, mobile=None, num_mobiles=0, tool=None, consumable=None, environmental=None):
        self.cell = cell
        self.mobile = mobile
        self.num_mobiles = num_mobiles
        self.tool = tool
        self.consumable = consumable
        self.environmental = environmental

        if self.mobile is not None:
            if self.num_mobiles < 1:
                self.num_mobiles = 1

    def __eq__(self, other):
        if other is None:
            return False
        return self.__dict__ == other.__dict__