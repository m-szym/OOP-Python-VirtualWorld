from Plant import *

HOGWEED_SEEDING_THRESHOLD = BASE_PLANT_SEEDING_THRESHOLD
HOGWEED_STRENGTH = 0
HOGWEED_INITIATIVE = BASE_PLANT_INITIATIVE
HOGWEED_TYPE = "HOGWEED"



class Hogweed(Plant):
    def __init__(self, new_location, new_world):
        super().__init__(new_world, new_location, HOGWEED_STRENGTH, HOGWEED_INITIATIVE, HOGWEED_TYPE, HOGWEED_SEEDING_THRESHOLD)

    def spawn_offspring(self, new_location):
        return Hogweed(new_location, self.world)

    def __str__(self):
        return "Hogweed at " + str(self.location)

    def collision(self, invader):
        invader.kill_self()

    def action(self):
        self.get_map().do_on_all_neighbours(self.location, lambda x: x.kill_self())
        super().action()

