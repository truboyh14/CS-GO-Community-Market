from collections import Counter

import requests

from Item import draw_a_random_item

myApiKey = "3e24c1f2-4db1-4820-a868-e8e763d3988d"
origin = "https://api.todaqfinance.net"
headers = {"Content-Type": "application/json",
           "x-api-key": myApiKey}


# Get a list of all the accounts
def get_accounts() -> list:
    url = origin + "/accounts"
    # page starts at 1
    page = 1

    params = {"filter[active]": "true",
              "page": page,
              "limit": 10000}

    total = []
    while True:
        r = requests.get(url, params=params, headers=headers).json()
        for user in r["data"]:
            if user["attributes"]["admin-email"] == "truman@example.com":
                total.append(user["id"])

        if "next" not in r["links"]:
            return total
        else:
            page += 1
            params["page"] = page


# Return the dictionary of items to quantity that owned by the account
def get_files_from_account(account: str) -> dict:
    url = origin + "/accounts/" + account + \
          "/files?page=1&limit=10"
    response = requests.get(url, headers=headers).json()

    items = {}

    if "errors" in response:
        raise Exception("%s: %s" % (response["errors"][0]["status"], response["errors"][0]["detail"]))

    for file in response["data"]:
        if "id" not in file["attributes"]["payload"] or \
                file["attributes"]["payload"]["id"] is None or type(
            file["attributes"]["payload"]["id"]) == int or len(
            file["attributes"]["payload"]["id"]) == 36:
            # Ignore the accounts that are not associated to our marketplace
            break
        elif file["attributes"]["payload"]["id"] in items:
            items[file["attributes"]["payload"]["id"]] += 1

        else:
            items[file["attributes"]["payload"]["id"]] = 1

    return items


# TODO
def get_transactions_from_account(account: str) -> dict:
    url = origin + "/accounts/" + account + "/transactions?page=1&limit=10000"

    response = requests.get(url, headers=headers).json()

    items = {}

    for file in response["data"]:
        if "id" not in file["attributes"]["payload"] or \
                file["attributes"]["payload"]["id"] is None or type(
            file["attributes"]["payload"]["id"]) == int or len(
            file["attributes"]["payload"]["id"]) == 36:
            # Ignore the accounts that are not associated to our marketplace
            break
        elif file["attributes"]["payload"]["id"] in items:
            items[file["attributes"]["payload"]["id"]] += 1

        else:
            items[file["attributes"]["payload"]["id"]] = 1

    return items


# !!Inefficient
def get_all_files() -> dict:
    total = Counter({})

    accounts = get_accounts()
    for account in accounts:
        a = Counter(get_files_from_account(account))
        total = total + a

    return total


# Create an account and return its account id
def create_account() -> str:
    url = origin + "/accounts"

    data = {
        "type": "account",
        "data": {
            "attributes": {
                "account-type": "individual",
                "admin-email": "truman@example.com",
                "contact": {
                    "last-name": "anonymous",
                    "first-name": "anonymous"
                }
            }
        }
    }
    r = requests.post(url, json=data, headers=headers).json()
    account_id = r["data"][0]["id"]
    print(account_id)
    return account_id


# We initialize a new account by randomly adding 5 items
def account_initialization() -> str:
    account_id = create_account()
    for i in range(5):
        create_item(draw_a_random_item(), account_id)


def create_item(item: str, owner: str) -> None:
    url = origin + "/files"

    payload = "{    \"data\": {    \"type\":\"file\",    " \
              "\"attributes\":{    \"payload\":{     \"id\": \"" + item + "\", " \
                                                                          "\"type\": \"loyalty-token\", \"member-type\": \"gold\"    },   " \
                                                                          "\"metadata\": {}},    \"relationships\":{    \"initial-account\":{    \"data\":{    \"type\":\"account\",    \"id\":\"" + owner + "\"    }    }  }    }} "

    response = requests.post(url, data=payload.encode('utf-8'), headers=headers)

    print(response.json())


if __name__ == "__main__":
    recipient = "3c8263ec-fc26-4186-85c2-2f91c7d1762f"
    # get_accounts()
    # account_initialization()
    # create_item("Sticker | OpTic Gaming (Holo) | Cologne 2016", recipient)
    # get_files_from_account(recipient)
    # get_all_files()
# get_files_from_account("AFDFSD")
