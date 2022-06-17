import csv
from collections import namedtuple
from functools import reduce

# Code for Checkpoint 1 goes here.
tree = namedtuple("tree", ["index", "width", "height", "volume"])

with open('trees.csv', newline = '') as csvfile:
  reader = csv.reader(csvfile, delimiter=',', quotechar='|')
  next(reader) # Skip the first line in trees.csv that contains the data lablels.
  # Code for Checkpoint 2 goes here.
  mapper = map(lambda x: tree(int(x[0]), float(x[1]), int(x[2]), float(x[3])), reader)

  trees = tuple(mapper)
  print(trees)
