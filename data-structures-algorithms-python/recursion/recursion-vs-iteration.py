def factorial(n):
  current_val = n
  factorial_val = 1
  for num in range(n):
    factorial_val = factorial_val * current_val
    current_val -= 1
  return factorial_val


# test cases
print(factorial(3) == 6)
print(factorial(0) == 1)
print(factorial(5) == 120)


def fibonacci(n):
  if n < 0:
    break
  if n == 0:
    return 0
  if n == 1:
    return 1
  fibonacci_list = [0, 1]
  while n > len(fibonacci_list) - 1:
    fibonacci_list.append(fibonacci_list[-1] + fibonacci_list[-2])
    #print("Element {}: {}".format(i, fibonacci_list[i]))
  print(fibonacci_list)
  return fibonacci_list[-1]


# test cases
print(fibonacci(3) == 2)
print(fibonacci(7) == 13)
print(fibonacci(0) == 0)



def sum_digits(n):
  if n <= 9:
    return n
  last_digit = n % 10
  return sum_digits(n // 10) + last_digit

# test cases
print(sum_digits(12) == 3)
print(sum_digits(552) == 12)
print(sum_digits(123456789) == 45)





# using iteration:
def iter_find_min(my_list):
  current_min = None
  for element in my_list:
    if current_min is None:
      current_min = element
    if element is not None:
      if element < current_min:
        current_min = element
  return current_min

#using recursion
def find_min(my_list, min_val=None):
  if len(my_list) == 0:
    return min_val
  if not min_val or my_list[0] < min_val:
    min_val = my_list[0]
  return find_min(my_list[1:], min_val)


# test cases
print(find_min([42, 17, 2, -1, 67]) == -1)
print(find_min([]) == None)
print(find_min([13, 72, 19, 5, 86]) == 5)




def is_palindrome(my_string):
  if len(my_string) < 2:
    return True
  if my_string[0] != my_string[-1]:
    return False
  return is_palindrome(my_string[1:-1])


# test cases
print(is_palindrome("abba") == True)
print(is_palindrome("abcba") == True)
print(is_palindrome("") == True)
print(is_palindrome("abcd") == False)





def multiplication(num_1, num_2):
  result = 0
  if (num_1 == 0) or (num_2 == 0):
    return 0
  else:
    return num_1 + multiplication(num_1, (num_2-1))


# test cases
print(multiplication(3, 7) == 21)
print(multiplication(5, 5) == 25)
print(multiplication(0, 4) == 0)




def depth(tree_node):
  if tree_node is None:
    return 0
  left_depth = depth(tree_node["left_child"])
  right_depth = depth(tree_node["right_child"])
  if left_depth > right_depth:
    return left_depth + 1
  else:
    return right_depth + 1

# HELPER FUNCTION TO BUILD TREES
def build_bst(my_list):
  if len(my_list) == 0:
    return None

  mid_idx = len(my_list) // 2
  mid_val = my_list[mid_idx]

  tree_node = {"data": mid_val}
  tree_node["left_child"] = build_bst(my_list[ : mid_idx])
  tree_node["right_child"] = build_bst(my_list[mid_idx + 1 : ])

  return tree_node

# HELPER VARIABLES
tree_level_1 = build_bst([1])
tree_level_2 = build_bst([1, 2, 3])
tree_level_4 = build_bst([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])

# test cases
print(depth(tree_level_1) == 1)
print(depth(tree_level_2) == 2)
print(depth(tree_level_4) == 4)
