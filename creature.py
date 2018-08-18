class Creature(object):

    def __init__(self, x, y, strength, gender):
        self.x = int(x)
        self.y = int(y)
        self.strength = int(strength)
        self.gender = gender

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_strength(self):
        return self.strength

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def get_gender(self):
        return self.gender

    def set_strength(self, strength):
        self.strength = strength
