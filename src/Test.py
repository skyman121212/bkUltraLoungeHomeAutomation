#!/usr/bin/env python3
import flux_led
import requests
import base64

# light = flux_led.WifiLedBulb("192.168.86.182")
# light.turnOff()

print("test")

url = 'https://api.mysportsfeeds.com/v1.2/pull/nba/2017-2018-regular/scoreboard.json?fordate=20180401'
headers = {'encrypted_credentials': base64.b64encode('kelseyhrubes:blakeiscute')}
response = requests.get(url, headers=headers)


print(response)