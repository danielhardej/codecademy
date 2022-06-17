from functools import reduce

costs = {"shirt": (4, 13.00), "shoes":(2, 80.00), "pants":(3, 100.00), "socks":(5, 5.00), "ties":(3, 14.00), "watch":(1, 145.00)}

nums = (24, 6, 7, 16, 8, 2, 3, 11, 21, 20, 22, 23, 19, 12, 1, 4, 17, 9, 25, 15)

# Given the record of item sales costs, find the total cost of items that cost more
# than £150. Assign the answer to variable total. Make sure to print out your solution.
# using all three higher-order functions

total = reduce(lambda x, y: x + y, filter(lambda r: r > 150.00, map(lambda q: costs[q][0] * costs[q][1], costs)))
print(total)

product = -1

# Given the tuple nums, use map(), filter(), and reduce() to find all numbers
# less than 10, add five to them, and find their total product.
# Assign the answer to variable product.

product = reduce(lambda x, y: x * y, map(lambda q: q + 5, filter(lambda r: r < 10 , nums)))
print(product)
