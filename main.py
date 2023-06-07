# This is a sample Python script.
import random

import MapLocations
import Maps
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import World as w
from Organism import *
from Sheep import Sheep


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print_hi('PyCharm')
    # world = w.World.square_map(10, 10)
    # # world.add_organism(Organism(world, MapLocations.SquareLocation(0, 0)))
    # world.add_organism(Sheep(world, MapLocations.SquareLocation(5, 5)))
    # world.map.print_map()
    # for i in range(0,10):
    #     world.make_turn()
    #     world.map.print_map(
    print("a")
    l1 = MapLocations.SquareLocation((0, 0))
    print(l1)
    l2 = MapLocations.SquareLocation.copy(l1)
    print(l2)
    l1.coords = (1, 1)
    print(l1)
    print(l2)   # l2 should not change
    print("b")
    l3 = l1.get_neighbour_location(0)
    print(l3)
    print(l1)
    print("c")
    l4 = l3 * 2
    print(l4)
    print(l1)





# See PyCharm help at https://www.jetbrains.com/help/pycharm/
