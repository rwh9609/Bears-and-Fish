from fish import Fish


class BabyFish(Fish):
    def __init__(self, x, y, strength, gender):
        Fish.__init__(self, x, y, strength, gender)
        self.f = 'baby fish'
