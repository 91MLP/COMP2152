import random

class Character:
    def __init__(self):
        # Roll dice for combat strength and health points
        self._combat_strength = random.randint(1, 20)
        self._health_points = random.randint(1, 20)

    # Complex getters and setters for combat_strength
    @property
    def combat_strength(self):
        return self._combat_strength

    @combat_strength.setter
    def combat_strength(self, value):
        if value < 0:
            raise ValueError("Combat strength cannot be negative.")
        self._combat_strength = value

    # Complex getters and setters for health_points
    @property
    def health_points(self):
        return self._health_points

    @health_points.setter
    def health_points(self, value):
        if value < 0:
            raise ValueError("Health points cannot be negative.")
        self._health_points = value

    def __del__(self):
        print(f"The {self.__class__.__name__} object is being destroyed by the garbage collector.")