from character import Character

class Monster(Character):
    def __init__(self):
        super().__init__()  # Call the parent constructor

    def monster_attacks(self):
        print(f"Monster attacks with combat strength: {self.combat_strength}")

    def __del__(self):
        super().__del__()  # Call the parent destructor