from character import Character
from item import Item

class Hero(Character):
    def __init__(self):
        super().__init__()
        self.inventory = []  # Inventory for items

    def add_item(self, item):
        self.inventory.append(item)

    def use_item(self, index):
        if 0 <= index < len(self.inventory):
            item = self.inventory.pop(index)
            item.use(self)
        else:
            print("Invalid item index!")

    def hero_attacks(self):
        print(f"Hero attacks with combat strength: {self.combat_strength}")