import pygame as pg
import pygame_gui as pgui

import MapLocations
import Maps

import World as w
from Human import Human
from Sheep import Sheep
from Wolf import Wolf

from Sim import Simulator


def visulizer(world):
    pg.init()

    w = 1200
    h = 800

    pg.display.set_caption('Quick Start')
    window_surface = pg.display.set_mode((w, h))

    background = pg.Surface((w, h))
    background.fill(pg.Color('#000000'))

    manager = pgui.UIManager((w, h))

    bs = 50
    bw = bs
    bh = bs

    bx = 0
    by = 0

    buttons = []

    if isinstance(world.map, Maps.SquareMap):
        for y in range(world.map.height):
            for x in range(world.map.width):
                print("_ ", end="")
                nb = pgui.elements.UIButton(relative_rect=pg.Rect((bx, by), (bw, bh)),
                                            text='{i}'.format(i=len(buttons)),
                                            manager=manager)
                nb.map_location = MapLocations.SquareLocation((x, y))
                buttons.append(nb)
                bx += bw
            print()
            by += bh + 0
            bx = 0
    elif isinstance(world.map, Maps.HexMap):
        size = world.map.size

        for q in range(-size, size + 1):
            r1 = max(-size, -q - size)
            r2 = min(size, -q + size)

            for i in range(-size, size - r2 + r1):
                print(" ", end="")
                bx += bw

            for r in range(0, abs(q)):
                bx -= bw / 2

            for r in range(r1, r2 + 1):
                print("_ ", end="")
                nb = pgui.elements.UIButton(relative_rect=pg.Rect((bx, by), (bw, bh)),
                                            text='{i}'.format(i=len(buttons)),
                                            manager=manager)
                nb.map_location = MapLocations.HexLocation((q, r, -q - r))
                buttons.append(nb)
                bx += bw
            print()
            by += bh + 0
            bx = 0

    tb = pgui.elements.UIButton(relative_rect=pg.Rect((0, 600), (100, 100)),
                                text="Next Turn",
                                manager=manager)
    add_wolf = pgui.elements.UIButton(relative_rect=pg.Rect((0, 700), (100, 100)),
                                text="add wolf",
                                manager=manager)


    clock = pg.time.Clock()
    is_running = True
    to_add = None

    while is_running:
        time_delta = clock.tick(60) / 1000.0
        for event in pg.event.get():
            if event.type == pg.QUIT:
                is_running = False
            elif event.type == pgui.UI_BUTTON_PRESSED:
                if event.ui_element == tb:
                    world.make_turn()
                    for button in buttons:
                        if world.map[button.map_location] is None:
                            button.set_text("")
                        else:
                            button.set_text(world.map[button.map_location].get_type()[0])
                elif event.ui_element == add_wolf:
                    to_add = "WOLF"
                else:
                    if to_add == "WOLF":
                        if world.map[event.ui_element.map_location] is None:
                            world.add_organism(Wolf(world, event.ui_element.map_location))
                            to_add = None
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    is_running = False
                elif event.key == pg.K_SPACE:
                    world.make_turn()
                    for button in buttons:
                        if world.map[button.map_location] is None:
                            button.set_text("")
                        else:
                            button.set_text(world.map[button.map_location].get_type()[0])
                else:
                    if isinstance(world.map, Maps.SquareMap):
                        if event.key == pg.K_UP:
                            world.get_human().direction = 3
                        elif event.key == pg.K_RIGHT:
                            world.get_human().direction = 0
                        elif event.key == pg.K_DOWN:
                            world.get_human().direction = 1
                        elif event.key == pg.K_LEFT:
                            world.get_human().direction = 2
                    elif isinstance(world.map, Maps.HexMap):
                        if event.key == pg.K_w:
                            world.get_human().direction = 3
                        elif event.key == pg.K_e:
                            world.get_human().direction = 2
                        elif event.key == pg.K_d:
                            world.get_human().direction = 1
                        elif event.key == pg.K_x:
                            world.get_human().direction = 0
                        elif event.key == pg.K_z:
                            world.get_human().direction = 5
                        elif event.key == pg.K_a:
                            world.get_human().direction = 4

                world.make_turn()
                for button in buttons:
                    if world.map[button.map_location] is None:
                        button.set_text("")
                    else:
                        button.set_text(world.map[button.map_location].get_type()[0])

            manager.process_events(event)

        manager.update(time_delta)

        window_surface.blit(background, (0, 0))
        manager.draw_ui(window_surface)

        pg.display.update()




if __name__ == '__main__':
    # print_hi('PyCharm')
    # world = w.World.square_map(10, 10)
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
    # cs = world.add_organism(CyberSheep(world, MapLocations.SquareLocation((5, 0))))
    # h = world.add_organism(Hogweed(world, MapLocations.SquareLocation((5, 5))))
    #
    # world.map.print_map()
    # world.save("test1")
    # world2 = w.World.load("test1")
    # world2.map.print_map()

    # # cs.choose_new_location()
    # for i in range(0, 10):
    #     print("Turn " + str(i))
    #     world.clean_board()
    #     world.make_turn()
    #     world.map.print_map()

    # world.map.print_map()
    # h = w.World.hex_map(5)
    # c = h.add_organism(CyberSheep(h, MapLocations.HexLocation((0, 0, 0))))
    # weed = h.add_organism(Hogweed(h, MapLocations.HexLocation((0, 1, -1))))
    # h.map.print_map()
    # h.save("hex_test")
    # h2 = w.World.load("hex_test")
    # print("First world")
    # h.map.print_map()
    # print("After turn")
    # h.make_turn()
    # h.clean_board()
    # h.map.print_map()
    # print("Second world")
    # h2.map.print_map()
    # print("After turn")
    # h2.make_turn()
    # h2.clean_board()
    # h2.map.print_map()
    # print("After another turn")
    # h2.make_turn()
    # h2.clean_board()
    # h2.map.print_map()
    # # for i in range(0, 10):
    # #     print("Turn " + str(i))
    # #     h.clean_board()
    # #     h.make_turn()
    # #     h.map.print_map()


    # s = w.World.square_map(10, 5)
    # human = s.add_organism(Human(s, MapLocations.SquareLocation((0, 0))))
    # s.human = human
    # visulizer(s)

    h = w.World.hex_map(5)
    human = h.add_organism(Human(h, MapLocations.HexLocation((0, 0, 0))))
    h.add_organism(Sheep(h, MapLocations.HexLocation((0, 1, -1))))
    h.human = human
    # visulizer(h)
    v = Simulator(h)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
