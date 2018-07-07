
import random
import math
import time
import HSVColor

class Breath:

    pixels_arr = None

    rate_arr = []

    def __init__(self, num_of_pixels):
        self.pixels_arr = [HSVColor.HSVColor() for i in range(0, num_of_pixels)]
        self.rate_arr = [random.uniform(0.1, 5) for _ in self.pixels_arr]
        self.offset_arr = [random.uniform(0.0, math.pi) for _ in self.pixels_arr]

    def apply(self, t):

        time_since_ephoc = time.time()
        for i in range(0, len(self.pixels_arr)):
            p = self.pixels_arr[i]
            rate = self.rate_arr[i]
            p.val = max(math.sin(rate * time_since_ephoc) / 2.0 + 0.5, 0.0)
            p.sat = 1.0
            p.hue = time_since_ephoc % 10.0 / 10.0
