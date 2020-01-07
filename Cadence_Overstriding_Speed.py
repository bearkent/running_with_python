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
    global tlast, vlastx,plastx,vlasty,plasty,vlastz,plastz

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
    tlast = t
    print(dt,y,vlasty,plasty,vlasty*vlasty_old)

    if vlasty*vlasty_old <= 0:
        print("step")

def Cadence2(t,ax,ay,az,x,y,z):
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
    tlast = t
    #print(dt,y,vlasty,plasty,vlasty*vlasty_old)

    if leftRange == False and y < -0.97:
        leftRange = True

    if y > -0.97:
        #print("checking for step")
        if leftRange:
            print("step")
            cadence = 60/dt
            print(cadence)
            leftRange = False

        tlast = t


if __name__ == "__main__":
    Replayer.live(Cadence2)
    Replayer.live(Cadence2)
