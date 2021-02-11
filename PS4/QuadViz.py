import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from IKEngin import Quadruped
from pyPS4Controller.controller import Controller
from threading import Thread

# Setting up 3D matplotlib figure
fig = plt.figure()
ax = Axes3D(fig)
# ax.set_aspect("equal")

x = y = z = yaw = pitch = roll = 0

WINDOW_SIZE = 500
ANIMATE_INTERVAL = 50
start_height = 170
ax.set_xlim3d(-WINDOW_SIZE / 2, WINDOW_SIZE / 2)
ax.set_ylim3d(-WINDOW_SIZE / 2, WINDOW_SIZE / 2)
ax.set_zlim3d(-start_height, WINDOW_SIZE - start_height)

ax.set_xlabel('x (mm)')
ax.set_ylabel('y (mm)')
ax.set_zlabel('z (mm)')

# Setting up Quadruped
robot = Quadruped(ax=ax, origin=(0, 0, 0))

class MyController(Controller):
    global switch, buffer, inc, x, y, z, yaw, pitch, roll
    def __init__(self, **kwargs):
        Controller.__init__(self, **kwargs)


    def on_x_press(self):
        print("Hello world")
        animate()

    def on_x_release(self):
       print("Goodbye world")

    def on_L3_right(self, i):
        global yaw
        yaw = i/30000
        animate()

    def on_L3_left(self, i):
        global yaw
        yaw = i/30000
        animate()

    def on_L3_x_at_rest(self):
        global yaw
        yaw = 0
        animate()

    def on_L3_up(self, i):
        global pitch
        pitch = i/150000
        animate()

    def on_L3_down(self, i):
        global pitch
        pitch = i/150000
        animate()

    def on_L3_y_at_rest(self):
        global pitch
        pitch = 0
        animate()

controller = MyController(interface="/dev/input/js0", event_format="3Bh2b", connecting_using_ds4drv=False)

def setup():
    ax.clear()
    ax.set_aspect("auto")

    ax.set_xlim3d(-WINDOW_SIZE / 2, WINDOW_SIZE / 2)
    ax.set_ylim3d(-WINDOW_SIZE / 2, WINDOW_SIZE / 2)
    ax.set_zlim3d(-start_height, WINDOW_SIZE - start_height)

    ax.set_xlabel('x (mm)')
    ax.set_ylabel('y (mm)')
    ax.set_zlabel('z (mm)')


def animate():
    global x, y, z, yaw, pitch, roll
    setup()
    # Going to starting pose
    #robot.start_position()
    # Shifting robot pose in cartesian system x-y-z (body-relative)
    #robot.shift_body_xyz(x, y, z)
    # Shifting robot pose in Euler Angles yaw-pitch-roll (body-relative)
    robot.shift_body_rotation(-yaw, pitch,roll)
    print(yaw)
    robot.draw_body()
    #robot.draw_legs()
    plt.draw()
    plt.pause(0.001)


    # print(i * ANIMATE_INTERVAL / 1000)

listener_thread = Thread(target=controller.listen())
listener_thread.daemon = True
listener_thread.start()
