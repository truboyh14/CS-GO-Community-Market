import requests


def get_items() -> list:
    # Cache the items list from server to save time
    try:
        f = open('./items_list.txt', encoding="utf8")
        items = f.read().splitlines()

    # Retrieve from server if doesn't exist locally
    except FileNotFoundError:
        url = "http://csgobackpack.net/api/GetItemsList/v2"

        params = {"no_details": "true",
                  "no_prices": "true"}

        r = requests.get(url, params=params).json()
        items = list(r["items_list"].keys())

    return items
