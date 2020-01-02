import numpy as np
from math import *
ax=
ay=
az=

j = np.array([cos(ay)*cos(az), -sin(az)*cos(ax)+sin(ax)*sin(ay)*cos(az), sin(ax)*sin(az)+cos(ax)*sin(ay)*cos(az)]
[cos(ay)*sin(az), cos(az)*cos(ax)+sin(ax)*sin(ay)*sin(az), -sin(ax)*cos(az)+cos(ax)*sin(ay)*sin(az)]
[-sin(ay), cos(ay)*sin(ax), cos(ax)*cos(ay)])

def Euler_J(j,ax,ay,az):
    j[0,0]=cos(ay)*cos(az)
    j[0,1]=-sin(az)*cos(ax)+sin(ax)*sin(ay)*cos(az)
    j[0,2]=sin(ax)*sin(az)+cos(ax)*sin(ay)*cos(az)
    j[1,0]=cos(ay)*sin(az)
    j[1,1]=sin(az), cos(az)*cos(ax)+sin(ax)*sin(ay)*sin(az)
    j[1,2]=-sin(ax)*cos(az)+cos(ax)*sin(ay)*sin(az)
    j[2,0]=-sin(ay)
    j[2,1]=cos(ay)*sin(ax)
    j[2,2]=cos(ax)*cos(ay)