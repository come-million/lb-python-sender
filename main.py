import time
import colorsys
import LBClientSender
import HSVColor
import Animations.Confetti
import Animations.RandHueMove
import Animations.Breath

lb_sender = LBClientSender.LBClientSender("10.0.0.202")

colors_arr = [HSVColor.HSVColor() for i in range(0, 50)]
rgb_arr = [0] * (3 * len(colors_arr))

#confetti = Animations.Confetti.Confetti(colors_arr)
breath = Animations.Breath.Breath(colors_arr)
#rand_hue_move = Animations.RandHueMove.RandHueMove(colors_arr)

NUM_OF_PIXELS = 250
FRAMES_PER_SECOND = 90

while True:
    rel_time = (time.time() % 2.0) / 2.0

    #rand_hue_move.apply()
    breath.apply(rel_time)

    for i in range(len(colors_arr)):
        hsv = colors_arr[i]
        rgb = colorsys.hsv_to_rgb(hsv.hue, hsv.sat, hsv.val)
        rgb_arr[3 * i: 3 * (i + 1)] = [int(c * 255) for c in rgb]

    lb_sender.send_packet(0, 1, rgb_arr)
    lb_sender.send_stored_frame()
    time.sleep(1.0 / FRAMES_PER_SECOND)



