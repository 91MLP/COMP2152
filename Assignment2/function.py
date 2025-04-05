import os
import platform

def save_game(hero, monsters_killed):
    with open("save.txt", "w") as file:
        file.write(f"{hero.health_points}\n")
        file.write(f"{hero.combat_strength}\n")
        file.write(f"{monsters_killed}\n")

def load_game():
    if not os.path.exists("save.txt"):
        return None, 0

    with open("save.txt", "r") as file:
        health_points = int(file.readline().strip())
        combat_strength = int(file.readline().strip())
        monsters_killed = int(file.readline().strip())

    return health_points, combat_strength, monsters_killed

def print_system_info():
    print(f"Operating System: {os.name}")
    print(f"Python Version: {platform.python_version()}")