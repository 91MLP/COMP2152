from hero import Hero
from monster import Monster
from function import save_game, load_game, print_system_info

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

def main():
    # Print system info
    print_system_info()

    # Load game state
    health_points, combat_strength, monsters_killed = load_game()
    if health_points is not None:
        hero = Hero()
        hero.health_points = health_points
        hero.combat_strength = combat_strength
    else:
        hero = Hero()

    # Create a monster
    monster = Monster()

    # Game loop
    while hero.health_points > 0 and monster.health_points > 0:
        print(f"\nHero Health: {hero.health_points}, Monster Health: {monster.health_points}")
        hero.hero_attacks()
        monster.monster_attacks()

        # Simulate damage
        hero.health_points -= monster.combat_strength
        monster.health_points -= hero.combat_strength

        if monster.health_points <= 0:
            print("Monster defeated!")
            monsters_killed += 1

    # Save game state
    save_game(hero, monsters_killed)
    print(f"Total monsters killed: {monsters_killed}")

if __name__ == "__main__":
    main()