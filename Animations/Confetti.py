
import random
import time

class Confetti:

    pixels_arr = None

    def __init__(self, pixels_arr):
        self.pixels_arr = pixels_arr

    def apply(self, t):

        rel_time = (time.time() % 7.0) / 7.0

        for p in self.pixels_arr:
            p.val *= 0.93

        for _ in range(0, len(self.pixels_arr) / 30):
            index = random.randint(0, len(self.pixels_arr) - 1)
            self.pixels_arr[index].val = 1.0
            self.pixels_arr[index].hue = rel_time
