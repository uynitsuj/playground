#import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px
import numpy as np
#from mpl_toolkits.mplot3d import Axes3D
from FIR import fir
import time

filename = 'log100sel.csv'
data = np.genfromtxt(filename, delimiter=",", dtype="|U10", usecols=(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

class QC:
    def __init__(self, x, y, z, roll, pitch, yaw, data):
        self.x = x
        self.y = y
        self.z = z
        self.dx = x
        self.dy = y
        self.roll = roll
        self.yaw = yaw
        self.pitch = pitch
        self.pointset = [[x,y,z]]
        self.LiDARptset = []
        self.pose = [[1,0,0,x],
                     [0,1,0,y],
                     [0,0,1,z],
                     [0,0,0,1]]
        self.LiDAR = [[1,0,0,x],
                     [0,1,0,y],
                     [0,0,1,z],
                     [0,0,0,1]]
        self.prx= [0,0,0,0]
        self.data = data
        self.I = [[1,0,0,0],
                [0,1,0,0],
                [0,0,1,0],
                [0,0,0,1]]

    def translate(self, dx, dy):
        return [[1,0,0,dx],
                [0,1,0,dy],
                [0,0,1,0],
                [0,0,0,1]]
    def rotate(self, yaw, pitch, roll):
        return [[np.cos(yaw)*np.cos(pitch),
        np.cos(yaw)*np.sin(pitch)*np.sin(roll)-np.sin(yaw)*np.cos(roll),
        np.cos(yaw)*np.sin(pitch)*np.cos(roll)+np.sin(yaw)*np.sin(roll),0],


        [np.sin(yaw)*np.cos(pitch),
        np.sin(yaw)*np.sin(pitch)*np.sin(roll)+np.cos(yaw)*np.cos(roll),
        np.sin(yaw)*np.sin(pitch)*np.cos(roll)-np.cos(yaw)*np.sin(roll),0],


        [-np.sin(pitch),
        np.cos(pitch)*np.sin(roll),
        np.cos(pitch)*np.cos(roll),0],
        [0,0,0,1]]

    def addpoint(self):
        self.pose = np.dot(self.translate(self.pose[0][3], self.pose[1][3]),
        np.dot(self.rotate(self.yaw, self.pitch, self.roll),
        np.dot(self.translate(self.dx, self.dy),
        self.I)))

        self.x = self.pose[0][3]
        self.y = self.pose[1][3]
        for i in range(0,4):
            self.LiDAR = np.dot(self.translate(self.pose[0][3], self.pose[1][3]),
            np.dot(self.rotate(self.yaw+(i*np.pi/2), self.pitch, self.roll),
            np.dot(self.translate(self.prx[i], 0),
            self.I)))
            self.LiDARptset.append([self.LiDAR[0][3]/10,self.LiDAR[1][3]/10,self.z])
        self.pointset.append([self.x, self.y, self.z])

    def update_line(self, hl, new_data):
    	xdata, ydata, zdata = hl._verts3d
    	hl.set_xdata(list(np.append(xdata, new_data[0])))
    	hl.set_ydata(list(np.append(ydata, new_data[1])))
    	hl.set_3d_properties(list(np.append(zdata, new_data[2])))
    	plt.draw()

    def core(self):
        a=0
        del_time = 0.000001
        time = float(self.data[0][1])
        ATT = []
        filter = fir(5)
        for i in range(1,self.data.shape[0]):
            if self.data[i][0] == 'PRX':
                a+=1
                self.prx = [float(self.data[i][3]),
                float(self.data[i][5]),
                float(self.data[i][7]),
                float(self.data[i][9])]
            if self.data[i][0] == 'IMU':
                a+=1
                newTime = float(self.data[i][1])
                velx= float(self.data[i][5]) * del_time
                vely= float(self.data[i][6]) * del_time
                self.dx = (float(self.data[i][5])*0.5*del_time*del_time+velx*del_time)
                self.dy = (float(self.data[i][6])*0.5*del_time*del_time+vely*del_time)
                del_time = (newTime-time) * 0.000001
                time=newTime
            if self.data[i][0] == 'CTUN':
                a+=1
                self.z=filter.apply_sma(float(data[i][10]) - 0.19)
            if self.data[i][0] == 'ATT':
                a+=1
                self.roll = ((float(self.data[i][3])*np.pi/180))
                self.pitch = ((float(self.data[i][5])*np.pi/180))
                self.yaw = ((float(self.data[i][7])*np.pi/180))
            if a>=1:
                self.addpoint()
                a=0

qc = QC(0,0,0,0,0,0, data)
qc.core()

x= [row[0] for row in qc.LiDARptset]
y= [row[1] for row in qc.LiDARptset]
z= [row[2] for row in qc.LiDARptset]
fig = go.Figure()
fig.add_trace(go.Scatter3d(
    x=x,
    y=y,
    z=z,
    mode='markers',
    marker=dict(
        size=2,
        color=z,                # set color to an array/list of desired values
        colorscale='Viridis',   # choose a colorscale
        opacity=0.3
    )
))
xp = [row[0] for row in qc.pointset]
yp = [row[1] for row in qc.pointset]
zp = [row[2] for row in qc.pointset]
fig.add_trace(go.Scatter3d(
    x=xp, y=yp, z=zp,
    marker=dict(
        size=0.1,
        colorscale='Viridis',
    ),
    line=dict(
        color='darkblue',
        width=3
    )
))

fig.update_layout(
    width=1800,
    height=1000,
    autosize=False,

    scene=dict(
        xaxis_title='X (Meters)',
        yaxis_title='Y (Meters)',
        zaxis_title='Z (Meters)',
        camera=dict(
            up=dict(
                x=0,
                y=0,
                z=1
            ),
            eye=dict(
                x=0,
                y=1.0707,
                z=1,
            )
        ),
        aspectratio = dict( x=1, y=1, z=0.7 ),
        aspectmode = 'manual'
    ),
)

fig.show()
