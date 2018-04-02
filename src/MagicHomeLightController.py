import time


class MagicHomeLightController:

    def __init__(self, light):
        self.light = light

    def flicker_lights(self, colors):
        self.light.setCustomPattern(colors, 100, "jump")
        time.sleep(3)
        self.light.setRgb(colors[0][0],colors[0][1],colors[0][2])
