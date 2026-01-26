import json
import os

FILE_NAME = "submission/assignment/project/users.json"

# Load existing users or initialize empty data
if os.path.exists(FILE_NAME):
    with open(FILE_NAME, "r") as file:
        data = json.load(file)
else:
    data = {"users": []}

def login(username, password):
    for user in data["users"]:
        if user["username"] == username and user["password"] == password: # match username and password
            return True
    return False

def prompt_password(min_len=6):
    while True:
        pw = input(f"Choose a password (min {min_len} chars): ")
        if len(pw) >= min_len: # length check
            return pw
        print("Password too short! Try again.")

def register(username, password=None, min_len=6):
    # ask for password if not provided
    if password is None:
        password = prompt_password(min_len)

    # check duplicate username
    for user in data["users"]:
        if user["username"] == username:
            return False  # Username already exists

    # save user
    data["users"].append({"username": username, "password": password})
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)
    return True


def main():
    while True:
        choice = input("Type 'login', 'register', or 'exit': ").strip().lower()

        match choice:
            case "login":
                username = input("Username: ").strip()
                password = input("Password: ")
                print("Login successful" if login(username, password) else "Invalid username or password")

            case "register":
                username = input("Choose a username: ").strip()
                password = prompt_password(6)
                print("Registration successful" if register(username, password) else "Username already exists")

            case "exit":
                print("Bye!")
                break

            case _:
                print("Invalid choice")

main()