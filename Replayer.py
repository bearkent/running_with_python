from sense_hat import SenseHat
import time
import csv
import gps
import pyttsx3

engine = pyttsx3.init()

session = gps.gps("localhost", "2947")
session.stream(gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)
 
while True:
    try:
        report = session.next()
        if report['class'] == 'TPV':
            if hasattr(report, 'speed'):
                s = report.speed
                s = round(s)
                print(s)
    except KeyError:
        pass
    except KeyboardInterrupt:
        quit()
    except StopIteration:
        session = None

def record(file):
    red=(255,0,0)
    white=(255,255,255)
    sense = SenseHat()
 
    sense.show_letter("W",text_colour=red,back_colour=white)
    sense.stick.wait_for_event()

    sense.show_letter("R",text_colour=red,back_colour=white)
    

    with open(file,"w") as f:
        writer = csv.writer(f)
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
            s = round(report.speed)
            writer.writerow([t,s,ax,ay,az,x,y,z])

            events = sense.stick.get_events()

            for event in events:
                if event.action == "pressed":
                    sense.clear()
                    return


def replay(file, fx):
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
            s = int(row[7])
            fx(t,s,ax,ay,az,x,y,z)

def live(fx):
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
        s = round(report.speed)
        fx(t,s,ax,ay,az,x,y,z)
