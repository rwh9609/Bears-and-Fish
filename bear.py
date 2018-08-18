from creature import Creature


class Bear(Creature):
    def __init__(self, x, y, strength, gender):
        Creature.__init__(self, x, y, strength, gender)
        self.n = 'B'

    def get_n(self):
        return self.n
