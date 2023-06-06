from Plant import *

GRASS_SEEDING_THRESHOLD = BASE_PLANT_SEEDING_THRESHOLD
GRASS_STRENGTH = BASE_PLANT_STRENGTH
GRASS_INITIATIVE = BASE_PLANT_INITIATIVE
GRASS_TYPE = "GRASS"


class Grass(Plant):
    def __init__(self, new_location, new_world):
        super().__init__(new_world, new_location, GRASS_STRENGTH, GRASS_INITIATIVE, GRASS_TYPE, GRASS_SEEDING_THRESHOLD)

    def spawn_offspring(self, new_location):
        return Grass(new_location, self.world)

    def __str__(self):
        return "Grass at " + str(self.location)
