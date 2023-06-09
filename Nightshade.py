from Plant import *

NIGHTSHADE_SEEDING_THRESHOLD = BASE_PLANT_SEEDING_THRESHOLD
NIGHTSHADE_STRENGTH = 99
NIGHTSHADE_INITIATIVE = BASE_PLANT_INITIATIVE
NIGHTSHADE_TYPE = "NIGHTSHADE"


class Nightshade(Plant):
    def __init__(self, new_world, new_location):
        super().__init__(new_world, new_location, NIGHTSHADE_STRENGTH, NIGHTSHADE_INITIATIVE, NIGHTSHADE_TYPE, NIGHTSHADE_SEEDING_THRESHOLD)

    def spawn_offspring(self, new_location):
        return Nightshade(self.world, new_location)

    def __str__(self):
        return "Nightshade at " + str(self.location)

    def collision(self, invader):
        invader.kill_self()