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

    Body_Tilt.body_tilt(messages,lock,t,s,ax,ay,az,x,y,z)

    Cadence_Overstriding_Speed.Cadence(messages,lock,t,s,ax,ay,az,x,y,z)

    GPS.speed(messages,lock,t,ax,ay,az,x,y,z)

    

# data is the function that generates things to do (messages)
def data(fx,messages,lock):
    live(fx,messages,lock)

def output(n):
    global messages

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
            fs = snd_strs[k]
            ss = fs.format(v)
            print(ss)
            say(ss)

        sleep(3)


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
ndata = 1000000
noutput = 1000*ndata

threadData = threading.Thread(target=data, args=(fx,messages,lock,))
threadData.start()

threadOutput = threading.Thread(target=output, args=(noutput,))
threadOutput.start()

threadData.join()
threadOutput.join()