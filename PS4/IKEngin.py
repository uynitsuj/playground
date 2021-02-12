from numpy import *  # imports all function so we don't have to use np.function()
import math
import numpy as np
import pyqtgraph.opengl as gl
import pyqtgraph as pg
# class defines robot joint vertices and stores & plots vertex definition
# in cartesian space relative to the origin of the base frame
# those vertices get plotted within MPL's 3d visualization plotter using their plot function.


class Quadruped:

    def __init__(self, ax=0, origin=(0, 0, 100), body_dim=(230, 78), limb_lengths=(107, 130), offsets=(10, 60), height=170):
        '''
        body_dim: (length, width,thickness) in mm
        limb_lengths: (upper_arm, bottom_arm) in mm
        offsets: (z_offset, y_offset) in mm
        '''
        self.ax = ax
        self.body_dim = body_dim
        self.limb_lengths = limb_lengths
        self.offsets = offsets
        self.init_origin = origin
        self.origin = origin
        self.yaw = 0
        self.pitch = 0
        self.roll = 0
        self.height = height

        #list of tuples of body frame coordinates in R3 cartesian
        self.body = [(origin[0] - self.body_dim[0] / 2,
                      origin[1] - self.body_dim[1] / 2, origin[2]),
                     (origin[0] + self.body_dim[0] / 2,
                      origin[1] - self.body_dim[1] / 2, origin[2]),
                     (origin[0] + self.body_dim[0] / 2,
                      origin[1] + self.body_dim[1] / 2, origin[2]),
                     (origin[0] - self.body_dim[0] / 2,
                      origin[1] + self.body_dim[1] / 2, origin[2]),
                     (origin[0] - self.body_dim[0] / 2,
                      origin[1] - self.body_dim[1] / 2, origin[2])]

        self.body_reset = [(origin[0] - self.body_dim[0] / 2,
                      origin[1] - self.body_dim[1] / 2, origin[2]),
                     (origin[0] + self.body_dim[0] / 2,
                      origin[1] - self.body_dim[1] / 2, origin[2]),
                     (origin[0] + self.body_dim[0] / 2,
                      origin[1] + self.body_dim[1] / 2, origin[2]),
                     (origin[0] - self.body_dim[0] / 2,
                      origin[1] + self.body_dim[1] / 2, origin[2]),
                     (origin[0] - self.body_dim[0] / 2,
                      origin[1] - self.body_dim[1] / 2, origin[2])]

    def draw_body(self, color='black'):
        x_data = [vector[0] for vector in self.body]
        y_data = [vector[1] for vector in self.body]
        z_data = [vector[2] for vector in self.body]
        #self.ax.plot(x_data, y_data, z_data, color=color)
        pts = vstack([x_data, y_data, z_data]).transpose()
        self.ax.w.addItem(gl.GLLinePlotItem(pos=pts, color=pg.glColor((4, 50)), width=1, antialias=True))

    @staticmethod
    def translate(delx, dely, delz):
        return [[1,0,0,delx],
                [0,1,0,dely],
                [0,0,1,delz],
                [0,0,0,1]]

    @staticmethod
    def rotate(yaw, pitch, roll):
        return [[cos(yaw)*cos(pitch),
        cos(yaw)*sin(pitch)*sin(roll)-sin(yaw)*cos(roll),
        cos(yaw)*sin(pitch)*cos(roll)+sin(yaw)*sin(roll),0],


        [sin(yaw)*cos(pitch),
        sin(yaw)*sin(pitch)*sin(roll)+cos(yaw)*cos(roll),
        sin(yaw)*sin(pitch)*cos(roll)-cos(yaw)*sin(roll),0],


        [-sin(pitch),
        cos(pitch)*sin(roll),
        cos(pitch)*cos(roll),0],
        [0,0,0,1]]

    def shift_body_rotation(self, yaw, pitch, roll):
        self.yaw = yaw
        self.pitch = pitch
        self.roll = roll
        for i, vector in enumerate(self.body):
            P = dot(Quadruped.translate(0, 0, self.body_reset[i][2]), dot(Quadruped.rotate(self.yaw, self.pitch, self.roll), Quadruped.translate(self.body_reset[i][0],self.body_reset[i][1],0)))
            self.body[i] = (P[0][3], P[1][3], P[2][3])
            #print((P[0][3], P[1][3], P[2][3]))
            #print(self.body_reset[i])
