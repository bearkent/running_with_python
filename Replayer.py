from sense_hat import SenseHat
import time

def record(file):
    sense = SenseHat()
    acceleration = sense.get_accelerometer_raw()

    with open(file,"wb") as f:
        while True:
            t=time.time_ns()
            o = sense.get_orientation()
            ax = o["pitch"]
            ay = o["roll"]
            az = o["yaw"]
            x = acceleration['x']
            y = acceleration['y']
            z = acceleration['z']
            f.write(t)
            f.write(ax)
            f.write(ay)
            f.write(az)
            f.write(x)
            f.write(y)
            f.write(z)

def replay(file, fx):
    with open(file,"rb") as f:
        while True:
            t = f.read()
            ax = f.read()
            ay = f.read()
            az = f.read()
            x = f.read()
            y = f.read()
            z = f.read()
            fx(t,ax,ay,az,x,y,z)

