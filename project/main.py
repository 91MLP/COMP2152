from hero import Hero
from monster import Monster
from item import Item
from function import save_game, load_game, print_system_info, dream_levels
import random

def main():
    # Print system info
    print_system_info()

    # Load game state
    health_points, combat_strength, monsters_killed, inventory = load_game()
    if health_points is not None:
        hero = Hero()
        hero.health_points = health_points
        hero.combat_strength = combat_strength
        hero.inventory = inventory
    else:
        hero = Hero()

    # Game loop
    while True:
        # Create a new monster for each battle
        monster = Monster()
        print("\nA new monster appears!")
        
        # Battle loop
        while hero.health_points > 0 and monster.health_points > 0:
            print(f"\nHero Health: {hero.health_points}, Monster Health: {monster.health_points}")
            
            # Hero's turn
            hero.hero_attacks()
            monster.health_points -= hero.combat_strength
            
            # Check if monster is defeated
            if monster.health_points <= 0:
                break
                
            # Monster's turn
            monster.monster_attacks()
            hero.health_points -= monster.combat_strength
            
            # Check if hero is defeated
            if hero.health_points <= 0:
                break

        # Battle outcome
        if monster.health_points <= 0:
            print("Monster defeated!")
            monsters_killed += 1

            # 50% chance to drop an item
            if random.random() < 0.5:
                item_type = random.choice(['sword', 'potion'])
                item = Item(item_type)
                hero.add_item(item)
                print(f"Got a {item_type}! Enter 'use' to check inventory")

        # Check if hero died
        if hero.health_points <= 0:
            print("Hero has been defeated! Game Over.")
            break

        # Inventory management
        user_input = input("Enter 'use' to open inventory, or press Enter to continue: ")
        if user_input.lower() == "use":
            print("\nInventory:")
            for i, item in enumerate(hero.inventory):
                print(f"{i}: {item.type} (power: {item.power})")
            item_index = input("Enter item number to use, or 'cancel': ")
            if item_index.isdigit():
                hero.use_item(int(item_index))

        # Save game state
        save_game(hero, monsters_killed)
        print(f"Total monsters killed: {monsters_killed}")

        # Ask if player wants to continue
        continue_game = input("Continue playing? (y/n): ")
        if continue_game.lower() != 'y':
            break

if __name__ == "__main__":
    main()