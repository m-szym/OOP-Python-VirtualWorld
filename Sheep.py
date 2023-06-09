from Animal import Animal, BASE_ANIMAL_SPEED

SHEEP_STRENGTH = 4
SHEEP_INITIATIVE = 4
SHEEP_SPEED = BASE_ANIMAL_SPEED
SHEEP_TYPE = "SHEEP"


class Sheep(Animal):
    def __init__(self, new_world, new_location):
        super().__init__(new_world, new_location, SHEEP_STRENGTH, SHEEP_INITIATIVE, SHEEP_TYPE, SHEEP_SPEED)

    def spawn_offspring(self, new_location):
        return Sheep(self.world, new_location)

    def __str__(self):
        return "Sheep at " + str(self.location)
