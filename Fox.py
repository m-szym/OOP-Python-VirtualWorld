from Animal import Animal, BASE_ANIMAL_SPEED

FOX_STRENGTH = 3
FOX_INITIATIVE = 7
FOX_SPEED = BASE_ANIMAL_SPEED
FOX_TYPE = "FOX"


class Fox(Animal):
    def __init__(self, new_location, new_world):
        super().__init__(new_location, new_world, FOX_STRENGTH, FOX_INITIATIVE, FOX_TYPE, FOX_SPEED)

    def spawn_offspring(self, new_location):
        return Fox(new_location, self.world)

    def __str__(self):
        return "Fox at " + str(self.location)

    def pre_collision(self, autochton):
        if autochton.get_type() == FOX_TYPE:
            # TODO: logger
            return False
        else:
            return super().pre_collision(autochton)