'''
An example in input:
1. Travel to another planet (costs credits).
- travel <planet> (e.g., travel mars) doesn't matter the case
2. Buy items from the market.
- buy <item> <quantity> (e.g., buy food 10)
3. Sell items to the market.
- sell <item> <quantity> (e.g., sell water 5)
'''


# Player state
state = {
    'location': 'earth',
    'credits': 1000,
    'inventory': {
        'food': 10,
        'water': 5,
        'fuel': 20
    },
    'inventory_capacity': {
        'food': 50,
        'water': 30,
        'fuel': 100
    }
}

# Market prices on different planets
market = {
    'earth': {
        'food': {'buy_price': 5, 'sell_price': 3},
        'water': {'buy_price': 2, 'sell_price': 1},
        'fuel': {'buy_price': 10, 'sell_price': 7}
    },
    'mars': {
        'food': {'buy_price': 8, 'sell_price': 5},
        'water': {'buy_price': 3, 'sell_price': 2},
        'fuel': {'buy_price': 15, 'sell_price': 10}
    },
    'jupiter': {
        'food': {'buy_price': 12, 'sell_price': 8},
        'water': {'buy_price': 5, 'sell_price': 3},
        'fuel': {'buy_price': 20, 'sell_price': 15}
    },
    'venus': {
        'food': {'buy_price': 7, 'sell_price': 4},
        'water': {'buy_price': 4, 'sell_price': 2},
        'fuel': {'buy_price': 18, 'sell_price': 12}
    }
}

# Travel costs between planets
travel_costs = {
    ('Earth', 'Mars'): 50,
    ('Earth', 'Jupiter'): 100,
    ('Earth', 'Venus'): 70,
    ('Mars', 'Jupiter'): 60,
    ('Mars', 'Venus'): 40,
    ('Mars', 'Earth'): 50,
    ('Jupiter', 'Earth'): 100,
    ('Jupiter', 'Venus'): 80,
    ('Jupiter', 'Mars'): 60,
    ('Venus', 'Earth'): 70,
    ('Venus', 'Mars'): 40,
    ('Venus', 'Jupiter'): 80,
}

# Based global variables
day = 1
max_day = 30
target_credits = 5000

print("Welcome to Space Trader!")
print("You start on Earth with 1000 credits.")
print("Your goal is to reach 5000 credits within 30 days by trading goods and traveling between planets.")

def instructions():
    # Instructions for the player
    print("Available commands:")
    print("1. travel <planet> - Travel to another planet (costs credits).")
    print("2. buy <item> <quantity> - Buy items from the market.")
    print("3. sell <item> <quantity> - Sell items to the market.")
    print("4. status - View your current status.")
    print("5. help - Show instructions again.")
    print("6. quit - Exit the game.")

def show_status():
    # Show current status
    print(f"Location: {state['location']}")
    print(f"Credits: {state['credits']}")
    print("Inventory:")
    for item, qty in state['inventory'].items():
        print(f"  {item}: {qty}/{state['inventory_capacity'][item]}")

def travel(planet):
    # Check if travel is possible
    if planet not in market:
        print("Unknown planet.")
        return
    # Check if already on the planet
    if planet == state['location']:
        print("You are already on that planet.")
        return
    # Determine travel cost
    # Compared two keys from state['location'] aka current planet to the target planet travel(planet), if they line up then retrieve similar value from travel_costs dict
    cost = travel_costs[(state['location'].capitalize(), planet.capitalize())] if (state['location'].capitalize(), planet.capitalize()) in travel_costs else travel_costs.get((planet.capitalize(), state['location'].capitalize()))
    # If no route found, or a faulty one
    if cost is None:
        print("No direct route to that planet.")
        return
    # Check if enough credits
    if state['credits'] < cost:
        print("Not enough credits to travel.")
        return
    # Update current player state (location and credits)
    state['credits'] -= cost
    state['location'] = planet
    print(f"Traveled to {planet}. Cost: {cost} credits.")
    print(f"Market prices on {planet}:")

def buy(item, quantity):
    # Check if item is available
    if item not in market[state['location']]:
        print("Item not available on this planet.")
        return
    # Retrieve price and calculate total cost
    price = market[state['location']][item]['buy_price']
    total_cost = price * quantity
    # Not enough credits or inventory space
    if state['credits'] < total_cost:
        print("Not enough credits to buy.")
        return
    if state['inventory'][item] + quantity > state['inventory_capacity'][item]:
        print("Not enough inventory space.")
        return
    # Update player state
    state['credits'] -= total_cost
    state['inventory'][item] += quantity
    print(f"Bought {quantity} {item}(s) for {total_cost} credits.")

def sell(item, quantity):
    # Check if item is sellable
    if item not in market[state['location']]:
        print("Item not buyable on this planet.")
        return
    # Check if enough items to sell
    if state['inventory'][item] < quantity:
        print("Not enough items to sell.")
        return
    # Retrieve price and calculate total earnings
    price = market[state['location']][item]['sell_price']
    total_earnings = price * quantity
    # Update player state
    state['credits'] += total_earnings
    state['inventory'][item] -= quantity
    print(f"Sold {quantity} {item}(s) for {total_earnings} credits.")

def entry():
    global day
    # Show market prices and travel options
    print(f"Available {state['location']} market prices:")
    for item, prices in market[state['location']].items():
        print(f"  {item}: Buy at {prices['buy_price']} credits, Sell at {prices['sell_price']} credits")
    print("Available travel options:")
    for (from_planet, to_planet), cost in travel_costs.items():
        if from_planet.lower() == state['location']:
            print(f"  To {to_planet} for {cost} credits")
    # Get player command
    match input("Enter command (type 'help' for instructions): ").strip().lower().split():
        case ["travel", planet]:
            travel(planet)
        case ["buy", item, qty]:
            buy(item, int(qty))
        case ["sell", item, qty]:
            sell(item, int(qty))
        case ["status"]:
            show_status()
            day = day - 1 # Stay on the same day after viewing status
        case ["help"]:
            instructions()
            day = day - 1 # Stay on the same day after viewing help
        case ["credits", qty]:
            state['credits'] += int(qty) # Debug command to add credits
            print(f"Added {qty} credits for testing purposes.")
        case ["day", qty]:
            day += int(qty) # Debug command to advance days
            print(f"Advanced {qty} days for testing purposes.")
        case ["quit"]:
            return False
        case _:
            print("Invalid command.")
            day = day - 1 # Stay on the same day after invalid command
    return True

def main():
    instructions()
    global day
    # Game loop
    while day <= max_day:
        print(f"\n--- Day {day} ---")
        if not entry():
            print("Exiting game. Goodbye!")
            return
        if state['credits'] >= target_credits:
            print(f"Congratulations! You've reached {state['credits']} credits and won the game!")
            return
        day += 1
    print(f"Game over! You ended with {state['credits']} credits.")

main()