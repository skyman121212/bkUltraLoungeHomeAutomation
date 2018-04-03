

class Team:

    def __init__(self, team_data, score):
        self.team_data = team_data
        self.score = score

    def __str__(self):
        return "{} ({})".format(self.team_data['displayName'], self.score)
