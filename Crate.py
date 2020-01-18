import Item
import random
import math


class Crate:
    """Crate that contains a game item

    === Attributes ===
    name: name os this crate
    type: type of this crate
    tier: tier of this crate ranging from 1-3
    tier 1: common(78%), rare(20%), legendary(2%)
    tier 2: common(52%), rare(40%), legendary(8%)
    tier 3: common(22%), rare(60%), legendary(18%)
    containing: all list of items it might contain
    """
    name: str
    tier: int
    containing: [Item, Item, Item]

    def __init__(self, name, tier, containing) -> None:
        """Initialize this crate
        """
        self.name = name
        self.tier = tier
        self.containing = containing

    def unbox(self) -> Item:
        """
        open a crate with items
        :return: opened item
        :rtype: Item
        """
        draw = random.randrange(1, 100)
        if draw < 2 * (self.tier ** 2):
            return self.containing[0]
        elif draw < 20 * self.tier + 2 * (self.tier ** 2):
            return self.containing[1]
        else:
            return self.containing[2]
