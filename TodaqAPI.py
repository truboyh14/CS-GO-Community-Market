import requests

myApiKey = "3e24c1f2-4db1-4820-a868-e8e763d3988d"
origin = "https://api.todaqfinance.net"
headers = {"Content-Type": "application/json",
           "x-api-key": myApiKey}


def accounts() -> None:
    url = origin + "/accounts"
    # page starts at 1
    page = 1

    params = {"filter[active]": "true",
              "page": page,
              "limit": 10}
    while True:
        r = requests.get(url, params=params, headers=headers).json()
        for user in r["data"]:
            print("%s %s: %s" % (user["attributes"]["contact"]["first-name"],
                                 user["attributes"]["contact"]["last-name"],
                                 user["id"]))

        if "next" not in r["links"]:
            break
        else:
            page += 1
            params["page"] = page
            print(params)


def create(last_name: str, first_name: str) -> None:
    url = origin + "/accounts"
    data = {
        "type": "account",
        "data": {
            "attributes": {
                "account-type": "individual",
                "admin-email": "truman@example.com",
                "contact": {
                    "last-name": last_name,
                    "first-name": first_name
                }
            }
        }
    }
    r = requests.post(url, json=data, headers=headers).json()
    print(r)


if __name__ == "__main__":
    create("Morrison", "Scott")
