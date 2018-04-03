import urllib.request
import json
from enum import Enum
from src.Team import Team
from src.Game import Game

class ESPNScrapper:

    def __init__(self):
        self.test = "hi"

    def get_events(self, sports):
        games = []
        for s in sports:
            games.extend(self.get_event(s))

        return games

    def get_event(self, sport):
        games = []

        with urllib.request.urlopen("{}".format(sport.value)) as url:
            data = json.loads(url.read().decode())

        events = data['events']

        for event in events:
            team1 = event['competitions'][0]['competitors'][0]
            team2 = event['competitions'][0]['competitors'][1]

            games.append(Game(Team(team1['team'], team1['score']), Team(team2['team'], team2['score'])))

        return games


class Sport(Enum):
    MENS_COLLEGE_BASKETBALL = \
        "http://site.api.espn.com/apis/site/v2/sports/basketball/mens-college-basketball/scoreboard"
    NBA = \
        "http://site.api.espn.com/apis/site/v2/sports/basketball/nba/scoreboard"

    def __str__(self):
        return self.name

    @staticmethod
    def from_string(s):
        try:
            return Sport[s]
        except KeyError:
            raise ValueError()

