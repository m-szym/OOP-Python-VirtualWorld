from Maps import SquareMap, HexMap

from Organism import Organism, DEAD_STATE


class World:
    def __init__(self):
        self.organisms = []
        self.turn = 0
        self.human = None
        self.map = None

    @classmethod
    def square_map(cls, width, height):
        world = cls()
        world.map = SquareMap(width, height)
        return world

    @classmethod
    def hex_map(cls, size):
        world = cls()
        world.map = HexMap(size)
        return world

    def populate(self):
        pass

    def add_organism(self, organism) -> Organism:
        try:
            self.map[organism.get_location()] = organism
            self.organisms.append(organism)
            return organism
        except KeyError:
            print(f"Organism {str(organism.get_location())} out of map")
            return None

    def clean_board(self):
        for organism in self.organisms:
            if organism.get_state() == DEAD_STATE:
                self.map[organism.get_location()] = None
                self.organisms.remove(organism)

    def make_turn(self):
        self.turn += 1
        for organism in self.organisms:
            organism.action()

    def sort_organisms(self):
        self.organisms.sort()

    def get_map(self):
        return self.map

    def get_turn(self):
        return self.turn

    def get_organisms(self):
        return self.organisms

    def get_human(self):
        return self.human