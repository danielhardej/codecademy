# We have seen how to create a process in Python; however, we didn’t see any speed or efficiency benefits in our previous example.
# To see the benefits of processes, let’s learn how to create multiple processes and test them out in our example.
# We will create multiple processes using one of the following approaches

import time
import multiprocessing

def greeting_with_sleep(string):
  print(string)
  time.sleep(2)
  print(string + " says hello!")


def main_multiprocessing():
  s = time.perf_counter()
  processes = []
  greetings = ['Codecademy', 'Chelsea', 'Hisham', 'Ashley']
  # add your code here
  for i in range(len(greetings)):
    p = multiprocessing.Process(target=greeting_with_sleep, args=(greetings[i],))
    processes.append(p)
    p.start()
  for process in processes:
    process.join()
  elapsed = time.perf_counter() - s
  print("Multiprocessing Elapsed Time: " + str(elapsed) + " seconds")

main_multiprocessing()
