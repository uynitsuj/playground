import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

class QC:
    def __init__(self, ax, x, y, z, roll, pitch, yaw):
        self.ax = ax
        self.x = x
        self.y = y
        self.z = z
        self.roll = roll
        self.pitch = pitch
        self.yaw = yaw
        self.pointset = [[self.x,self.y,self.z], [1,2,3], [2,3,3]]
        self.pose = [[0,0,0,self.x],
                    [0,0,0,self.y],
                    [0,0,0,self.z],
                    [0,0,0,0]]
    #def addpoint(self):
    #def transform():
    def draw(self):
        x_data = [vector[0] for vector in self.pointset]
        y_data = [vector[1] for vector in self.pointset]
        z_data = [vector[2] for vector in self.pointset]
        self.ax.plot(x_data, y_data, z_data)


fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
quadcopter = QC(ax,0,0,0,0,0,0)
quadcopter.draw()

plt.show()
