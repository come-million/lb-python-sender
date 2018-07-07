
import random
import time
import math

class Vibe:

    color_hues = [random.random() for _ in range(0, 6)]
    sin_freq = range(5, 5 + len(color_hues))
    pixels_arr = None
    last_t = 0.0
    pixel_hue = [0]

    def __init__(self, pixels_arr):
        self.pixels_arr = pixels_arr
        self.choose_locations()

    def choose_locations(self):
        self.pixel_hue = [0] * len(self.pixels_arr)
        for i in range(0, len(self.pixels_arr)):
            self.pixel_hue[i] = random.randint(0, len(self.color_hues) - 1)

    def apply(self, t):

        t = (time.time() % 2.0) / 2.0

        if t < self.last_t:
            pass
            #self.choose_locations()
        self.last_t = t

        val = max(0.0, math.sin(2 * math.pi * t - math.pi / 2) / 2.0 + 0.5)
        curr_time = time.time()
        for i in range(0, len(self.pixels_arr)):
            hue_group = self.pixel_hue[i]
            self.pixels_arr[i].val = math.sin(curr_time * self.sin_freq[hue_group]) / 2.0 + 0.5
            self.pixels_arr[i].hue = self.color_hues[hue_group]
