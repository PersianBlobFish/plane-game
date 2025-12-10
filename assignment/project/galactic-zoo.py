state = {
    'day': 1,
    'max_day': 7,
    'credits': 100,
    'creatures': {
        'slime': 2,
        'raptor': 1,
        'phoenix': 1
    },
    'hunger':{ # hunger level 0 (full) to 3 (starving)
        'slime': 1,
        'raptor': 2,
        'phoenix': 0
    },
    'dirtiness':{ # dirt level 0 (clean) to 3 (filthy)
        'slime': 1,
        'raptor': 1,
        'phoenix': 0
    },
    'target_creatures': 20,
    'target_credits': 500
}

action = 1

def help():
    print("Available commands:")
    print("1. show status - Display current day, credits, and creatures.")
    print("2. show creatures - List all creatures in the zoo.")
    print("3. feed [creature] - Feed a specific creature to reduce hunger.")
    print("4. clean [creature] - Clean a specific creature to reduce dirtiness.")
    print("5. buy [creature] - Add a new creature to the zoo.")
    print("6. breed [creature] - Breed a specific creature to increase its count.")
    print("7. sell [creature] - Sell a creature for credits.")
    print("8. help - Show this help message.")
    print("9. quit - Exit the game.")

def total_creatures():
    return sum(state['creatures'].values())

def show_status():
    print(f"Day: {state['day']}/{state['max_day']}")
    print(f"Credits: {state['credits']}")
    print(f"Hunger Levels: {state['hunger']}")
    print(f"Dirtiness Levels: {state['dirtiness']}")    
    print(f"Total Creatures: {total_creatures()}/{state['target_creatures']}")

def show_creature():
        if not state['creatures']:
            print("You have no creatures.")
            return
        print("Creatures in the zoo:")
        for creature, count in state['creatures'].items():
            hunger = state['hunger'].get(creature, 0)
            dirt = state['dirtiness'].get(creature, 0)
            print(f"- {creature}: {count} (Hunger: {hunger}, Dirtiness: {dirt})")

def feed_creature(creature):
    if creature in state['creatures'] and state['creatures'][creature] > 0:
        if state['hunger'][creature] > 0:
            state['hunger'][creature] += 2
            print(f"You fed a {creature}. Hunger level is now {state['hunger'][creature]}.")
        else:
            print(f"The {creature} is already full.")
    else:
        print(f"You don't have any {creature}s.")

def clean_habitat(creature):
    if creature in state['creatures'] and state['creatures'][creature] > 0:
        if state['dirtiness'][creature] > 0:
            state['dirtiness'][creature] += 1
            print(f"You cleaned a {creature}. Dirtiness level is now {state['dirtiness'][creature]}.")
        else:
            print(f"The {creature} is already clean.")
    else:
        print(f"You don't have any {creature}s.")

def buy_creature(creature):
    creature_costs = {
        'slime': 50,
        'raptor': 200,
        'phoenix': 500
    }
    if creature in creature_costs:
        cost = creature_costs[creature]
        if state['credits'] >= cost:
            state['credits'] -= cost
            state['creatures'][creature] = state['creatures'].get(creature, 0) + 1
            state['hunger'][creature] = state['hunger'].get(creature, 0)
            state['dirtiness'][creature] = state['dirtiness'].get(creature, 0)
            print(f"You bought a {creature}.")
        else:
            print("Not enough credits to buy that creature.")
    else:
        print("Unknown creature type.")

def breed_creature(creature):
    if creature in state['creatures'] and state['creatures'][creature] >= 2:
        if creature in state['hunger'] and state['hunger'][creature] < 2:
            state['creatures'][creature] += 1
            state['hunger'][creature] -= 1 # breeding makes them a bit hungrier
            print(f"You bred a {creature}. You now have {state['creatures'][creature]} {creature}s.")
        else:
            print(f"The {creature}s are too hungry to breed. Feed them first.")
    else:
        print(f"You need at least 2 {creature}s to breed.")

def sell_creature(creature):
    sell_prices = {
        'slime': 30,
        'raptor': 150,
        'phoenix': 400
    }
    if creature in state['creatures'] and state['creatures'][creature] > 0:
        price = sell_prices.get(creature, 0)
        state['credits'] += price
        state['creatures'][creature] -= 1
        print(f"You sold a {creature} for {price} credits.")
    else:
        print(f"You don't have any {creature}s to sell.")

def endday():
    print(f"The sun has settled down and the day has come to an end! Day: {state['day']}")
    state ['day'] += 1
    if any(value == 0 for value in state['hunger'].values()):
        print(f"You have been penalized (-100 credit) for letting your creature starves. Remaining credit:{state['credits']}")
        state['credits'] -= 100
    else:
        state['hunger']['slime','raptor','phoenix'] -= 1
    
def main():
    print("Welcome to Galactics Zoos")
    help()
    while True:
        global action
        command = input("> ").strip().lower()
        if state['credits'] < 0:
            print("Your zoo had been bankrupted.")
            break
        if action == 5:
            endday()
            action = 1
        if command.startswith("feed "):
            creature = command.split()[1]
            feed_creature(creature)
            action += 1
        elif command.startswith("clean "):
            creature = command.split()[1]
            clean_habitat(creature)
            action = action + 1
        elif command.startswith("buy "):
            creature = command.split()[1]
            buy_creature(creature)
            action += 1
        elif command.startswith("breed "):
            creature = command.split()[1]
            print (creature)
            breed_creature(creature)
            action += 1
        elif command.startswith("sell "):
            creature = command.split()[1]
            sell_creature(creature)
            action += 1
        elif command == "show status":
            show_status()
        elif command == "show creature":
            show_creature()
        elif command == "help":
            help()
        elif command == "quit":
            print("Thanks for playing")
            break
        else:
            print("Unknown command. Type 'help' for a list of commands.")

main()