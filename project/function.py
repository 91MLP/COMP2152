import os
import platform

def save_game(hero, monsters_killed):
    with open("save.txt", "w") as file:
        file.write(f"{hero.health_points}\n")
        file.write(f"{hero.combat_strength}\n")
        file.write(f"{monsters_killed}\n")
        # Save inventory
        file.write(f"{len(hero.inventory)}\n")
        for item in hero.inventory:
            file.write(f"{item.type},{item.power}\n")

def load_game():
    if not os.path.exists("save.txt"):
        return None, None, 0, []
    
    with open("save.txt", "r") as file:
        health_points = int(file.readline().strip())
        combat_strength = int(file.readline().strip())
        monsters_killed = int(file.readline().strip())
        # Load inventory
        inventory = []
        item_count = int(file.readline().strip())
        for _ in range(item_count):
            item_type, power = file.readline().strip().split(',')
            item = Item(item_type)
            item.power = int(power)
            inventory.append(item)

    return health_points, combat_strength, monsters_killed, inventory

def print_system_info():
    print(f"Operating System: {os.name}")
    print(f"Python Version: {platform.python_version()}")

def dream_levels():
    while True:
        try:
            level = int(input("Enter dream level (0-3): "))
            if 0 <= level <= 3:
                return level
            else:
                print("Please enter a number between 0 and 3.")
        except ValueError:
            print("Invalid input. Please enter a number.")