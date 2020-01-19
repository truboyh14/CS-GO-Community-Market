class Item:
    """Game Item

    === Attributes ===
    name: name of this item
    tier: tier of this item
    description: description of this item
    example- "ruby", "gem", 2, "shiny red jewel"
    """
    name: str
    tier: int

    def __init__(self, name, tier) -> None:
        """Initialize this item
        """
        self.details = (name, tier)
