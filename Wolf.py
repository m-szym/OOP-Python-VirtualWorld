from Animal import Animal, BASE_ANIMAL_SPEED

WOLF_STRENGTH = 9
WOLF_INITIATIVE = 5
WOLF_SPEED = BASE_ANIMAL_SPEED
WOLF_TYPE = "WOLF"


class Wolf(Animal):
    def __init__(self, new_location, new_world):
        super().__init__(new_location, new_world, WOLF_STRENGTH, WOLF_INITIATIVE, WOLF_TYPE, WOLF_SPEED)

    def spawn_offspring(self, new_location):
        return Wolf(new_location, self.world)

    def __str__(self):
        return "Wolf at " + str(self.location)
