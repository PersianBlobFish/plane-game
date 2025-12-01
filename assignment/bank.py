answer = input("Greeting: ").lower()

match(answer):
    case answer if answer.startswith("hello"):
        print("$0")
    case answer if answer.startswith("h"):
        print("$20")
    case _:
        print("$100")
