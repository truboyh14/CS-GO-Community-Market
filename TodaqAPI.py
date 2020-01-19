import requests

myApiKey = "3e24c1f2-4db1-4820-a868-e8e763d3988d"
origin = "https://api.todaqfinance.net"
headers = {"Content-Type": "application/json",
           "x-api-key": myApiKey}


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


def create_account() -> None:
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
    print(r)


if __name__ == "__main__":
    get_accounts()
