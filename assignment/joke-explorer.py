import sys
import json
import requests

API_URL_RANDOM = "https://official-joke-api.appspot.com/jokes/random"

jokes = []
favourites = []

def fetch_random_joke():
    global jokes
    try:
        response = requests.get(API_URL_RANDOM)
    except requests.RequestException:
        sys.exit("Error fetching data")
    data = response.json()
    print_joke(data)
    jokes.append(data)
    return data

def print_joke(joke):
    print(f"[{joke['id']}] ({joke['type']})")
    print(joke['setup'])
    print(joke['punchline'])

def fetch_many_jokes(times):
    global jokes
    for _ in range(times):
        data = fetch_random_joke()
        jokes.append(data)
    return jokes

def favourite(joke_id):
    joke_id = int(joke_id)
    for joke in jokes:
        if joke["id"] == joke_id:
            favourites.append(joke)
            return json.dumps(joke, indent=4)   # JSON OUTPUT
    return json.dumps({"error": "Joke not found"}, indent=4)

def main():
    print("Welcome to the Public API Joke Explorer!")
    print("Type 'help' to see available commands.")
    while True:
        cmd = input("> ")
        
        if cmd == "help":
            print("Commands: random, many <n>, fav <id>, listfav, quit")
        
        elif cmd == "random":
            fetch_random_joke()

        elif cmd.startswith("many"):
            _, n = cmd.split()
            fetch_many_jokes(int(n))

        elif cmd.startswith("fav"):
            _, joke_id = cmd.split()
            json_output = favourite(joke_id)
            print(f"Favourite added: ID {joke_id}")

        elif cmd.startswith("list"):
            for fav in favourites:
                print(f"[{fav['id']}] ({fav['type']})")
                print(fav['setup'])
                print(fav['punchline'])
                print()

        elif cmd == "quit":
            print("Goodbye!")
            break
        
        else:
            print("Unknown command. Type 'help' for options.")

if __name__ == "__main__":
    main()
