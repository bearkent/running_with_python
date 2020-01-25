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

Body_Tilt = Body_Tilt.body_tilt
Cadence = Cadence_Overstriding_Speed.Cadence
Speed = GPS.Speed
#overstriding

# lock is used to make sure that only one thread is changing messages at a time
lock = threading.Lock()
# messages contains a set of things to do
messages = {Body_Tilt:body_lean,Cadence:cadence,Speed:s}

# data is the function that generates things to do (messages)
def data(n):
  global messages

  for i in range(n):
    m = "MESSAGE-{0}".format(i)
    print("data: {0}".format(m))
    # have to get the lock so that only one thread changes messages at a time
    lock.acquire()
    messages.append(m)
    # have to release the lock or the other thread will wait forever on it
    lock.release()

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

ndata = 100
noutput = 1000*ndata

threadData = threading.Thread(target=data, args=(ndata,))
threadData.start()

threadOutput = threading.Thread(target=output, args=(noutput,))
threadOutput.start()
