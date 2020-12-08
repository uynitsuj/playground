import matplotlib.pyplot as plt
import serial
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import time
ser = serial.Serial('/dev/ttyUSB0', 500000)
print(ser)
if ser.is_open==False :
    print("no BNO055 detected")
else:
    print("BNO055 detected")

class BNO:
    def __init__(self, x, y, z, roll, pitch, yaw):
        self.x = x
        self.y = y
        self.z = z
        self.dx = x
        self.dy = y
        self.dz = z
        self.roll = roll
        self.yaw = yaw
        self.pitch = pitch
        self.pointset = [x,y,z]
        self.pose = [[1,0,0,x],
                     [0,1,0,y],
                     [0,0,1,z],
                     [0,0,0,1]]
        self.I = [[1,0,0,0],
                [0,1,0,0],
                [0,0,1,0],
                [0,0,0,1]]

    def translate(self, dx, dy, dz):
        return [[1,0,0,dx],
                [0,1,0,dy],
                [0,0,1,dz],
                [0,0,0,1]]
    def rotate(self, yaw, pitch, roll):
        return [[np.cos(yaw)*np.cos(pitch),np.cos(yaw)*np.sin(pitch)*np.sin(roll)-np.sin(yaw)*np.cos(roll),np.cos(yaw)*np.sin(pitch)*np.cos(roll)+np.sin(yaw)*np.sin(roll),0],
        [np.sin(yaw)*np.cos(pitch),np.sin(yaw)*np.sin(pitch)*np.sin(roll)+np.cos(yaw)*np.cos(roll),np.sin(yaw)*np.sin(pitch)*np.cos(roll)-np.cos(yaw)*np.sin(roll),0],
        [-np.sin(pitch),np.cos(pitch)*np.sin(roll),np.cos(pitch)*np.cos(roll),0],
        [0,0,0,1]]

    def addpoint(self):
        #print(self.dz)
        self.pose = np.dot(self.translate(self.pose[0][3], self.pose[1][3], self.pose[2][3]),
        np.dot(self.rotate(self.yaw, self.pitch, self.roll),
        np.dot(self.translate(self.dx, self.dy, self.dz),
        self.I)))
        #print(self.pose)

        self.x = self.pose[0][3]
        self.y = self.pose[1][3]
        self.z = 0
        self.pointset = [self.x, self.y, self.z]

    def core(self, new_data):
        del_time = 0.2
        #print(new_data)
        if new_data[0] == 'Accl':
                velx= float(new_data[1]) * del_time
                vely= float(new_data[2]) * del_time
                velz= (float(new_data[3])) * del_time
                self.dx = (float(new_data[1])*0.5*del_time*del_time+velx*del_time)
                self.dy = (float(new_data[2])*0.5*del_time*del_time+vely*del_time)
                #self.dz = ((float(new_data[3]))*0.5*del_time*del_time+vely*del_time)
                self.dz = 0
        if new_data[0] == 'Orient':
                self.roll = (float(new_data[1]))
                self.pitch = (float(new_data[2]))
                self.yaw = (float(new_data[3]))
        self.addpoint()

def update_line(hl, new_data):
    xdata, ydata, zdata = hl._verts3d
    hl.set_xdata(list(np.append(xdata, new_data[0])))
    hl.set_ydata(list(np.append(ydata, new_data[1])))
    hl.set_3d_properties(list(np.append(zdata, new_data[2])))
    plt.draw()

map = plt.figure()
map_ax = Axes3D(map)
#map_ax.autoscale(enable=True, axis='both', tight=True)

# # # Setting the axes properties
map_ax.set_xlim3d([-1.5, 1.5])
map_ax.set_ylim3d([-1.5, 1.5])
map_ax.set_zlim3d([0.0, 1])
map_ax.set_xlabel('m')
map_ax.set_ylabel('m')
map_ax.set_zlabel('m')

hl, = map_ax.plot3D([0],[0],[0])
imu = BNO(0,0,0,0,0,0)
while True:
    imu.core(new_data = ser.readline().split(","))
    #print(imu.pointset)
    update_line(hl,imu.pointset)
    plt.show(block=False)
    plt.pause(0.01)
plt.close('all')
