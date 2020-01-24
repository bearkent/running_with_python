#print("4")
#print("zkhgngiurh")

#for i in range(0,5):
#   print(i)
import Replayer

s = Replayer.speed_for_replayer

#s = str(s)

s = bytes.fromhex(str(s)).decode('ascii')

print(s)