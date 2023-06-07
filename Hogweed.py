from Plant import *

HOGWEED_SEEDING_THRESHOLD = BASE_PLANT_SEEDING_THRESHOLD
HOGWEED_STRENGTH = 0
HOGWEED_INITIATIVE = BASE_PLANT_INITIATIVE
HOGWEED_TYPE = "HOGWEED"


class Hogweed(Plant):
    def __init__(self, new_location, new_world):
        super().__init__(new_location, new_world, HOGWEED_STRENGTH, HOGWEED_INITIATIVE, HOGWEED_TYPE,
                         HOGWEED_SEEDING_THRESHOLD)

    def spawn_offspring(self, new_location):
        return Hogweed(new_location, self.world)

    def __str__(self):
        return "Hogweed at " + str(self.location)

    def collision(self, invader):
        if invader.get_type() == "CYBER_SHEEP":
            self.kill_self()
        else:
            invader.kill_self()

    def action(self):
        self.get_map().do_on_all_neighbours(self.location, hogweed_poison)
        super().action()


def hogweed_poison(imap, loc):
    t = imap[loc]
    if t is not None and t.get_type() != "CYBER_SHEEP":
        imap[loc].kill_self()
