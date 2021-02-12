import struct

file = open("/dev/input/js0", "rb")
while True:
    #print(file.readline(struct.calcsize("3Bh2b")))
    if file.read(struct.calcsize("3Bh2b")) is None:
        print("lack of event")
        break
    event = file.read(struct.calcsize("3Bh2b"))
    print(event)
    (*tv_sec, value, button_type, button_id) = struct.unpack("3Bh2b", event)
    print(tv_sec)
    print(button_type)
    print(button_id)
    print(value)

print("break")
