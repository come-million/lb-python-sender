import time
import LBClientSender

lb_sender = LBClientSender.LBClientSender("10.0.0.202")

NUM_OF_PIXELS = 51
FRAMES_PER_SECOND = 30

while True:
    rel_time = (time.time() % 2.0) / 2.0

    arr = [0, 0, 0] * NUM_OF_PIXELS
    for i in range(0, int(rel_time * NUM_OF_PIXELS)):
        arr[i * 3 + 2] = 255
    lb_sender.send_packet(0, 0, arr)
    lb_sender.send_stored_frame()
    time.sleep(1.0 / FRAMES_PER_SECOND)


