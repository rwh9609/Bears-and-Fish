from ecosystem import Ecosystem
from bear import Bear
from fish import Fish
from babyfish import BabyFish
from babybear import BabyBear
from killedspot import KilledSpot
from random import randint, choice
from itertools import cycle
import random

class Reader(object):

    # data values are fed into constructor, aka input.txt
    def __init__(self, data):

        # creates a file object which contains the data file with the animal values and matrix size
        self.fp = open(data)
        self.grid = [[]]
        self.moves = 0
        self.creatures = []

    def instantiate(self):

        # reads the data file and creates the values which will be used to create the matrix
        line = self.fp.readline()
        info = line.split()
        n = (int(info[0]))
        m = (int(info[1]))
        line2 = self.fp.readline()
        info2 = line2.split()
        self.moves = int(info2[0])

        # creates the matrix where the Fish and Bears live
        # feeds the ecosystem an n x m matrix determined by the data file values
        self.grid = Ecosystem(n, m)

        # calls the make_board function in the Ecosystem class
        self.grid.make_board()

        # prints the currently empty matrix with '-' values
        self.grid.print()

    def placements(self):

        # reads the next line of the input file, which contain the animal values
        line = self.fp.readline()

        # reads all of the data from input
        # adds all of the creatures to a list
        # creatures have attributes including position, sex, and strength
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

                # creates a bear object which is a child of the creature class
                bear = (Bear(x, y, strength, gender))

                # appends a Bear object to a creatures list, not to be confused with the creatures class
                # the creatures list is a variable of the reader class
                self.creatures.append(bear)
            elif n is 'F':
                x = info[1]
                y = info[2]
                strength = info[3]
                gender = info[4]

                # appends a Fish object to a creatures list, not to be confused with the creatures class
                # the creatures list is a variable of the reader class
                fish = Fish(x, y, strength, gender)
                self.creatures.append(fish)

            # onto the next line, while a line exists, for the while loop to execute
            line = self.fp.readline()

        for creature in self.creatures:

            # grid is an object of the ecosystem class, set_pos is a method of the ecosystem class
            # this method call sets the position for each creature in the creatures list onto the matrix
            self.grid.set_pos(creature)

    # updates the board with current values of the matrix
    def update_board(self):

        # the flood function is called on the grid object which is an object of the
        # ecosystem class
        # the flood function completely deletes the current board in mac/linux terminals
        self.grid.flood()

        # prints the updated matrix
        return self.grid.print()

    def roam_and_kill(self):

        # cycles through the creatures list for a number of moves based on the inputted number of moves
        # gathered from the data file


        # gridx and gridy are the bounds of the matrix
        gridx = self.grid.get_x()
        gridy = self.grid.get_y()

        # the loop which executes the moves
        for move in range(self.moves):
            # cycler = cycle(self.creatures)
            # gets the next creature from the cycler variable
            # creature = next(cycler)
            creature = random.choice(self.creatures)
            # x and y are the current positions of the selected creature
            x = creature.get_x()
            y = creature.get_y()

            # gets the strength of the creature in case of potential combat
            strength = creature.get_strength()

            # decision_maker will determine whether the creature moves up, down, left, or right
            decision_maker = randint(2, 5)

            # creature moves right
            # the killedspot is the empty spot where a creature just left from
            if decision_maker is 2:
                if x+1 >= gridx and y+1 >= gridy:
                    pass
                elif x+1 >= gridx:
                    pass
                else:
                    creature.set_x(x+1)
                    replacement = KilledSpot(x, y, 0, 'M')
                    self.grid.set_pos(replacement)

            # creature moves left
            elif decision_maker is 3:
                if x-1 < 0 and y-1 < 0:
                    pass
                elif x-1 < 0:
                    pass
                else:
                    creature.set_x(x-1)
                    replacement = KilledSpot(x, y, 0, 'M')
                    self.grid.set_pos(replacement)

            # creature moves down
            elif decision_maker is 4:
                if y+1 >= gridy and x+1 >= gridx:
                    pass
                elif y+1 >= gridy:
                    pass
                else:
                    creature.set_y(y+1)
                    replacement = KilledSpot(x, y, 0, 'M')
                    self.grid.set_pos(replacement)

            # creature moves up
            elif decision_maker is 5:
                if y-1 < 0 and x-1 < 0:
                    pass
                elif y-1 < 0:
                    pass
                else:
                    creature.set_y(y-1)
                    replacement = KilledSpot(x, y, 0, 'M')
                    self.grid.set_pos(replacement)

            # new_x and new_y are the current x and y values of the creature's place on the matrix
            new_x = creature.get_x()
            new_y = creature.get_y()
            current_gender = creature.get_gender()

            # checks each creature's position
            # and if the creature which has just moved
            # arrives at the same spot as another creature
            # then combat or reproduction ensues
            for each in self.creatures:

                # gets the current x and y position of each creature
                if new_x == each.get_x() and new_y == each.get_y() and each is not creature:
                    opp_strength = int(each.get_strength())
                    opp_gender = each.get_gender()

                    # get_n returns the creature type, e.g. 'F', 'B', 'f', or 'b'
                    n = creature.get_n()
                    m = each.get_n()

                    # determines if reproduction should occur
                    if opp_gender != current_gender and n == m:
                        if creature.n is 'B':
                            baby = BabyBear(new_x, new_y, 1, 'M')
                            self.grid.set_pos(baby)
                            self.creatures.append(baby)
                            self.creatures.remove(creature)
                            self.creatures.remove(each)
                            #del each
                            break
                        elif creature.n is 'F':
                            baby = BabyFish(new_x, new_y, 1, 'M')
                            self.grid.set_pos(baby)
                            self.creatures.append(baby)
                            self.creatures.remove(creature)
                            self.creatures.remove(each)
                            #del creature
                            #del each
                            break

                    # determines who wins the combat if two creatures are at the same spot
                    if opp_strength > int(strength):
                        self.creatures.remove(creature)
                        break
                    elif int(strength) >= opp_strength:
                        self.creatures.remove(each)
                        break

            # updates the board with the current list of creatures
            for creature in self.creatures:
                self.grid.set_pos(creature)

            # wipes the board from the mac/linux terminal
            self.grid.flood()

            # prints the board
            self.grid.print()

