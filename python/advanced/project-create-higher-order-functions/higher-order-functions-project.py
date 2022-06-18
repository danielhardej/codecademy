# project to create your own higher-order functions and then use them to process data from a CSV file.
# project from the functional programming module in advanced Python 3 on codecademy
#
# The functions you will create are:
# count(): will return the frequency of an element in an iterable
# average(): will return the average of elements in an iterable of numbers
# avg_helper() :When next() in an iterable returns "null", avg_helper() should compute the average and return that value.
# median() : will return the value of the median element of elements in an iterable of numbers
# std_dev(): will return the standard deviation of elements in an iterable of numbers

import csv
from functools import reduce

def count(predicate, itr):
  count_filter = filter(predicate, itr)
  count_reduce = reduce(lambda x,y: x+1 , count_filter, 0)
  return count_reduce

def average(itr):
  # If itr is not iterable, this will generate an iterator.
  iterable = iter(itr)
  return avg_helper(0, iterable, 0)

def avg_helper(curr_count, itr, curr_sum):
  next_sum = next(itr, "null")
  if next_sum == "null":
    return curr_sum/curr_count
  curr_sum += next_sum
  curr_count += 1
  return avg_helper(curr_count, itr, curr_sum)

def median(itr):
  iterable = iter(itr)
  iterabel.sort()
  # NB we use the // operator to get the truncated value of the division
  if len(iterable) % 2 == 0:
    median = (iterable[n//2] + iterable[n//2 - 1]) / 2
  else:
    median = iterable[n//2]
  return median

def std_dev(itr):
  iterable = iter(itr)
  N = len(iterable)
  mean = average(itr)
  var = sum((x - mean)**2 for x in itr)
  return (var / N) ** 0.5

with open('1kSalesRec.csv', newline = '') as csvfile:
  reader = csv.reader(csvfile, delimiter=',', quotechar='|')
  fields = next(reader)
  count_belgiums = count(lambda x: x[1] == "Belgium", reader)
  print(count_belgiums)

  csvfile.seek(0)
  avg_portugal = average(map(lambda x: float(x[13]), filter(lambda x: x[1] == "Portugal", reader)))
  print(avg_portugal)
