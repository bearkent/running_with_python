import Audio
import threading
from Replayer import live
import Cadence_Overstriding_Speed
import Body_Tilt
import Speed_Stride_Length
import time
from sense_hat import SenseHat
import os

dic_cad = {}
dic_tilt = {}
dic_over_stride = {}

tlast = 0
vlastx = 0
plastx = 0
vlasty = 0
plasty = 0
vlastz = 0
plastz = 0
leftRange = True
lock = threading.Lock()

def fx(t,ax,ay,az,x,y,z):
    global lock,tlast,vlastx,plastx,vlasty,plasty,vlastz,plastz,leftRange
    sense = SenseHat()
    acceleration = sense.get_accelerometer_raw()
    t=time.time_ns()
    o = sense.get_orientation()
    ax = o["pitch"]
    ay = o["roll"]
    az = o["yaw"]
    x = acceleration['x']
    y = acceleration['y']
    z = acceleration['z']
    tlast = 0
    vlastx = 0
    plastx = 0
    vlasty = 0
    plasty = 0
    vlastz = 0
    plastz = 0
    leftRange = True

    lock.acquire({blocking=True})
    dic_cad["cad"] = Cadence_Overstriding_Speed.Cadence(t,ax,ay,az,x,y,z)
    dic_tilt["tilt"] = Body_Tilt.body_tilt(t,ax,ay,az,x,y,z)
    dic_over_stride["over_stride"] = Cadence_Overstriding_Speed.overstriding(t,ax,ay,az,x,y,z)
    lock.release()

def data_collection(fx):
    live(fx)

def audio_running(dic1,dic2,dic3):
    
    if dic1 < 180:
        os.system("mpg321 cadence.mp3")
        break

    if dic2 > 6:
        os.system("mpg321 decrease_tilt.mp3")
        break
    
    elif dic2 < 4:
        os.system("mpg321 increase_tilt.mp3")
        break

    else:
        break

    if dic3:
        os.system("mpg321 overstriding2.mp3")

thread1 = threading.Thread(target=data_collection, args=(fx,))
thread2 = threading.Thread(target= audio_running, args=(dic1,dic2,dic3,))

thread1.start()
thread2.start()

thread1.join()
thread2.join()