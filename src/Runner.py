#!/usr/bin/env python3
import argparse
from enum import Enum
from src.ESPNScraper import Sport
from src.ESPNScraper import ESPNScraper

parser = argparse.ArgumentParser(description='Home light parser')
parser.add_argument('--list-events', dest='events', type=Sport.from_string, nargs='+',
                    help='events to show', choices=list(Sport))


args = parser.parse_args()

scrapper = ESPNScrapper()

scrapper.list_events(args.events)



