import random

def main():
    name = input("Enter a name? ")
    if name.lower() == "harry" or name.lower() == "hermione" or name.lower() == "ron":
        print("Gryffindor")
    elif name.lower() == "draco":
        print("Slytherin")
    else:
        house = random.randint(1,4)
        if house == 1:
            print("Gryffindor")
        elif house == 2:
            print("Hufflepuff")
        elif house == 3:
            print("Ravenclaw")
        else:
            print("Slytherin")

main()