import json


# Load JSON data
with open("submission/assignment/project/users.json", "r") as file:
    data = json.load(file)

def authenticate(username, password):
    for user in data["users"]:
        if user["username"] == username and user["password"] == password:
            return True
    return False

input_username = input("Username: ")
input_password = input("Password: ")

if authenticate(input_username, input_password):
    print("Login successful")
else:
    print("Invalid username or password")

def main(choice):
    match choice:
        case "login":
            input_username = input("Username: ")
            input_password = input("Password: ")
            if authenticate(input_username, input_password):
                print("Login successful")
            else:
                print("Invalid username or password")
        case _:
            print("Invalid choice")
