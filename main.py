# This is a sample Python script.
import random

import MapLocations
import Maps
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import World as w
from CyberSheep import CyberSheep
from Hogweed import Hogweed
from Organism import *
from Sheep import Sheep

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print_hi('PyCharm')
    world = w.World.square_map(10, 10)
    # # world.add_organism(Organism(world, MapLocations.SquareLocation(0, 0)))
    # world.add_organism(Sheep(world, MapLocations.SquareLocation(5, 5)))
    # world.map.print_map()


    # print("a")
    # l1 = MapLocations.SquareLocation((0, 0))
    # print(l1)
    # l2 = MapLocations.SquareLocation.copyc(l1)
    # print(l2)
    # l1.coords = (1, 1)
    # print(l1)
    # print(l2)  # l2 should not change
    # print("b")
    # l3 = l1.get_neighbour_location(0)
    # print(l3)
    # print(l1)
    # print("c")
    # l4 = l3 * 2
    # print(l4)
    # print(l1)

    # world.add_organism(Sheep(world, MapLocations.SquareLocation((5, 0))))
    #
    #
    # def targeter(imap, location):
    #     if imap[location] is not None and imap[location].get_type() == "SHEEP":
    #         return True
    #     else:
    #         return False
    #
    #
    # p = world.map.bfs(MapLocations.SquareLocation((0, 0)), targeter)
    # for i in p:
    #     print(i)
    cs = world.add_organism(CyberSheep(world, MapLocations.SquareLocation((5, 0))))
    h = world.add_organism(Hogweed(world, MapLocations.SquareLocation((5, 5))))

    # cs.choose_new_location()
    for i in range(0, 10):
        print("Turn " + str(i))
        world.clean_board()
        world.make_turn()
        world.map.print_map()

    # world.map.print_map()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
