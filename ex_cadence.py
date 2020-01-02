from sense_hat import SenseHat
import time

# https://www.sigmaelectronica.net/wp-content/uploads/2017/11/RPI-guia.pdf
# https://projects.raspberrypi.org/en/projects/getting-started-with-the-sense-hat/9

sense = SenseHat()

print(time.time())

while True:
  acceleration = sense.get_accelerometer_raw()
  x = acceleration['x']
  y = acceleration['y']
  z = acceleration['z']
