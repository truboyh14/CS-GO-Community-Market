from CSGOBackpackAPI import get_items
from random import randrange


def draw_a_random_item() -> str:
    items = get_items()

    lucky_number = randrange(len(items))

    return items[lucky_number]