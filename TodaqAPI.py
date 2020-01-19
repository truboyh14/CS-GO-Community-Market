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
            total.append(user["id"])

        if "next" not in r["links"]:
            print(total)
            return total
        else:
            page += 1
            params["page"] = page


def get_files(account: str) -> None:
    url = "https://api.todaqfinance.net/accounts/" + account + \
          "/files?page=1&limit=10000"
    response = requests.get(url, headers=headers)

    print(response.json())


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

    get_files(recipient)
