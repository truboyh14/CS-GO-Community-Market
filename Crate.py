import Item
import random
class Crate:
    """Crate that contains a game item

    === Attributes ===
    name: name os this crate
    type: type of this crate
    tier: tier of this crate ranging from 1-3
    description: items it might contain
    """
    name: str
    type: str
    tier: int
    containing: [Item,Item,Item]

    def __init__(self, name, tier, type, containing) -> None:
        """Initialize this crate
        """
        self.name = name
        self.tier = tier
        self.type = type
        self.containing = containing

    def unbox(self) -> Item:
        random.randrange(start, stop[, step])





