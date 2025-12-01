state = {
    'day': 1,
    'max_day': 30,
    'bounty': 0, 
    'energy': 100, 
    'cash': 500, 
    'hauls_completed': 0, 
    'loot': 0, 
    'target_credits': 500000 
}

tools = {
    'lockpick': {'cost': 100, 'bonus': 10},
    'drill': {'cost': 300, 'bonus': 30},
    'hacking_device': {'cost': 500, 'bonus': 50},
    'inside_man': {'cost': 1000, 'bonus': 80}
}

inventory = {
    'lockpick': 0,
    'drill': 0,
    'hacking_device': 0,
    'inside_man': 0
}

banks = {
    'small bank': {'base_loot': 1000, 'difficulty': 1},
    'city bank': {'base_loot': 5000, 'difficulty': 3},
    'national bank': {'base_loot': 20000, 'difficulty': 5},
    'federal reserve': {'base_loot': 100000, 'difficulty': 8}
}

debug_mode = False

def help():
    print("Heist Simulator Commands:")
    print("1. show_status - Display current status")
    print("2. show_inventory - Display your tools")
    print("3. buy_tools - Purchase tools for heists")
    print("4. attempt_heist - Attempt to heist a bank")
    print("5. rest - Rest to recover energy and advance the day")
    print("6. quit - Exit the game")
def calculate_heist_success(bank_name):
    bank = banks[bank_name]
    tool_bonus = sum(inventory[tool] * tools[tool]['bonus'] for tool in inventory)
    success_chance = max(10, 70 + tool_bonus - (bank['difficulty']+state['bounty']) * 10) # Minimum 10% chance (goodluck to all the gamblers out there xoxo)
    return success_chance
def show_status():
    print(f"Day: {state['day']}/{state['max_day']}")
    print(f"Cash: ${state['cash']}")
    print(f"Bounty: ${state['bounty']}")
    print(f"Energy: {state['energy']}/100")
    print(f"Hauls Completed: {state['hauls_completed']}")
    print(f"Loot Collected: ${state['loot']}")
def show_inventory():
    print("Inventory:")
    for tool, qty in inventory.items():
        print(f"{tool.capitalize()}: {qty}")

def buy_tools():
    print("Available tools to buy:")
    for tool, info in tools.items():
        print(f"{tool.capitalize().replace('_',' ')}: Cost: ${info['cost']}, Bonus: {info['bonus']}")
    choice = input("Enter the tool you want to buy (or 'exit' to cancel): ").strip().lower().replace(" ","_")
    if choice in tools:
        if state['cash'] >= tools[choice]['cost']:
            state['cash'] -= tools[choice]['cost']
            inventory[choice] += 1
            print(f"You bought a {choice.capitalize().replace('_',' ')}.")
        else:
            print("Not enough cash to buy that tool.")
    elif choice == 'exit':
        return
    else:
        print("Invalid tool choice.")

def scout_banks():
    print("Available banks to heist:")
    for bank in banks:
        print(f"- {bank}")

def attempt_heist():
    scout_banks()
    global debug_mode
    choice = input("Enter the bank you want to heist (or 'exit' to cancel): ").strip()
    if choice in banks:
        success_chance = calculate_heist_success(choice)
        if debug_mode == True:
            print(f"[DEBUG] Bounty: {state['bounty']}, Tool Bonus: {sum(inventory[tool] * tools[tool]['bonus'] for tool in inventory)}, Difficulty: {banks[choice]['difficulty']}")
        print(f"Attempting heist on {choice} with a success chance of {success_chance}%...")
        import random
        if random.randint(1, 100) <= success_chance:
            loot = banks[choice]['base_loot']
            state['cash'] += loot
            state['loot'] += loot
            state['hauls_completed'] += 1
            state['bounty'] += 1
            state['day'] += 1
            print(f"Heist successful! You stole ${loot}.")
        else:
            state['bounty'] += 2
            state['energy'] -= 20
            state['day'] += 1
            print("Heist failed! You lost energy and your bounty increased.")
    elif choice == 'exit':
        return
    else:
        print("Invalid bank choice.")

def rest():
    print("Resting to recover energy...")
    state['energy'] = min(100, state['energy'] + 30)
    state['day'] += 1
    print(f"Energy restored to {state['energy']}. Day advanced to {state['day']}.")

def debug():
    global debug_mode
    if debug_mode:
        debug_mode = False
        print("Debug mode deactivated.")
        return
    print("DEBUG INFO:")
    print(state)
    print(inventory)
    debug_mode = True

def main():
    print("Welcome to Heist Simulator!")
    print("\nWhat would you like to do?")
    print("1. Show Status")
    print("2. Show Inventory")
    print("3. Buy Tools")
    print("4. Attempt Heist")
    print("5. Rest")
    print("6. Help")
    print("7. Quit")
    while state['day'] <= state['max_day']:
        print(f"\n--- Day {state['day']} ---")
        choice = input("Enter your choice: ").strip().lower().split()
        if debug_mode == True:
            print(choice)
        if choice == ['1'] or choice == ['show','status']:
            show_status()
        elif choice == ['2'] or choice == ['show','inventory']:
            show_inventory()
        elif choice == ['3'] or choice == ['buy','tools']:
            buy_tools()
        elif choice == ['4'] or choice == ['attempt','heist']:
            attempt_heist()
        elif choice == ['5'] or choice == ['rest']:
            rest()
        elif choice == ['6'] or choice == ['help']:
            help()
        elif choice == ['7'] or choice == ['quit']:
            print("Thanks for playing Heist Simulator!")
            break
        elif choice == ['debug']:
            debug()
        else:
            print("Invalid choice. Please try again.")
        
        if state['cash'] >= state['target_credits']:
            print(f"Congratulations! You've amassed ${state['cash']} and won the game!")
            break
    else:
        print("You've run out of days! Game over.")

main()