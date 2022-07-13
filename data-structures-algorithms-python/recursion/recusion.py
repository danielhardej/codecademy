
def sum_to_one(n):
  if n==1:
    return n
  print("Recursing with input: {0}".format(n))
  return n + sum_to_one(n-1)

print(sum_to_one(7))


def factorial(n):
  if n <= 1:
    return n

  else:
    return n * factorial(n-1)

print(factorial(12))


def flatten(my_list):
  result = []
  for item in my_list:
    if isinstance(item, list):
      print("List found!")
      flat_list = flatten(item)
      result += flat_list
    else:
      result.append(item)
  return result

planets = ['mercury', 'venus', ['earth'], 'mars', [['jupiter', 'saturn']], 'uranus', ['neptune', 'pluto']]
print(flatten(planets))
