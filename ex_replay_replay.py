import Replayer

def get_body_tilt(t, ax, ay, az, x, y, z):
    Body_Tilt = 360-ax
    print("Body tilt is"+Body_Tilt+"degrees")

Replayer.replay("test.bin",get_body_tilt)