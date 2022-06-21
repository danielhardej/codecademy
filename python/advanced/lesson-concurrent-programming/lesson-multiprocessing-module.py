# multiprocessing
# This module is unique from threading and asyncio in that allows
# the user to leverage multiple processors on a given machine simultaneously.
# This is because instead of threads or asynchronous tasks, multiprocessing is powered by subprocesses.

import time
import multiprocessing

def greeting_with_sleep(string):
  s = time.perf_counter()
  print(string)
  time.sleep(2)
  print("says hello!")
  elapsed = time.perf_counter() - s
  print("Multiprocessing Elapsed Time: " + str(elapsed) + " seconds")

p = multiprocessing.Process(target=greeting_with_sleep, args=('Codecademy',))
p.start()
