from Plant import *

GUARANA_SEEDING_THRESHOLD = BASE_PLANT_SEEDING_THRESHOLD
GUARANA_STRENGTH = BASE_PLANT_STRENGTH
GUARANA_INITIATIVE = BASE_PLANT_INITIATIVE
GUARANA_TYPE = "GUARANA"
GUARANA_STRENGTH_BONUS = 3


class Guarana(Plant):
    def __init__(self, new_world, new_location):
        super().__init__(new_world, new_location, GUARANA_STRENGTH, GUARANA_INITIATIVE, GUARANA_TYPE, GUARANA_SEEDING_THRESHOLD)

    def spawn_offspring(self, new_location):
        return Guarana(self.world, new_location)

    def __str__(self):
        return "Guarana at " + str(self.location)

    def collision(self, invader):
        invader.set_strength(invader.get_strength() + GUARANA_STRENGTH_BONUS)
        self.kill_self()