import time
import colorsys
import LBClientSender
import HSVColor
import Animations.Confetti
import Animations.RandHueMove
import Animations.Breath
import Animations.Flash
import Animations.Vibe

lb_sender = LBClientSender.LBClientSender("10.0.0.201")

PIXELS_PER_STRAND = 250
STRANDS_PER_CONTROLLER = 40
TOTAL_PIXELS = (PIXELS_PER_STRAND * STRANDS_PER_CONTROLLER)
FRAMES_PER_SECOND = 60

colors_arr = [HSVColor.HSVColor() for i in range(0, TOTAL_PIXELS)]
rgb_arr = [0] * (3 * len(colors_arr))

confetti = Animations.Confetti.Confetti(colors_arr)
#breath = Animations.Breath.Breath(TOTAL_PIXELS)
#rand_hue_move = Animations.RandHueMove.RandHueMove(colors_arr)
#flash = Animations.Flash.Flash(colors_arr)
#vibe = Animations.Vibe.Vibe(colors_arr)

while True:
    rel_time = (time.time() % 2.0) / 2.0

    #rand_hue_move.apply()
    #breath.apply(rel_time)
    confetti.apply(rel_time)
    #flash.apply(rel_time)
    #vibe.apply(rel_time)

    for i in range(len(colors_arr)):
        hsv = colors_arr[i]
        rgb = colorsys.hsv_to_rgb(hsv.hue, hsv.sat, hsv.val)
        rgb_arr[3 * i: 3 * (i + 1)] = [int(c * 255) for c in rgb]

    for i in range(0, STRANDS_PER_CONTROLLER):
        lb_sender.send_packet(i, 1, rgb_arr[(3 * i * PIXELS_PER_STRAND) : (3 * (i + 1) * PIXELS_PER_STRAND)])
    lb_sender.send_stored_frame()
    time.sleep(1.0 / FRAMES_PER_SECOND)



