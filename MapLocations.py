class MapLocation:
    # def __init__(self, new_coords):
    #     self.coords = new_coords
    #     self.coords_num = len(new_coords)

    def __init__(self, other_location):
        self.coords = other_location.coords
        self.coords_num = other_location.coords_num

    def __eq__(self, other):
        if not isinstance(other, MapLocation):
            return False
        return self.coords == other.coords

    def __hash__(self):
        return hash(self.coords)

    def __str__(self):
        string_form = "("
        for coord in self.coords:
            string_form += str(coord) + " "
        string_form += ")"
        return string_form

    def get_neighbour_location(self, direction):
        pass


#    N
#   W W
#    S


SQUARE_DIRS = {
    "E": (1, 0),
    "S": (0, 1),
    "W": (-1, 0),
    "N": (0, -1)
}


class SquareLocation(MapLocation):
    def __init__(self, x, y):
        self.coords = (x, y)
        self.coords_num = 2

    def get_x(self):
        return self.coords[0]

    def get_y(self):
        return self.coords[1]

    def __add__(self, other):
        return SquareLocation(self.get_x() + other.get_x(), self.get_y() + other.get_y())

    def __mul__(self, scale):
        return SquareLocation(self.get_x() * scale, self.get_y() * scale)

    def get_neighbour_location(self, direction):
        return self + SquareLocation(*SQUARE_DIRS[direction])

    def get_far_neighbour_location(self, direction, distance):
        return self + (SquareLocation(*SQUARE_DIRS[direction]) * distance)


#    NW NE
#   W     E
#    SW SE


HEX_DIRS = {
    "E": (1, 0, -1),
    "SE": (0, 1, -1),
    "SW": (-1, 1, 0),
    "W": (-1, 0, 1),
    "NW": (0, -1, 1),
    "NE": (1, -1, 0)
}


class HexLocation(MapLocation):
    def __init__(self, q, r, s):
        self.coords = (q, r, s)
        self.coords_num = 3

    def __init__(self, q, r):
        self.coords = (q, r, -q-r)
        self.coords_num = 3

    def get_q(self):
        return self.coords[0]

    def get_r(self):
        return self.coords[1]

    def get_s(self):
        return self.coords[2]

    def __add__(self, other):
        return HexLocation(self.get_q() + other.get_q(), self.get_r() + other.get_r(), self.get_s() + other.get_s())

    def __mul__(self, scale):
        return HexLocation(self.get_q() * scale, self.get_r() * scale, self.get_s() * scale)

    def get_neighbour_location(self, direction):
        return self + HexLocation(*HEX_DIRS[direction])
