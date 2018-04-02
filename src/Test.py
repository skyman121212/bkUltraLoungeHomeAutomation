#!/usr/bin/env python3
import flux_led
import requests
import base64

# light = flux_led.WifiLedBulb("192.168.86.182")
# light.turnOff()

print("test")

pull_url = 'https://api.mysportsfeeds.com/v1.2/pull/nba/2017-2018-regular/scoreboard.json?fordate=20180401'
USERNAME = "kelseyhrubes"
PASSWORD = "blakeiscute"

def send_request(pull_url):
    # Request
    try:
        response = requests.get(
            url={pull_url},
            params={
                "fordate": "20180401"
            },
            headers={
                "Authorization": "Basic " + base64.b64encode('{}:{}'.format({USERNAME},{PASSWORD}).encode('utf-8')).decode('ascii')
            }
        )
        print('Response HTTP Status Code: {status_code}'.format(
            status_code=response.status_code))
        print('Response HTTP Response Body: {content}'.format(
            content=response.content))
    except requests.exceptions.RequestException:
        print('HTTP Request failed')



send_request(pull_url)