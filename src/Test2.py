#!/usr/bin/env python3
import flux_led
from MagicHomeLightController import MagicHomeLightController

light = flux_led.WifiLedBulb("192.168.86.182")

lightController = MagicHomeLightController(light)
lightController.flicker_lights([[255, 0, 0], [255, 0, 255]])
