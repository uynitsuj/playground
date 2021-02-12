import threading
import struct

class PS4Thread(threading.Thread):

    def __init__(self, input_cbk = None, name='ps4-input-thread'):
        self.input_cbk = input_cbk
        super(PS4Thread, self).__init__(name=name)
        self.start()

    def run(self):
        file = open("/dev/input/js0", "rb")
        while True:
            event = file.read(struct.calcsize("3Bh2b"))
            (*tv_sec, value, button_type, button_id) = struct.unpack("3Bh2b", event)
            self.input_cbk(button_id) #waits to get input + Return
            if (button_id == 1 and button_type == 2):
                print("L3_y_axis val:", value)

showcounter = 0 #something to demonstrate the change

def my_callback(inp):
    #evaluate the keyboard input
    print('You Entered:', inp, ' Counter is at:', showcounter)

#start the Keyboard thread

if __name__ == '__main__':
    kthread = PS4Thread(my_callback)
    while True:
        #the normal program executes without blocking. here just counting up
        showcounter += 1
