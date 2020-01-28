import Replayer
import threading

def body_tilt(messages,lock,t,s,ax,ay,az,x,y,z):
    body_lean = ay-270
    print(body_lean)

    if body_lean > 10 or body_lean < 0:
        lock.acquire()
        messages['Body_Tilt'] = body_lean
        lock.release()

if __name__ == "__main__":
    messages = {}
    lock = threading.Lock()
    Replayer.live(body_tilt,messages,lock)