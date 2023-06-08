from Animal import Animal, BASE_ANIMAL_SPEED

HUMAN_STRENGTH = 5
HUMAN_INITIATIVE = 4
HUMAN_SPEED = BASE_ANIMAL_SPEED
HUMAN_TYPE = "HUMAN"
HUMAN_SKILL_COOLDOWN = 5
HUMAN_SKILL_DURATION = 5


class Human(Animal):
    def __init__(self, new_location, new_world):
        super().__init__(new_world, new_location, HUMAN_STRENGTH, HUMAN_INITIATIVE, HUMAN_SPEED, HUMAN_TYPE)
        self.skill_cooldown = HUMAN_SKILL_COOLDOWN
        self.skill_duration_left = 0
        self.skill_active = False
        self.direction = self.get_map().directions_num

    def spawn_offspring(self, new_location):
        pass

    def decide_where_to_move(self):
        return self.direction

    def skill(self):
        if not self.skill_active and self.skill_cooldown > 0:
            self.skill_cooldown -= 1

        if self.skill_active and self.skill_duration_left > 1:
            self.skill_duration_left -= 1
        elif self.skill_active and self.skill_duration_left == 1:
            self.skill_duration_left = 0
            self.skill_active = False
            self.skill_cooldown = HUMAN_SKILL_COOLDOWN

        if self.skill_active:
            self.balefire()

    def balefire(self):
        self.get_map().do_on_all_neighbours(self.location, kill_target)

    def action(self):
        self.skill()
        super().action()
        self.direction = self.get_map().directions_num

    def activate_skill(self):
        self.skill_active = True
        self.skill_cooldown = HUMAN_SKILL_COOLDOWN

    def give_command(self, command):
        if command <= self.get_map().directions_num:
            self.direction = command
            return True
        elif command == 200:
            if self.skill_cooldown == 0 and not self.skill_active:
                self.activate_skill()
                return True
        else:
            return False


def kill_target(imap, loc):
    if imap[loc] is not None:
        imap[loc].kill_self()
