import threading

# lock is used to make sure that only one thread is changing messages at a time
lock = threading.Lock()
# messages contains a set of things to do
messages = set()

# data is the function that generates things to do (messages)
def data(n):
  global messages

  for i in range(n):
    m = "MESSAGE-{0}".format(i)
    print("data: {0}".format(m))
    # have to get the lock so that only one thread changes messages at a time
    lock.acquire()
    messages.add(m)
    # have to release the lock or the other thread will wait forever on it
    lock.release()

# output is the function that gets the messages and does something with them
def output(n):
  global messages

  for i in range(n):
    # have to get the lock so that only one thread changes messages at a time
    lock.acquire()
    # making a copy of the messages, which is fast, so that the data thread
    # does not get slowed down
    msgs = messages.copy()
    messages.clear()
    # have to release the lock or the other thread will wait forever on it
    lock.release()

    # now do something with the messages.  This can be really slow, and that
    # doesn't make your data thread slow
    for m in msgs:
      print("output: {0} {1}".format(i,m))

ndata = 100
noutput = 1000*ndata

threadData = threading.Thread(target=data, args=(ndata,))
threadData.start()

threadOutput = threading.Thread(target=output, args=(noutput,))
threadOutput.start()


