import threading

n = 100

def printStuff(s):
    for i in range(n):
        print("{0}: {1}".format(s,i))

t1 = threading.Thread(target=printStuff, args=("A",))
t2 = threading.Thread(target=printStuff, args=("B",))

t1.start()
t2.start()

t1.join()
t2.join()