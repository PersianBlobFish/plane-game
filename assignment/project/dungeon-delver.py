# Player state
state = {
    'hp': 20,
    'location': 'entrance',
    'potions': 2,
    'position': (0, 0),
    'score': 0,
    'cleared_rooms': set()
}
# Dungeon layout
dungeon = {
    (0, 0): {'description': 'You are at the dungeon entrance.', 'exits': ['north']},
    (0, 1): {'description': 'A dimly lit corridor.', 'exits': ['south', 'east', 'north']},
    (1, 1): {'description': 'A room with a sleeping goblin.', 'exits': ['west', 'east', 'north','south']},
    (0, 2): {'description': 'A treasure room filled with gold!', 'exits': ['south', 'east']},
    (1, 2): {'description': 'A dark chamber with eerie sounds.', 'exits': ['west', 'south', 'east']},
    (2, 1): {'description': 'A narrow passageway.', 'exits': ['north', 'west','south']},
    (2, 2): {'description': 'The lair of the dungeon boss!', 'exits': ['south']},
}
# Player statistics
stats = {
    'attack': 10,
    'defense': 5,
    'level': 1,
    'experience': 0,
    'next_level_exp': 0
}
# Calculate next level experience
stats['next_level_exp'] = 2 ** stats['level'] * 10

# Directional movement
def move(direction):
    x, y = state['position']
    if direction == 'north':
        new_pos = (x, y + 1)
    elif direction == 'south':
        new_pos = (x, y - 1)
    elif direction == 'east':
        new_pos = (x + 1, y)
    elif direction == 'west':
        new_pos = (x - 1, y)
    else:
        print("Invalid direction!")
        return
    # Check if the move is valid
    if new_pos in dungeon and direction in dungeon[state['position']]['exits']:
        state['position'] = new_pos
        describe_location()
    else:
        print("You can't go that way!")

def describe_location():
    # Describe the current location
    pos = state['position']
    room = dungeon[pos]
    print(room['description'])
    print("Exits:", ', '.join(room['exits']))

def help_menu():
    # Classic help menu
    print("Available commands:")
    print("move <direction> - Move up, down, left, or right (north, south, east, west)")
    print("stats - Show player stats")
    print("use potion - Use a health potion")
    print("status - Show player status")
    print("help - Show this help menu")
    print("quit - Exit the game")

def show_status():
    # Show current status
    print("Player Status:")
    print(f"HP: {state['hp']}")
    print(f"Location: {state['position']}")
    print(f"Potions: {state['potions']}")
    print(f"Score: {state['score']}")
    print(f"Level: {stats['level']} (EXP: {stats['experience']}/{stats['next_level_exp']})")

def show_stats():
    # Show player stats
    print("Player Stats:")
    for key, value in stats.items():
        print(f"{key.capitalize()}: {value}")

def use_potion():
    # Use a health potion
    if state['potions'] > 0:
        state['hp'] += 10
        state['potions'] -= 1
        print("You used a potion. HP increased by 20.")
    else:
        print("No potions left!")

def enter_room():
    # Check if room is cleared for the first time (this is to prevent multiple rewards in the same room)
    pos = state['position']
    if pos not in state['cleared_rooms']:
        state['cleared_rooms'].add(pos)
        if pos != (0, 0):  # Don't reward for entrance
            state['score'] += 10
            stats['experience'] += 20
            if stats['experience'] >= stats['next_level_exp']: # Level up mechanic (so you guys dont speed run the boss)
                stats['level'] += 1
                state['hp'] += 10
                stats['attack'] += 5 # Irrelevance but nice to have
                stats['defense'] += 3
                stats['experience'] = 0 # Reset experience at new level
                stats['next_level_exp'] = 2 ** stats['level'] * 10 # Formula for next level experience
                print(f"You leveled up to level {stats['level']}!")
        print("You have cleared a new room! Score increased by 10.")

def room_event():
    # Handle events in specific rooms
    # Goblin encounter
    if state['position'] == (1, 1):
        print("A goblin attacks you!")
        state['hp'] -= 15
        if state['hp'] <= 0:
            print("You have been defeated by the goblin. Game over.")
            exit()
        else:
            print(f"You defeated the goblin! HP is now {state['hp']}.")
    # Boss encounter
    if state['position'] == (2, 2):
        print("You have encountered the dungeon boss!")
        state['hp'] -= 50
        if state['hp'] <= 0:
            print("You have been defeated by the boss. Game over.")
            exit()
        else:
            print(f"You defeated the boss! HP is now {state['hp']}. You win!")
            exit()
    # Treasure room
    if state['position'] == (0, 2):
        print("You found a treasure chest! You gain 50 score.")
        state['score'] += 50
        print(f"Score is now {state['score']}.")
    # Health potion room
    if state['position'] == (2, 1):
        print("You found a health potion!")
        state['potions'] += 1
        print(f"Potions: {state['potions']}")
    

def main():
    print("Welcome to Dungeon Delver!")
    help_menu()
    describe_location()
    # Main game loop
    while True:
        command = input("> ").strip().lower()
        if command.startswith("move "):
            direction = command.split()[1]
            move(direction)
            enter_room()
            room_event()
            print(f"Position: {state['position']}")
            print(f"HP: {state['hp']}, Potions: {state['potions']}, Score: {state['score']}")
        elif command == "status":
            show_status()
        elif command == "stats":
            show_stats()
        elif command == "use potion":
            use_potion()
        elif command == "help":
            help_menu()
        elif command == "quit":
            print("Thanks for playing!")
            break
        else:
            print("Unknown command. Type 'help' for a list of commands.")

main()