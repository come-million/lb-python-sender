
import random
import math
import time

class Breath:

    pixels_arr = None

    rate_arr = []

    def __init__(self, pixels_arr):
        self.pixels_arr = pixels_arr
        self.rate_arr = [random.uniform(0.1, 5) for _ in pixels_arr]
        self.offset_arr = [random.uniform(0.0, math.pi) for _ in pixels_arr]

    def apply(self, t):

        time_since_ephoc = time.time()
        for i in range(0, len(self.pixels_arr)):
            p = self.pixels_arr[i]
            rate = self.rate_arr[i]
            p.val = max(math.sin(rate * time_since_ephoc) / 2.0 + 0.5, 0.0)
            p.sat = 1.0
            p.hue = time_since_ephoc % 10.0 / 10.0
