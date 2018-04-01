#!/usr/bin/env python3
import flux_led

light = flux_led.WifiLedBulb("192.168.86.182")
light.turnOn()

