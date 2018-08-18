from ecosystem import Ecosystem
from bear import Bear
from fish import Fish
from babyfish import BabyFish
from babybear import BabyBear
from killedspot import KilledSpot
from random import randint, choice
from itertools import cycle


class Reader(object):

    def __init__(self, data):
        self.fp = open(data)
        self.grid = [[]]
        self.moves = 0
        self.creatures = []

    def instantiate(self):
        line = self.fp.readline()
        info = line.split()
        n = (int(info[0]))
        m = (int(info[1]))
        line2 = self.fp.readline()
        info2 = line2.split()
        self.moves = int(info2[0])
        self.grid = Ecosystem(n, m)
        self.grid.make_board()
        self.grid.print()

    def placements(self):
        line = self.fp.readline()
        self.creatures = []
        line.split()
        while line != "":
            info = line.split()
            n = info[0]
            if n is 'B':
                x = info[1]
                y = info[2]
                strength = info[3]
                gender = info[4]
                bear = (Bear(x, y, strength, gender))
                self.creatures.append(bear)
            elif n is 'F':
                x = info[1]
                y = info[2]
                strength = info[3]
                gender = info[4]
                fish = Fish(x, y, strength, gender)
                self.creatures.append(fish)
            line = self.fp.readline()

        for x in self.creatures:
            self.grid.set_pos(x)

    def update_board(self):
        self.grid.flood()
        return self.grid.print()

    def roam_and_kill(self):
        cycler = cycle(self.creatures)
        gridx = self.grid.get_x()
        gridy = self.grid.get_y()
        for move in range(self.moves):
            creature = next(cycler)
            x = creature.get_x()
            y = creature.get_y()
            strength = creature.get_strength()
            decision_maker = randint(1, 6)
            # right
            if decision_maker is 2:
                if x+1 >= gridx and y+1 >= gridy:
                    creature.set_y(0)
                    creature.set_x(0)
                elif x+1 >= gridx:
                    creature.set_y(y+1)
                    creature.set_x(0)
                else:
                    creature.set_x(x+1)
                replacement = KilledSpot(x, y, 0, 0)
                self.grid.set_pos(replacement)
            # left
            elif decision_maker is 3:
                if x-1 < 0 and y-1 < 0:
                    creature.set_x(gridx-1)
                    creature.set_y(gridy-1)
                elif x-1 < 0:
                    creature.set_y(y-1)
                    creature.set_x(gridx-1)
                else:
                    creature.set_x(x-1)
                replacement = KilledSpot(x, y, 0, 0)
                self.grid.set_pos(replacement)
            # down
            elif decision_maker is 4:
                if y+1 >= gridy and x+1 >= gridx:
                    creature.set_y(0)
                    creature.set_x(0)
                elif y+1 >= gridy:
                    creature.set_y(0)
                    creature.set_x(x+1)
                else:
                    creature.set_y(y+1)
                replacement = KilledSpot(x, y, 0, 0)
                self.grid.set_pos(replacement)
            # up
            elif decision_maker is 5:
                if y-1 < 0 and x-1 < 0:
                    creature.set_y(gridy-1)
                    creature.set_x(gridx-1)
                elif y-1 < 0:
                    creature.set_y(gridy-1)
                    creature.set_x(x-1)
                else:
                    creature.set_y(y-1)
                replacement = KilledSpot(x, y, 0, 0)
                self.grid.set_pos(replacement)
            elif decision_maker is 1:
                continue
            new_x = creature.get_x()
            new_y = creature.get_y()
            current_gender = creature.get_gender()
            for each in self.creatures:
                if each is creature:
                    continue
                elif new_x == each.get_x() and new_y == each.get_y():

                    opp_strength = int(each.get_strength())
                    opp_gender = each.get_gender()
                    n = creature.get_n()
                    m = each.get_n()
                    if opp_gender != current_gender and n == m:
                        if creature.n is 'B':
                            baby = BabyBear(new_x, new_y, 1, 'M')
                            self.grid.set_pos(baby)
                            self.creatures.append(baby)
                            del creature
                            del each
                            break
                        elif creature.n is 'F':
                            baby = BabyFish(new_x, new_y, 1, 'M')
                            self.grid.set_pos(baby)
                            self.creatures.append(baby)
                            del creature
                            del each
                            break

                    if opp_strength > int(strength):
                        del creature
                        break
                    elif int(strength) >= opp_strength:
                        del each
                        break
            for creature in self.creatures:
                self.grid.set_pos(creature)

            self.grid.flood()
            self.grid.print()

