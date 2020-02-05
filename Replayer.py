from sense_hat import SenseHat
import time
import csv
import gps
import pyttsx3
import threading
import GPS

#session = gps.gps("localhost", "2947")
#session.stream(gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)

def record(file):
    red=(255,0,0)
    white=(255,255,255)
    sense = SenseHat()
 
    sense.show_letter("W",text_colour=red,back_colour=white)
    sense.stick.wait_for_event()

    sense.show_letter("R",text_colour=red,back_colour=white)
    sense.stick.wait_for_event()

    event = sense.stick.wait_for_event()

    with open(file,"w") as f:
        writer = csv.writer(f)
        while True:
            acceleration = sense.get_accelerometer_raw()
            messages = {}
            lock = threading.Lock()
            t=time.time_ns()
            o = sense.get_orientation()
            ax = o["pitch"]
            ay = o["roll"]
            az = o["yaw"]
            x = acceleration['x']
            y = acceleration['y']
            z = acceleration['z']
            s = GPS.speed(messages,lock,t,ax,ay,az,x,y,z)
            writer.writerow([messages,lock,t,s,ax,ay,az,x,y,z])

            events = sense.stick.get_events()

            for event in events:
                if event.action == "pressed":
                    sense.clear()
                    break


def replay(file, fx, messages, lock):
    with open(file,"r") as f:
        reader = csv.reader(f)
        for row in reader:
            t = int(row[0])
            ax = float(row[1])
            ay = float(row[2])
            az = float(row[3])
            x = float(row[4])
            y = float(row[5])
            z = float(row[6])
            s = float(row[7])
            fx(messages,lock,t,s,ax,ay,az,x,y,z)

def live(fx, messages, lock):
    sense = SenseHat()

    while True:
        acceleration = sense.get_accelerometer_raw()
        t=time.time_ns()
        o = sense.get_orientation()
        ax = o["pitch"]
        ay = o["roll"]
        az = o["yaw"]
        x = acceleration['x']
        y = acceleration['y']
        z = acceleration['z']
        s = GPS.speed(messages,lock,t,ax,ay,az,x,y,z)
        fx(messages,lock,t,s,ax,ay,az,x,y,z)
