from random import randint

from Animal import Animal, BASE_ANIMAL_SPEED

TURTLE_STRENGTH = 2
TURTLE_INITIATIVE = 1
TURTLE_SPEED = BASE_ANIMAL_SPEED
TURTLE_TYPE = "TURTLE"
TURTLE_MOVEMENT_CHANCE_BASE = 4
TURTLE_MOVEMENT_THRESHOLD = 3
TURTLE_DEFENCE = 5


class Turtle(Animal):
    def __init__(self, new_location, new_world):
        super().__init__(new_location, new_world, TURTLE_STRENGTH, TURTLE_INITIATIVE, TURTLE_TYPE, TURTLE_SPEED)

    def spawn_offspring(self, new_location):
        return Turtle(new_location, self.world)

    def __str__(self):
        return "Turtle at " + str(self.location)

    def reflect_attack(self, attacker):
        if attacker.get_strength() < TURTLE_DEFENCE:
            return True
        else:
            return False

    def move(self):
        r = randint(0, TURTLE_MOVEMENT_CHANCE_BASE)

        if r >= TURTLE_MOVEMENT_THRESHOLD:
            super().move()
        # TODO: logger