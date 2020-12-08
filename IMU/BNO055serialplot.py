import serial
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style

ser = serial.Serial('/dev/ttyUSB0', 500000)
print(ser)
if ser.is_open==False :
    print("no BNO055 detected")
else:
    print("BNO055 detected")
#data = []
#while True:
    #data = ser.read_until().split(",")

fig, (ax1, ax2) = plt.subplots(2, 1)
fig.suptitle('BNO055')

index = -1
ax1.clear()
ax2.clear()
ax1.set_ylabel('Orientation - (degrees)')
ax1.set_xlabel('Time - (samples)')
ax2.set_xlabel('Time - (samples)')
ax2.set_ylabel('Accelerometer - (m/s^2)')
accel_x = []
accel_y = []
accel_z = []
orient_x = []
orient_y = []
orient_z = []
x1 = []
x2 = []
temp = []
def animate(i):
    global index
    data = ser.readline().split(",")
    index += 1
    if data[0]=="Orient":
        x1.append(index)
        orient_x.append(float(data[1]))
        orient_y.append(float(data[2]))
        orient_z.append(float(data[3]))
        if len(orient_x)>=10:
            x1.pop(0)
            orient_x.pop(0)
            orient_y.pop(0)
            orient_z.pop(0)
        ax1.clear()
        ax1.set_ylabel('Orientation - (degrees)')
        ax1.set_xlabel('Time - (samples)')
        ax1.set_ylim([-360, 360])
        ax1.plot(x1, orient_x, label = "x")
        ax1.plot(x1, orient_y, label = "y")
        ax1.plot(x1, orient_z, label = "z")
    if data[0]=="Accl":
        x2.append(index)
        accel_x.append(float(data[1]))
        accel_y.append(float(data[2]))
        accel_z.append(float(data[3]))
        if len(accel_x)>=10:
            x2.pop(0)
            accel_x.pop(0)
            accel_y.pop(0)
            accel_z.pop(0)
        ax2.clear()
        ax2.set_xlabel('Time - (samples)')
        ax2.set_ylabel('Accelerometer - (m/s^2)')
        ax2.set_ylim([-15, 15])
        ax2.plot(x2, accel_x, label = "x")
        ax2.plot(x2, accel_y, label = "y")
        ax2.plot(x2, accel_z, label = "z")
    if data[0]=="Temp":
        temp.append(float(data[1]))
ani = animation.FuncAnimation(fig, animate, interval=10)
plt.show()
