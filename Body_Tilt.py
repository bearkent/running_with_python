import Replayer

def body_tilt(t,ax,ay,az,x,y,z):
    body_lean = ay-270
    print(body_lean)

if __name__ == "__main__":
    Replayer.live(body_tilt)