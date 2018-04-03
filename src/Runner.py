#!/usr/bin/env python3
import argparse
from src.ESPNScraper import Sport
from src.ESPNScraper import ESPNScraper

parser = argparse.ArgumentParser(description='Home light parser')
parser.add_argument('--list-events', dest='events', type=Sport.from_string, nargs='+',
                    help='events to show', choices=list(Sport))


args = parser.parse_args()

scrapper = ESPNScraper()

e = scrapper.get_events(args.events)

for event in e:
    print(event)



