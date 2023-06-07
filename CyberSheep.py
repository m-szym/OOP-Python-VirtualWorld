from Animal import Animal, BASE_ANIMAL_SPEED

CYBER_SHEEP_STRENGTH = 11
CYBER_SHEEP_INITIATIVE = 4
CYBER_SHEEP_SPEED = BASE_ANIMAL_SPEED
CYBER_SHEEP_TYPE = "CYBER_SHEEP"


class CyberSheep(Animal):
    def __init__(self, new_location, new_world):
        super().__init__(new_location, new_world, CYBER_SHEEP_STRENGTH, CYBER_SHEEP_INITIATIVE, CYBER_SHEEP_TYPE, CYBER_SHEEP_SPEED)

    def spawn_offspring(self, new_location):
        return CyberSheep(new_location, self.world)

    def __str__(self):
        return "Cyber Sheep at " + str(self.location)

    def choose_new_location(self):
        p = self.get_map().bfs(self.location,
                               lambda imap, loc: imap[loc] is not None and imap[loc].get_type() == "HOGWEED")

        if p is None:
            print(f"Didn't find hogweed, wandering from {self.location}")
            return super().choose_new_location()
        else:
            print(f"Found hogweed at {p[-1]}")
            print(f"Starting from {p[0]}")
            return p[0]