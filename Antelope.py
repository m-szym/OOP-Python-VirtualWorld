from random import randint

from Animal import Animal

ANTELOPE_STRENGTH = 4
ANTELOPE_INITIATIVE = 4
ANTELOPE_SPEED = 2
ANTELOPE_TYPE = "ANTELOPE"
ANTELOPE_ESCAPE_CHANCE_BASE = 10
ANTELOPE_ESCAPE_CHANCE_THRESHOLD = 5


class Antelope(Animal):
    def __init__(self, new_location, new_world):
        super().__init__(new_location, new_world, ANTELOPE_STRENGTH, ANTELOPE_INITIATIVE, ANTELOPE_TYPE, ANTELOPE_SPEED)

    def spawn_offspring(self, new_location):
        return Antelope(new_location, self.world)

    def __str__(self):
        return "Antelope at " + str(self.location)

    def escape(self):
        escape_chance = randint(0, ANTELOPE_ESCAPE_CHANCE_BASE)
        if escape_chance > ANTELOPE_ESCAPE_CHANCE_THRESHOLD:
            new_location = self.get_map().get_first_free_neighbour(self.location)
            if new_location is not None:
                self.update_location(new_location)
                return True
        else:
            return False

    def collision(self, invader):
        if invader.get_type() == self.get_type():
            self.mate()
        else:
            if not self.escape():
                self.fight(invader)
            else:
                invader.update_location(self.location)
