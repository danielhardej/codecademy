#### Fill in the correct argument to the recursive call of this function that sums all the individual digits of a given integer.

    def sum_digits(n):
      if n < 10:
        return n
      else:
        last_digit = n % 10
        # What argument is every digit except the last?
        return last_digit + sum_digits(?????)

      sum_digits(12)
      # 3
      sum_digits(194)
      # 14

- [x] n // 10
- [ ] n % 10
- [ ] n * 10
- [ ] n - 10

#### The function call will eventually reach the base case with the given argument and function definition.

    def power_set(my_list):
        if len(my_list) == 0:
            return [[]]
        power_set_without_first = power_set(my_list[1:])
        with_first = [ [my_list[0]] + rest for rest in power_set_without_first ]
        return with_first + power_set_without_first

    power_set(['a', 'b', 'c'])

- [x] True.
- [ ] False.

#### Which comment surrounds the base case of this function which produces a binary search tree from a sorted list given as input?

      def build_bst(my_list):
        # COMMENT 1
        if len(my_list) == 0:
          return None
        # END COMMENT 1

        # COMMENT 2
        mid_idx = len(my_list) // 2
        mid_val = my_list[mid_idx]
        # END COMMENT 2

          # COMMENT 3
        tree_node = {"data": mid_val}
        tree_node["left_child"] = build_bst(my_list[ : mid_idx])
        tree_node["right_child"] = build_bst(my_list[mid_idx + 1 : ])
        # END COMMENT 3

        # COMMENT 4
        return tree_node
        # END COMMENT 4


- [ ] Comment 3
- [ ] Comment 2
- [ ] Comment 4
- [x] Comment 1

#### Which comment surrounds the recursive step of this function which produces Fibonnaci numbers?

    # COMMENT 1
    def fibonacci(n):
    # END OF COMMENT 1

      # COMMENT 2
      if n <= 1:
        return 1
      # END OF COMMENT 2

      # COMMENT 3
      else:
        return fibonacci(n - 1) + fibonacci(n - 2)
        # END OF COMMENT 3

- [ ] Comment 2
- [ ] Comment 1
- [x] Comment 3

#### Fill in the argument to the recursive call in this function that produces the sum of all numbers from 1 to a given input integer.

def sum_to_one(n):
  if n < 0:
    SumToOneException("0 or Positive Numbers Only!")
  if n <= 1:
    return n
  return n + sum_to_one(????)

- [x] n - 1
- [ ] n - 2
- [ ] n + 1
- [ ] n * 1

#### The following recursive function will conclude with the given argument.

    def fibonacci(n):
      if n <= 1:
        return 1
      else:
        return fibonacci(n + 1) + fibonacci(n + 2)

    fibonacci(7)

- [ ] True.
- [x] False.

#### Fill in the missing piece of this function which computes the nth Fibonacci number. Fibonacci numbers are produced from the previous two numbers in the sequence. 1, 1, 2, 3, 5, 8

    def fibonacci(n):
      if n <= 1:
        return 1
      else:
        return fibonacci(n - 1) + fibonacci(?????)

- [ ] n + 2
- [x] n - 2
- [ ] n - 1
- [ ] n + 1

#### Which comment surrounds the base case of this recursive function which produces a power set from a given list of elements?

      def power_set(my_list):
          # COMMENT 1
          if len(my_list) == 0:
              return [[]]
          # END COMMENT 1

          # COMMENT 2
          power_set_without_first = power_set(my_list[1:])
          # END COMMENT 2

          # COMMENT 3
          with_first = [ [my_list[0]] + rest for rest in power_set_without_first ]
          # END COMMENT 3

          # COMMENT 4
          return with_first + power_set_without_first
          # END COMMENT 4

- [ ] Comment 4
- [x] Comment 1
- [ ] Comment 2
- [ ] Comment 3

#### Complete the missing portion of this recursive function which removes nested lists from the list given as an argument.

    def flatten(l):
       result = []
       for el in l:
         if isinstance(el, list):
           ????????
           result += flat
         else:
           result.append(el)
       return result

    flatten(el)


- [ ] flat = flatten(result)
- [x] flat = flatten(el)
- [ ] flat = [el]


#### Complete the missing piece of this recursive function which calculates the product of every number from 1 up to the integer given as an argument. this function should return 1 for an input of 0

    def factorial(n):
      if n < 0:
        raise FactorialException("Input must be 0 or greater")
      if ???????:
        return 1
      else:
        return n * factorial(n - 1)


- [x] n <= 1
- [ ] n == 1
- [ ] n != 0
- [ ] n % 2 == 0


#### What is the Big O runtime of this recursive function?

    def factorial(n):
      if n <= 1:
        return 1
      else:
        return n * factorial(n - 1)

- [ ] Quadratic - O(N^2)
- [x] Linear - O(N)
- [ ] Logarithmic - O(logN)
- [ ] Factorial - O(N!)

#### What is the Big O runtime of this recursive function?

    def fibonacci(n):
      if n <= 1:
        return 1
      else:
        return fibonacci(n - 1) + fibonacci(n - 2)

- [ ] Linear - O(N)
- [x] Exponential - O(2^N)
- [ ] Constant - O(1)
- [ ] Quadratic - O(N^2)
