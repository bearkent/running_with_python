from time import sleep
import pyttsx3
import Audio
import threading
from Replayer import live
import Cadence_Overstriding_Speed
import Body_Tilt
import Speed_Stride_Length
import time
from sense_hat import SenseHat
import os
import GPS

engine = pyttsx3.init()
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

body_lean = Body_Tilt.body_tilt
cadence = Cadence_Overstriding_Speed.Cadence
s = GPS.speed
#overstriding

# lock is used to make sure that only one thread is changing messages at a time
lock = threading.Lock()
# messages contains a set of things to do
messages = {'Body_Tilt':body_lean,'Cadence':cadence,'Speed':s,"Messages":"empty"}

def data_for_data(fx1,fx2,fx3):
    global t,s,ax,ay,az,x,y,z

    a = fx1(t,ax,ay,az,x,y,z)
    b = fx2(t,ax,ay,az,x,y,z)
    c = fx3(t,s,ax,ay,az,x,y,z)

    global l
    l = []
    l = l.append(a,b,c)

# data is the function that generates things to do (messages)
def data(n):
    global messages
    for i in  range(n):
        m = "MESSAGE-{0}".format(i)
        print("data: {0}".format(m))
        # have to get the lock so that only one thread changes messages at a time
        lock.acquire()
        messages["Messages"] = m
        # have to release the lock or the other thread will wait forever on it
        lock.release()

def data_for_output(fx1,fx2,fx3):
    return data(data_for_data(fx1,fx2,fx3))

# output is the function that gets the messages and does something with them
def output(n):
    global messages

    for i in range(n):
        # have to get the lock so that only one thread changes messages at a time
        lock.acquire()
        # making a copy of the messages, which is fast, so that the data thread
        # does not get slowed down
        msgs = messages.copy()
        messages.clear()
        # have to release the lock or the other thread will wait forever on it
        lock.release()

        # now do something with the messages.  This can be really slow, and that
        # doesn't make your data thread slow
    for m in msgs:
        print("output: {0} {1}".format(i,m))
        global sound_vars
        sound_vars = {}
        sound_vars.update({m:i})
        for var in sound_vars:
            dta = sound_vars
            key = list(dta.keys())[list(dta.values()).index(i)]
            val = dta[key]

            if key == 'Body_tilt':
                if val < 4:
                    Audio.increase_tilt_audio
                    dta.clear()
            elif val > 6:
                    Audio.decrease_tilt_audio
                    dta.clear
            elif key == 'Cadence':
                if val < 180:
                    Audio.cadence_audio
                    dta.clear()
            elif key == 'speed':
                Audio.speed_audio
                dta.clear()
            else:
                dta.clear()

        sleep(30)

#def audio(b,c,s):
#    while True:
#        if b > 5:
#            Audio.decrease_tilt_audio
#        elif b < 5:
#            Audio.increase_tilt_audio
#        elif c < 180:
#            Audio.cadence_audio
#        else:
#            Audio.speed_audio
#            sleep(30)
#
ndata = 100
noutput = 1000*ndata

threadData = threading.Thread(target=data, args=(ndata,))
threadData.start()

threadOutput = threading.Thread(target=output, args=(noutput,))
threadOutput.start()

threadData.join()
threadOutput.join()