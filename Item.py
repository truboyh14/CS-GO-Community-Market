class Item:
    """Game Item

    === Attributes ===
    name: name of this item
    type: type of this item
    tier: tier of this item
    description: description of this item
    """
    name: str
    type: str
    tier: int
    description: str

    def __init__(self, name, type, tier, description) -> None:
        """Initialize this item
        """
        self.name = name
        self.type = type
        self.tier = tier
        self.description = description

