import struct

file = open("/dev/input/js0", "rb")
while True:
    event = file.read(struct.calcsize("3Bh2b"))
    print(event)
    (*tv_sec, value, button_type, button_id) = struct.unpack("3Bh2b", event)
    print(tv_sec)
    print(button_type)
    print(button_id)
    print(value)
