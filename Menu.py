import pygame as pg
import pygame_gui as pgui

from Sheep import Sheep
from Wolf import Wolf


class AddOrganismSubMenu():
    def __init__(self,
                 manager,
                 world,
                 MENU_X_OFFSET,
                 MENU_Y_OFFSET,
                 MENU_BUTTON_SIZE):
        self.o_to_add = None
        self.manager = manager
        self.world = world
        self.buttons = []

        next_button_x = MENU_X_OFFSET

        self.add_wolf_button = pgui.elements.UIButton(relative_rect=pg.Rect((next_button_x, MENU_Y_OFFSET),
                                                                            MENU_BUTTON_SIZE),
                                                      text="WOLF",
                                                      manager=self.manager)
        self.buttons.append(self.add_wolf_button)
        next_button_x += MENU_BUTTON_SIZE[0]

        self.add_sheep_button = pgui.elements.UIButton(relative_rect=pg.Rect((next_button_x, MENU_Y_OFFSET),
                                                                             MENU_BUTTON_SIZE),
                                                       text="SHEEP",
                                                       manager=self.manager)
        self.buttons.append(self.add_sheep_button)
        next_button_x += MENU_BUTTON_SIZE[0]

        self.add_fox_button = pgui.elements.UIButton(relative_rect=pg.Rect((next_button_x, MENU_Y_OFFSET),
                                                                           MENU_BUTTON_SIZE),
                                                     text="FOX",
                                                     manager=self.manager)
        self.buttons.append(self.add_fox_button)
        next_button_x += MENU_BUTTON_SIZE[0]

    def __contains__(self, button):
        if button in self.buttons:
            return True
        else:
            return False

    def manage_events(self, event):
        if event.ui_element == self.add_wolf_button:
            self.o_to_add = "WOLF"
        elif event.ui_element == self.add_sheep_button:
            self.o_to_add = "SHEEP"
        elif event.ui_element == self.add_fox_button:
            self.o_to_add = "FOX"
        else:
            self.o_to_add = None

    def add_org(self, location):
        if self.world.map[location] is not None:
            # self.clog += "<br>Cannot add organism to {loc} - location is not empty".format(loc=location)
            return False
        else:
            if self.o_to_add is None:
                # self.clog += "<br>Cannot add organism - no organism selected"
                return False
            else:
                world_change = True
                if self.o_to_add == "SHEEP":
                    # self.clog += "<br>Adding sheep to {loc}".format(loc=location)
                    self.world.add_organism(Sheep(self.world, location))
                elif self.o_to_add == "WOLF":
                    self.world.add_organism(Wolf(self.world, location))
                    # self.clog += "<br>Adding wolf to {loc}".format(loc=location)

                self.o_to_add = None
                return True
