
import random

class Confetti:

    pixels_arr = None

    def __init__(self, pixels_arr):
        self.pixels_arr = pixels_arr

    def apply(self, t):
        for p in self.pixels_arr:
            p.val *= 0.95

        index = random.randint(0, len(self.pixels_arr) - 1)
        self.pixels_arr[index].val = 1.0
        self.pixels_arr[index].hue = t
