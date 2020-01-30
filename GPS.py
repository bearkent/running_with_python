import gps
import Replayer
import Audio
import pyttsx3
import time
import threading

session = gps.gps("localhost", "2947")
session.stream(gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)

def speed(messages,lock,t,ax,ay,az,x,y,z):

    #session = gps.gps("localhost", "2947")
    #session.stream(gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)

    global session

    # session.stream(gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)
    # session = gps.gps("localhost", "2947")
    # session.stream(gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)


    # session = gps.gps("localhost", "2947")
    # session.stream(gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)
 
    
    try:
        report = session.next()
        # Wait for a 'TPV' report and display the current time
        # To see all report data, uncomment the line below
        # print(report)
        if report['class'] == 'TPV':
            if hasattr(report, 'speed'):
                print(report.speed)
                s = report.speed
                
                return s

                lock.acquire()
                messages['Speed'] = s
                lock.release()

    except KeyError:
        pass
    except KeyboardInterrupt:
        quit()
    except StopIteration:
        session = None
        print("GPSD has terminated")

        
if __name__ == "__main__":
    messages = {}
    lock = threading.Lock()
    Replayer.live(speed,messages,lock)
