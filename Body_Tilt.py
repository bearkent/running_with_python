from sense_hat import SenseHat
import time

sense = SenseHat()

while True:
    o = sense.get_orientation()
    pitch = o["pitch"]
    d=open("Aftter_Run_Data.bin","wb")
    d.write()