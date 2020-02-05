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

def say(str):
    global engine
    engine.say(str)
    engine.runAndWait()

# lock is used to make sure that only one thread is changing messages at a time
lock = threading.Lock()
# messages contains a set of things to do
messages = {}

def fx(messages,lock,t,s,ax,ay,az,x,y,z):
    #info for threading functions
    Body_Tilt.body_tilt(messages,lock,t,s,ax,ay,az,x,y,z)

    Cadence_Overstriding_Speed.Cadence(messages,lock,t,s,ax,ay,az,x,y,z)

    GPS.speed(messages,lock,t,ax,ay,az,x,y,z)

    

# data is the function that generates things to do (messages)
def data(fx,messages,lock):
    live(fx,messages,lock)

def output(n,messages,lock):

    snd_strs = {
        'Body_Tilt':'Your body tilt is {0}.',
        'Cadence':'Your cadence is {0}.',
        'Speed':'Your speed is {0} miles per hour.'
        }

    while True:
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
        for k,v in msgs.items():
            print("{0},{1}".format(k,v))
            fs = snd_strs[k]
            ss = fs.format(v)
            print(ss)
            say(ss)

        #change to 30 for after stem fair
        sleep(3)


ndata = 1000000
noutput = 1000*ndata

threadData = threading.Thread(target=data, args=(fx,messages,lock,))
threadData.start()

threadOutput = threading.Thread(target=output, args=(noutput,messages,lock,))
threadOutput.start()

threadData.join()
threadOutput.join()