from bear import Bear
from fish import Fish
from babyfish import BabyFish
from babybear import BabyBear
from creature import Creature
from killedspot import KilledSpot
import time
import sys


class Ecosystem(object):

    def __init__(self, x, y):
        # --- Create  grid of numbers
        # Create an empty list
        self.grid = [[]]
        self.x = x
        self.y = y

    def make_board(self):
        # Loop for each row
        for row in range(self.x):
            # For each row, create a list that will represent an entire row
            self.grid.append([])
            # Loop for each column
            for column in range(self.y):
                # Add in the number zero to the current row
                self.grid[row].append('-')

    def print(self):
        for y in range(self.y):
            # print(' -'*(self.x*2+1))
            # print(' - ', end='')
            for x in range(self.x):
                print('{:}'.format(self.grid[x][y]), end='  ')
            print()
            print()
        # print(' -'*(self.x*2+1))

    def set_pos(self, creature):
        x = creature.get_x()
        y = creature.get_y()
        if isinstance(creature, Bear):
            self.grid[x][y] = 'B'
        elif isinstance(creature, KilledSpot):
            self.grid[x][y] = '-'
        elif isinstance(creature, BabyFish):
            self.grid[x][y] = '>'
        elif isinstance(creature, BabyBear):
            self.grid[x][y] = '9'
        elif isinstance(creature, Fish):
            self.grid[x][y] = 'F'

    def get_y(self):
        return self.y

    def get_x(self):
        return self.x

    def set_y(self, y):
        self.y = y

    def set_x(self, x):
        self.x = x

    def flood(self):
        time.sleep(2)
        for y in range(self.y*2):
            sys.stdout.write("\033[F")
            sys.stdout.write("\033[K")
