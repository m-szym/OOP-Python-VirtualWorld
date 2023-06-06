from MapLocations import SQUARE_DIRS, SquareLocation, HEX_DIRS, HexLocation


class Map:
    def __init__(self):
        self.directions_num = 0
        self.internal_map = {}
        # self.directions = {}

        self.create_map()

    def create_map(self):
        pass

    def __contains__(self, location):
        return location in self.internal_map

    def __getitem__(self, location):
        if location not in self.internal_map:
            raise KeyError("Location not in map")
        return self.internal_map[location]

    def __setitem__(self, location, value):
        if location not in self.internal_map:
            raise KeyError("Location not in map")
        self.internal_map[location] = value

    def on_map(self, location):
        if location in self.internal_map:
            return True
        else:
            return False

    def move_org(self, org, new_location):
        self.internal_map[new_location] = org
        self.internal_map[org.get_location()] = None
        # org.set_location(new_location)

    def do_on_all_neighbours(self, location, func):
        for direction in self.directions:
            neighbour_location = location.get_neighbour_location(direction)
            if neighbour_location in self:
                func(self, neighbour_location)

    def get_first_free_neighbour(self, location):
        for direction in self.directions:
            neighbour_location = location.get_neighbour_location(direction)
            if neighbour_location in self and self[neighbour_location] is None:
                return neighbour_location
        return None

    def get_neighbours(self, location):
        neighbours = []
        for direction in self.directions:
            neighbour_location = location.get_neighbour_location(direction)
            if neighbour_location in self:
                neighbours.append(neighbour_location)
        return neighbours

    def get_neighbours_with_organisms(self, location):
        neighbours = []
        for direction in self.directions:
            neighbour_location = location.get_neighbour_location(direction)
            if neighbour_location in self and self[neighbour_location] is not None:
                neighbours.append(self[neighbour_location])
        return neighbours

    def print_all_locations(self):
        for location in self.internal_map:
            print(location, self.internal_map[location])

    def print_map(self):
        pass




class SquareMap(Map):
    def __init__(self, width, height):
        self.directions = SQUARE_DIRS
        self.directions_num = len(SQUARE_DIRS)
        self.internal_map = {}

        self.width = width
        self.height = height
        # super().__init__()
        self.create_map()

    def create_map(self):
        for x in range(self.width):
            for y in range(self.height):
                self.internal_map[SquareLocation(x, y)] = None

    def print_map(self):
        for y in range(self.height):
            for x in range(self.width):
                if self.internal_map[SquareLocation(x, y)] is None:
                    print("_", end="")
                else:
                    print("O", end="")
            print()


class HexMap(Map):
    def __init__(self, size):
        self.directions = HEX_DIRS
        self.directions_num = len(HEX_DIRS)
        self.size = size
        super().__init__()

    def create_map(self):
        for q in range(-self.size, self.size):
            r1 = max(-self.size, -q - self.size)
            r2 = min(self.size, -q + self.size)
            for r in range(r1, r2):
                self.internal_map[HexLocation(q, r)] = None
