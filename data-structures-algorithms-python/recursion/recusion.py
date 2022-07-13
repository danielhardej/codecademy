
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



# Define build_bst() below...
def build_bst(my_list):
  if len(my_list) == 0:
    return "No Child"
  middle_idx = len(my_list) // 2
  print("Middle index: {}".format(middle_idx))
  middle_value = my_list[middle_idx]
  print("Middle value: {}".format(middle_value))
  tree_node = {"data" : middle_value}
  tree_node["left_child"] = build_bst(my_list[0:middle_idx])
  tree_node["right_child"] = build_bst(my_list[middle_idx+1:])
  return tree_node

# For testing
sorted_list = [12, 13, 14, 15, 16]
binary_search_tree = build_bst(sorted_list)
print(binary_search_tree)

# fill in the runtime as a string
# 1, logN, N, N*logN, N^2, 2^N, N!
runtime = "N*logN"
