import random

class RandHueMove:

    pixels_arr = None

    def __init__(self, pixels_arr):
        self.pixels_arr = pixels_arr
        for p in self.pixels_arr:
            p.hue = random.random()
            p.val = 1.0
            p.sat = 1.0

    def apply(self):
        for p in self.pixels_arr:
            p.hue += 0.005