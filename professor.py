import random

def get_level():
    while True:
        try:
            n = int(input("Level (1, 2, or 3): "))
            if n in [1, 2, 3]:
                return n
            else:
                print("Invalid input. Please enter 1, 2, or 3.")
        except ValueError:
            print("Please enter a valid integer.")

def generate_integer(n):
    if n == 1:
        lower = 0
    else:
        lower = 10 ** (n - 1)
    upper = 10 ** n - 1
    return random.randint(lower, upper)

def main():
    level = get_level()
    score = 0
    num_problems = 10

    for _ in range(num_problems):
        x = generate_integer(level)
        y = generate_integer(level)
        correct_answer = x + y

        attempts = 0
        answered_correctly = False

        while attempts < 3 and not answered_correctly:
            try:
                user_input = input(f"{x} + {y} = ")
                user_answer = int(user_input)
                if user_answer == correct_answer:
                    score += 1
                    answered_correctly = True
                else:
                    print("EEE")
                    attempts += 1
            except ValueError:
                print("EEE")
                attempts += 1

        if not answered_correctly:
            print(f"{x} + {y} = {correct_answer}")

    print("Score:", score)

if __name__ == "__main__":
    main()