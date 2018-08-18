from creature import Creature


class KilledSpot(Creature):
    def __init__(self, x, y, strength, gender):
        Creature.__init__(self, x, y, strength, gender)
