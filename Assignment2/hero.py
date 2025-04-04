from character import Character

class Hero(Character):
    def __init__(self):
        super().__init__()  # Call the parent constructor

    def hero_attacks(self):
        print(f"Hero attacks with combat strength: {self.combat_strength}")

    def __del__(self):
        super().__del__()  # Call the parent destructor