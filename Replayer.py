from sense_hat import SenseHat
import time
import array

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
            f.write(t.to_bytes(8,byteorder="little"))
            a = array.array('d',[ax,ay,az,x,y,z])
            print(a)
            print(a.tobytes())
            f.write(a.tobytes())
            # f.write(ay)
            # f.write(az.to_bytes(8,byteorder="little"))
            # f.write(x.to_bytes(8,byteorder="little"))
            # f.write(y.to_bytes(8,byteorder="little"))
            # f.write(z.to_bytes(8,byteorder="little"))

def replay(file, fx):
    with open(file,"rb") as f:
        while True:
            t = int.from_bytes(f.read(),byteorder="little")
            a = array.array('d')
            b = f.read()
            print(b)
            a.frombytes(b)
            print(a)
            ax = a[0]
            ay = a[1]
            az = a[2]
            x = a[3]
            y = a[4]
            z = a[5]
            # ax = float.from_bytes(f.read(),byteorder="little")
            # ay = float.from_bytes(f.read(),byteorder="little")
            # az = float.from_bytes(f.read(),byteorder="little")
            # x = float.from_bytes(f.read(),byteorder="little")
            # y = float.from_bytes(f.read(),byteorder="little")
            # z = float.from_bytes(f.read(),byteorder="little")
            fx(t,ax,ay,az,x,y,z)

