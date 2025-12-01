from ast import match_case
import sys
import requests

API_URL = "https://api.coingecko.com/api/v3/simple/price"

def fetch_prices(coin_list):
    params = {"ids": ",".join(coin_list), "vs_currencies": "usd"}
    try:
        response = requests.get(API_URL, params=params)
    except requests.RequestException:
        sys.exit("Error fetching data")
    data = response.json()
    return data


def print_price(coin, prices): 
    print(f"{coin}: ${prices[coin]['usd']}")
    pass

def main():
    coins = ["bitcoin", "ethereum", "solana"]
    prices = fetch_prices(coins)
    track = []
    print("Welcome to the Crypto Price Tracker!")
    print("Type 'help' for commands.")
    while True:
        cmd = input("> ").strip()
        if cmd == "help":
            print("Commands: update, price <coin>, add <coin>, list, quit")
        elif cmd == "update":
            fetch_prices(coins)
            print("Updated current price")
            pass
        elif cmd.startswith("price"):
            i = cmd.split()[1]
            print_price(i, prices)
            pass
        elif cmd.startswith("add"):
            i = cmd.split()[1]
            print(f"Added {i}")
            track.append(i)
            # TODO: add the coin to tracking list and fetch price
            pass
        elif cmd == "list":
            print("Tracked coins:")
            for t in track:
                print_price(t,prices)
        elif cmd == "quit":
            print("Goodbye!")
            break
        else:
            print("Unknown command. Type 'help' for help.")
if __name__ == "__main__":
    main()