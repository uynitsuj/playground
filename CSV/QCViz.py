import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from FIR import fir

filename = 'LOG90.csv'
data = np.genfromtxt(filename, delimiter=",", dtype="|U10", usecols=(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10))


#IMU[i][1] timestep
#IMU[i][2] GyrX (rad/s)
#IMU[i][3] GyrY
#IMU[i][4] GyrZ
#IMU[i][5] AccX (m/s/s)
#IMU[i][6] AccY
#IMU[i][7] AccZ
#PRX[i][1] timestep
#PRX[i][3] D0 (decimeters) 1 dm = 0.1 m
#PRX[i][5] D90
#PRX[i][7] D180
#PRX[i][9] D270
#ATT[i][3] Roll
#ATT[i][5] Pitch
#ATT[i][7] Yaw
'''

      pos=pos.plus(acc.multiply(0.5f*del_time*del_time).plus(vel.multiply(del_time)).multiply(10.0f));
      //println(pos);
      pos.z(10.0f*ultra.get(num).get(1));
      vel = vel.plus(acc.multiply(del_time));
      orient=orient.plus(new Vec(imu.get(num).get(1),imu.get(num).get(2),imu.get(num).get(3)).multiply(del_time));
      time=newTime;

'''

class QC:
    def __init__(self, ax, x, y, z, roll, pitch, yaw, data):
        self.ax = ax
        self.x = x
        self.y = y
        self.z = z
        self.dx = x
        self.dy = y
        self.roll = roll
        self.pitch = pitch
        self.yaw = yaw
        self.pointset = [[x,y,z]]
        self.poseset = []
        self.pose = [[1,0,0,x],
                     [0,1,0,y],
                     [0,0,1,z],
                     [0,0,0,1]]
        self.PRX = []
        self.data = data

    def translate(self, dx, dy):
        return [[1,0,0,dx],
                [0,1,0,dy],
                [0,0,1,0],
                [0,0,0,1]]
    def rotate(self, yaw, pitch, roll):
        return [[np.cos(yaw)*np.cos(pitch),np.cos(yaw)*np.sin(pitch)*np.sin(roll)-np.sin(yaw)*np.cos(roll),np.cos(yaw)*np.sin(pitch)*np.cos(roll)+np.sin(yaw)*np.sin(roll),self.x],
        [np.sin(yaw)*np.cos(pitch),np.sin(yaw)*np.sin(pitch)*np.sin(roll)+np.cos(yaw)*np.cos(roll),np.sin(yaw)*np.sin(pitch)*np.cos(roll)-np.cos(yaw)*np.sin(roll),self.y],
        [-np.sin(pitch),np.cos(pitch)*np.sin(roll),np.cos(pitch)*np.cos(roll),self.z],
        [0,0,0,1]]

    def addpoint(self):
        self.pose = np.dot(self.translate(self.dx, self.dy),self.rotate(self.yaw, self.pitch, self.roll))
        self.poseset.append(self.pose)
        self.x = self.pose[0][3]
        self.y = self.pose[1][3]
        self.pointset.append([self.x, self.y, self.z])
    def drawQCpath(self):
        x_data = [vector[0][3] for vector in self.poseset]
        y_data = [vector[1][3] for vector in self.poseset]
        z_data = [vector[2][3] for vector in self.poseset]
        orr11 = [vector[0][0] for vector in self.poseset]
        orr21 = [vector[1][0] for vector in self.poseset]
        orr31 = [vector[2][0] for vector in self.poseset]
        orr12 = [vector[0][1] for vector in self.poseset]
        orr22 = [vector[1][1] for vector in self.poseset]
        orr32 = [vector[2][1] for vector in self.poseset]
        orr13 = [vector[0][2] for vector in self.poseset]
        orr23 = [vector[1][2] for vector in self.poseset]
        orr33 = [vector[2][2] for vector in self.poseset]
        self.ax.plot(x_data, y_data, z_data)
        #ax.quiver(x_data, y_data, z_data, x_data+self.poseset[0][0], y_data+self.poseset[0][1], z_data+self.poseset[0][2])
        for i in range(1,len(x_data)):
            ax.quiver(x_data[i], y_data[i], z_data[i], x_data[i]+orr11[i], y_data[i]+orr21[i], z_data[i]+orr31[i], normalize = True, length = 0.01, color = "blue", arrow_length_ratio = 0.0001)
            ax.quiver(x_data[i], y_data[i], z_data[i], x_data[i]+orr12[i], y_data[i]+orr22[i], z_data[i]+orr32[i], normalize = True, length = 0.01, color = "green", arrow_length_ratio = 0.0001)
            ax.quiver(x_data[i], y_data[i], z_data[i], x_data[i]-orr13[i], y_data[i]-orr23[i], z_data[i]+orr33[i], normalize = True, length = 0.01, color = "red", arrow_length_ratio = 0.0001)
    def core(self):
        a=0
        del_time = 0.000001
        time = float(self.data[0][1])
        ATT = []
        filter = fir(4)
        for i in range(1,self.data.shape[0]):
            if self.data[i][0] == 'PRX':
                a+=1
                self.PRX.append(data[i,:])
            if self.data[i][0] == 'IMU':
                newTime = float(self.data[i][1])
                velx= float(self.data[i][5]) * del_time
                vely= float(self.data[i][6]) * del_time
                self.dx = (float(self.data[i][5])*0.5*del_time*del_time+velx*del_time)
                self.dy = (float(self.data[i][6])*0.5*del_time*del_time+vely*del_time)
                del_time = (newTime-time) * 0.000001
                time=newTime
            if self.data[i][0] == 'CTUN':
                self.z=(float(data[i][10]) - 0.19)
            if self.data[i][0] == 'ATT':
                self.roll = ((float(self.data[i][3])*np.pi/180)-self.roll)
                self.pitch = ((float(self.data[i][5])*np.pi/180)-self.pitch)
                self.yaw = ((float(self.data[i][7])*np.pi/180)-self.yaw)
            if a==1:
                self.addpoint()
                a=0

fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")

ax.set_xlabel('X (m)')
ax.set_ylabel('Y (m)')
ax.set_zlabel('Z (m)')
ax.set_xlim3d(-0.25,0.25)
ax.set_ylim3d(-0.25,0.25)
ax.set_zlim3d(0,0.5)
quadcopter = QC(ax,0,0,0,0,0,0, data)
quadcopter.core()
quadcopter.pointset
quadcopter.poseset
quadcopter.drawQCpath()

plt.show()
