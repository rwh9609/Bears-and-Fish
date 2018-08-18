from creature import Creature


class Fish(Creature):
    def __init__(self, x, y, strength, gender):
        Creature.__init__(self, x, y, strength, gender)
        self.n = 'F'

    def get_n(self):
        return self.n
