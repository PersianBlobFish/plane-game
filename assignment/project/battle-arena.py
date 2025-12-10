import random
class Fighter:
    def __init__(self, name, max_hp, base_attack):
        self._name = name
        self._max_hp = max_hp
        self._hp = max_hp
        self._base_attack = base_attack
    def is_alive(self):
        return self._hp > 0
    def take_damage(self, amount):
        self._hp = max(0, self._hp - amount)
    def reset(self):
        self._hp = self._max_hp
    def attack(self, target):
        raise NotImplementedError("Override in subclass")
class Warrior(Fighter):
    def attack(self, target):
        damage = self._base_attack + random.randint(0, 5)
        target.take_damage(damage)
        print(f"{self._name} attacks {target._name} for {damage} damage!")
class Mage(Fighter):
    def attack(self, target):
        damage = self._base_attack + random.randint(5, 10)
        target.take_damage(damage)
        print(f"{self._name} casts a spell on {target._name} for {damage} damage!")
class Rogue(Fighter):
    def attack(self, target):
        damage = self._base_attack + random.randint(2, 7)
        target.take_damage(damage)
        print(f"{self._name} strikes {target._name} from the shadows for {damage} damage!")
def run_duel(f1, f2):
    f1.reset()
    f2.reset()
    print(f"\nDuel starts between {f1._name} and {f2._name}!")
    while f1.is_alive() and f2.is_alive():
        f1.attack(f2)
        if not f2.is_alive():
            print(f"{f2._name} has been defeated! {f1._name} wins!")
            break
        f2.attack(f1)
        if not f1.is_alive():
            print(f"{f1._name} has been defeated! {f2._name} wins!")
            break
def create_fighter():
    name = input("Enter fighter name: ")
    print("Choose fighter type:")
    print("1. Warrior")
    print("2. Mage")
    print("3. Rogue")
    choice = input("> ")
    if choice == "1":
        return Warrior(name, 100, 10)
    elif choice == "2":
        return Mage(name, 80, 12)
    elif choice == "3":
        return Rogue(name, 90, 11)
    else:
        print("Invalid choice.")
        return None
def main():
    fighters = []

    while True:
        print("\n1. Create fighter")
        print("2. List fighters")
        print("3. Start duel")
        print("4. Quit")
        choice = input("> ")

        if choice == "1":
            f = create_fighter()
            if f is not None:
                fighters.append(f)
                print(f"Fighter '{f._name}' created and added!")
        
        elif choice == "2":
            if not fighters:
                print("No fighters created yet.")
            else:
                for idx, fighter in enumerate(fighters):
                    print(f"{idx + 1}. {fighter._name} (HP: {fighter._max_hp}, Attack: {fighter._base_attack})")

        elif choice == "3":
            if len(fighters) < 2:
                print("You need at least 2 fighters to duel.")
                continue

            print("Choose first fighter:")
            for idx, f in enumerate(fighters):
                print(f"{idx + 1}. {f._name}")
            f1 = fighters[int(input("> ")) - 1]

            print("Choose second fighter:")
            for idx, f in enumerate(fighters):
                print(f"{idx + 1}. {f._name}")
            f2 = fighters[int(input("> ")) - 1]

            run_duel(f1, f2)

        elif choice == "4" or choice.lower() == "quit":
            print("Goodbye!")
            break
if __name__ == "__main__":
    main()