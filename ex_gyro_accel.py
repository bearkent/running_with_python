from sense_hat import SenseHat
import time

# https://www.sigmaelectronica.net/wp-content/uploads/2017/11/RPI-guia.pdf
# https://projects.raspberrypi.org/en/projects/getting-started-with-the-sense-hat/9

sense = SenseHat()

while True:
  acceleration = sense.get_accelerometer_raw()
  x = acceleration['x']
  y = acceleration['y']
  z = acceleration['z']

  #x=x*360
  #y=y*360
  #z=z*360

  print("x={0}, y={1}, z={2}".format(x, y, z))
  
  o = sense.get_orientation()
  pitch = o["pitch"]
  roll = o["roll"]
  yaw = o["yaw"]
  print("pitch {0} roll {1} yaw {2}".format(pitch, roll, yaw))
  time.sleep(2)
