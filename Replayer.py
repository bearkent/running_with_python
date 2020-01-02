from sense_hat import SenseHat
import time

sense = SenseHat()
acceleration = sense.get_accelerometer_raw()

def record(file):
    with open(file,"wb") as f:
        read_data = f.read
        while True:
            t=int(round(time.time()*1000))
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
        read_data = f.read()
        while True:
            t = f.read()
            ax = f.read()
            ay = f.read()
            az = f.read()
            x = acceleration['x']
            y = acceleration['y']
            z = acceleration['z']
            fx(t,ax,ay,az,x,y,z)