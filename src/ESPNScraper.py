import urllib.request
import json
from enum import Enum


class ESPNScraper:

    def __init__(self):
        self.test = "hi"

    def list_events(self, sports):
        for s in sports:
            self.list_event(s)

    def list_event(self, sport):
        with urllib.request.urlopen("{}".format(sport.value)) as url:
            data = json.loads(url.read().decode())
        print(len(data['events']))


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

