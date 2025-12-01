import random
from random import randint

level = int(input("Level: "))
guess = int(input("Guess: "))
answer = randint(1, level)
while True:
    if guess < answer:
        print("Too small!")
        guess = int(input("Guess: "))
    elif guess > answer:
        print("Too large!")
        guess = int(input("Guess: "))
    elif guess == answer:
        print("Just right!")
        break
    else:
        print("Invalid number")
        guess = int(input("Guess: "))