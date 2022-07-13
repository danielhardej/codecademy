
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


# define the fibonacci() function below...
def fibonacci(n):
  if n == 1:
    return 1
  if n == 0:
    return 0
  print("Recursive call with {0} as input".format(n))
  return fibonacci(n-1) + fibonacci(n-2)

fibonacci(5)
# set the appropriate runtime:
# 1, logN, N, N^2, 2^N, N!
fibonacci_runtime = "2^N"
