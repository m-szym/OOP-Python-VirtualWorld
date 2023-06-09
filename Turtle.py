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
    def __init__(self, new_world, new_location):
        super().__init__(new_world, new_location, TURTLE_STRENGTH, TURTLE_INITIATIVE, TURTLE_TYPE, TURTLE_SPEED)

    def spawn_offspring(self, new_location):
        return Turtle(self.world, new_location)

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