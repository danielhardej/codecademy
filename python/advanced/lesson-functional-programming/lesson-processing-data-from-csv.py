import csv
from collections import namedtuple
from functools import reduce

tree = namedtuple("tree", ["index", "width", "height", "volume"])

with open('trees.csv', newline = '') as csvfile:
  reader = csv.reader(csvfile, delimiter=',', quotechar='|')
  next(reader)
  mapper = map(lambda x: tree(int(x[0]), float(x[1]), int(x[2]), float(x[3])), reader)

  # Create a tuple called trees and populate it with data of trees that have a height greater
  # than 75. First, create an iterator called t where you filter out trees that don’t meet the
  # height requirement. Then create the trees tuple.

  t = filter(lambda x: x[2] > 75, mapper)
  trees = tuple(t)

  # Create a variable called widest and store in it the record of the widest tree in trees.
  widest = reduce(lambda x, y: x if x.width > y.width else y, trees)
  print(widest)
