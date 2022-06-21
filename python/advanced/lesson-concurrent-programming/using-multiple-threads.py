# introduction to using multithreading in python using simple timer functions

import time
import threading

def greeting_with_sleep(string):
  print(string)
  time.sleep(2)
  print("says hello!")


def main_threading():
  s = time.perf_counter()
  greetings = ['Codecademy', 'Chelsea', 'Hisham', 'Ashley']
  threads = []
  for i in range(len(greetings)):
    # create thread
    t = threading.Thread(target=greeting_with_sleep, args=(greetings[i],))
    # add thread to threads list
    threads.append(t)
    # start thread
    t.start()

  elapsed = time.perf_counter() - s
  print("Threading Elapsed Time: " + str(elapsed) + " seconds")


main_threading()
