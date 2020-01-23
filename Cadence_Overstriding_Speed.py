import Replayer
from time import time
from time import sleep

tlast = 0
vlastx = 0
plastx = 0
vlasty = 0
plasty = 0
vlastz = 0
plastz = 0
leftRange = True

def Cadence(t,ax,ay,az,x,y,z):
    global tlast, vlastx,plastx,vlasty,plasty,vlastz,plastz,leftRange

    if tlast == 0:
        tlast = t
        return

    vlasty_old = vlasty
    dt = (t-tlast)/1.0e9
    vlastx = vlastx+9.8*x*dt
    vlasty = vlasty+9.8*(y-1)*dt
    vlastz = vlastz+9.8*z*dt
    plastx = plastx+vlastx*dt
    plasty = plasty+vlasty*dt
    plastz = plastz+vlastz*dt

    if leftRange == False and y < -0.97:
        leftRange = True

    if y > -0.97:
        if leftRange:
            cadence = 60/dt
            print(cadence)
            leftRange = False
            tlast = t
    
def overstriding(t,ax,ay,az,x,y,z):
    global tlast, vlastx,plastx,vlasty,plasty,vlastz,plastz,leftRange

    if tlast == 0:
        tlast = t
        return

    vlasty_old = vlasty
    dt = (t-tlast)/1.0e9
    vlastx = vlastx+9.8*x*dt
    vlasty = vlasty+9.8*(y-1)*dt
    vlastz = vlastz+9.8*z*dt
    plastx = plastx+vlastx*dt
    plasty = plasty+vlasty*dt
    plastz = plastz+vlastz*dt

    if leftRange == False and y < -0.97:
        leftRange = True

    if y > -0.97:
        if leftRange:
            cadence = 60/dt
            print(cadence)
            leftRange = False
            tlast = t
    



if __name__ == "__main__":
    Replayer.live(Cadence)
