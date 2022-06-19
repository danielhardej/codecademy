## Given the tuple of numbers nums, complete the code that first finds all numbers that are greater than 10, squares them, and then finds the minimum of those numbers.
nums = (2, 12, 14, 1, 8, 10, 3, 7, 5, 15)
mn = reduce(lambda x, y: x if x < y else y, map(lambda k: k**2, filter(lambda q: q > 10, nums)))


## How would you write the following code as a lambda function?
def fcn(x, y):
  z = x**2 + y**2
  return z
## Answer:
fcn = lambda x,y: x**2 + y**2


## Complete the function that squares all even numbers in a tuple called nums.
map(lambda k: k**2, filter(lambda x: x % 2 == 0, nums))
