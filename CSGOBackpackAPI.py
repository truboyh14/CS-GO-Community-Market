import requests


# Get the information of in-game items in CS:GO through
# http://CSGOBackpack.net REST API
def get_items() -> list:
    # Attempt to retrieve created list from workspace
    try:
        f = open('./items_list.txt', encoding="utf8")
        items = f.read().splitlines()

    # Retrieve from server if doesn't exist on workspace
    except FileNotFoundError:
        url = "http://csgobackpack.net/api/GetItemsList/v2"

        params = {"no_details": "true",
                  "no_prices": "true"}

        r = requests.get(url, params=params).json()
        items = list(r["items_list"].keys())

    return items
