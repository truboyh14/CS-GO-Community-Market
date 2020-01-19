from Item import Item
import random
import math


class Crate:

    """Crate that contains a game item

    === Attributes ===
    name: name os this crate
    rarities: common(78%), rare(20%), legendary(2%)
    """
    name: str
    tier: int

    def __init__(self, name) -> None:
        """Initialize this crate
        """
        self.name = name

    def generate_item(self, tier) -> Item:
        """
        Generate a item of a certain tier.
        :param tier: tier of item
        :type tier: str
        :return: generated item
        :rtype: Item
        """
        if tier == 'legendary':
            draw = random.randrange(1, 5)
            return Item('L' + str(draw), tier)
        elif tier == 'rare':
            draw = random.randrange(1, 10)
            return Item('R' + str(draw), tier)
        else:
            draw = random.randrange(1, 20)
            return Item('C' + str(draw), tier)

    def unbox(self) -> Item:
        """
        open a crate with items
        :return: opened item
        :rtype: Item
        """
        draw = random.randrange(1, 101)
        if draw <= 2:
            return self.generate_item('legendary')
        elif draw <= 22:
            return self.generate_item('rare')
        else:
            return self.generate_item('common')


if __name__ == "__main__":

    """
    This example creates 20 crates and unboxes their contents and puts it on a list, it then prints the item details.
    """
    item_list = []
    for i in range(20):
        crate = Crate(str(i))
        item_list.append(crate.unbox())

    for i in item_list:
        print(i.details)
