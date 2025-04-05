import random

class Item:
    def __init__(self, item_type):
        self.type = item_type  # "sword" or "potion"
        if self.type == "sword":
            self.power = random.randint(1, 5)  # Weapon increases attack power
        else:
            self.power = random.randint(3, 8)  # Potion restores health

    def use(self, hero):
        if self.type == "sword":
            hero.combat_strength += self.power
            print(f"Hero equipped a sword! Combat strength +{self.power}")
        else:
            hero.health_points += self.power
            print(f"Hero drank a potion! Health +{self.power}")