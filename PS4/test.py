from pyPS4Controller.controller import Controller


class MyController(Controller):

    def __init__(self, **kwargs):
        Controller.__init__(self, **kwargs)

    def on_x_press(self):
       print("Hello world")

    def on_x_release(self):
       print("Goodbye world")

    def on_L3_right(self, i):
       print(i)

    def on_L3_left(self, i):
       print(i)
controller = MyController(interface="/dev/input/js0", event_format="3Bh2b", connecting_using_ds4drv=False)
# you can start listening before controller is paired, as long as you pair it within the timeout window
controller.listen()
