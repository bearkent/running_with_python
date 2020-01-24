import gps
import Replayer
import Audio
import pyttsx3
import time

engine = pyttsx3.init()

session = gps.gps("localhost", "2947")
session.stream(gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)

def speed(t,s,ax,ay,az,x,y,z):

    #session = gps.gps("localhost", "2947")
    #session.stream(gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)

    global engine,session
    session.stream(gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)
    session = gps.gps("localhost", "2947")
    session.stream(gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)


    session = gps.gps("localhost", "2947")
    session.stream(gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)
 
    while True:
        try:
            report = session.next()
        # Wait for a 'TPV' report and display the current time
        # To see all report data, uncomment the line below
        # print(report)
            if report['class'] == 'TPV':
                if hasattr(report, 'speed'):
                    print(report.speed)
                    report.speed=s
                    #s = round(s)      
                    engine.say(s)
                    engine.runAndWait()

        except KeyError:
            pass
        except KeyboardInterrupt:
            quit()
        except StopIteration:
            session = None
            print("GPSD has terminated")

        engine.say(s)
        engine.runAndWait()

if __name__ == "__main__":
    Replayer.live(speed)
