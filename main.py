# This is a sample Python script.
import random

import MapLocations
import Maps
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import World as w
from Organism import *


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print_hi('PyCharm')
    world = w.World.square_map(10, 10)
    world.add_organism(Organism(world, MapLocations.SquareLocation(0, 0)))
    world.map.print_map()
    print(f"0 to {world.map.directions_num + 1}")
    for i in range(0, 100):
        a = random.randint(0, world.map.directions_num + 1)
        if a == world.map.directions_num + 1:
            print("stay")
        print(a)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
