import socket
import array
import random

class LBClientSender:

    ip_addr = None

    last_frame_id = random.randint(0, 100000000)
    sock = socket.socket(socket.AF_INET,  # Internet
                         socket.SOCK_DGRAM)  # UDP
    stored_msgs = []

    PROTOCOL_VERSION = 0
    UDP_PORT = 2000

    def __init__(self, ip_addr):
        self.ip_addr = ip_addr

    def _uint8_to_array(self, num):
        c1 = (num / (1)) % 256
        return [c1]

    def _uint16_to_array(self, num):
        c1 = (num / (256)) % 256
        c2 = (num / (1)) % 256
        return [c2, c1]

    def _uint32_to_array(self, num):
        c1 = (num / (256 * 256 * 256)) % 256
        c2 = (num / (256 * 256)) % 256
        c3 = (num / (256)) % 256
        c4 = (num / (1)) % 256
        return [c4, c3, c2, c1]

    def send_packet(self, strip_id, pixel_id, pixel_data):
        self.stored_msgs.append({"strip_id" : strip_id, "pixel_id": pixel_id, "pixel_data":pixel_data})

    def send_stored_frame(self):
        num_of_segments = len(self.stored_msgs)
        for i in range(0, num_of_segments):
            curr_segment = self.stored_msgs[i]
            self._do_send(curr_segment["strip_id"], num_of_segments, i, curr_segment["pixel_id"], curr_segment["pixel_data"])
        self.last_frame_id = self.last_frame_id + 1
        self.stored_msgs = []

    def _do_send(self, strip_id, seg_in_frame, seg_id, pixel_id, pixels_data):
        data = self._uint8_to_array(LBClientSender.PROTOCOL_VERSION) + \
               self._uint32_to_array(self.last_frame_id) + \
               self._uint32_to_array(seg_in_frame) + \
               self._uint32_to_array(seg_id) + \
               self._uint16_to_array(strip_id) + \
               self._uint16_to_array(pixel_id)

        data = data + pixels_data
        msg = "LedBurn" + array.array('B', data).tostring()
        self.sock.sendto(msg, (self.ip_addr, LBClientSender.UDP_PORT))
