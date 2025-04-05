from character import Character

class Monster(Character):
    def __init__(self, drop_chance=0.5):
        super().__init__()
        self.drop_chance = drop_chance

    def monster_attacks(self):
        print(f"Monster attacks with combat strength: {self.combat_strength}")

    def __del__(self):
        super().__del__()