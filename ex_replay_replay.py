import Replayer

def get_body_tilt(t, ax, ay, az, x, y, z):
    Body_Tilt = 360-ax
    print("Body tilt is {0} degrees".format(Body_Tilt))

Replayer.replay("test.csv",get_body_tilt)