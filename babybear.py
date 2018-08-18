from bear import Bear


class BabyBear(Bear):
    def __init__(self, x, y, strength, gender):
        Bear.__init__(self, x, y, strength, gender)
        self.f = 'baby bear'
