import requests


# Generate a key pair using P-256
def generate_ecdsa() -> list:
    url = "https://8gwifi.org/crypto/rest/ec/generatekpecdsa/prime256v1"
    r = requests.get(url).json()
    generated = [r["ecprivateKeyA"], r["ecpubliceKeyA"]]
    print(generated)
    return generated
