
class Game:

    def __init__(self, home, away):
        self.home = home
        self.away = away

    def __str__(self):
        return "{} vs {}".format(self.home, self.away)

