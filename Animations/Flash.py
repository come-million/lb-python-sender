
import random
import time
import math

class Flash:

    pixels_arr = None
    last_t = 0.0
    hue = 0.0

    def __init__(self, pixels_arr):
        self.pixels_arr = pixels_arr
        self.choose_locations()

    def choose_locations(self):
        num_of_on = len(self.pixels_arr) / 3;
        self.on_pixels = [random.randint(0, len(self.pixels_arr) - 1) for _ in range(0, num_of_on)]
        for p in self.pixels_arr:
            p.val = 0.0
        self.hue = random.random();

    def apply(self, t):

        t = (time.time() % 0.3) / 0.3

        if t < self.last_t:
            self.choose_locations()
        self.last_t = t

        val = max(0.0, math.sin(2 * math.pi * t - math.pi / 2) / 2.0 + 0.5);
        for i in self.on_pixels:
            self.pixels_arr[i].val = val
            self.pixels_arr[i].hue = self.hue
