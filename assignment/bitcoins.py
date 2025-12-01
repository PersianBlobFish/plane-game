import sys
import requests


def main():
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")

    try:
        n = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

    api_key = "7c42ac5ba64243fffe399bbb7bb9e8159324ef6635283c0cc906cc90662eed1f"
    url = f"https://rest.coincap.io/v3/assets/bitcoin?apiKey={api_key}"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.RequestException:
        sys.exit("Error fetching Bitcoin price")


    try:
        data = response.json()
        price_usd = float(data["data"]["priceUsd"])
    except (KeyError, TypeError, ValueError):
        sys.exit("Unexpected response format")

    total = price_usd * n
    print(f"${total:,.4f}")

main()
