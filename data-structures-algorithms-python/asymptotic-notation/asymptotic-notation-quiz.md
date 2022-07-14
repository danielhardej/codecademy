#### Which function has the most efficient Big O runtime?

    def func_one(list):
      for element in list:
        print(element)
        if element % 2 == 0:
          print("EVEN STEVEN!")

    def func_two(list):
      for element in list:
        for element2 in list:
          print(element, element2)

    def func_three(list):
      print(list)
      for i in range(0, 100000):
        print(i)

    def func_four(list):
      for element in list:
        print(element)

      for element2 in list:
        print(element * element)


func_two()
func_four()
- [x] func_three()
func_one()


#### Which function has the Big O runtime of O(N + M)?

    def first_func(list1):
      for element in list1:
        print(element)

    def second_func(list1, list2):
      for element in list1:
        print(element)
        for element2 in list2:
          print(element2)

    def third_func(list1, list2):
      for element in list1:
        print(element)

      for element2 in list2:
        print(element2)

    def fourth_func(list1):
      for element in list1:
        for element2 in list1:
          print(element + element2)


- [x] third_func()
first_func()
second_func()
fourth_func()



#### What is the runtime of the following code?

    def make_sum(num1, num2):
      return num1 + num2

Logarithmic: O(logN)
- [x] Constant: O(1)
Quadratic: O(N^2)
Linear: O(N)


#### Suppose we want to retrieve data stored under the string "secret", which of the data structures would give us the most efficient retrieval?

    # Option 1: Tuple
    option_1 = (("secret", "I like dogs"), ("public", "Cats are cool"))
    # Option 2: Dictionary
    option_2 = {"secret": "I like dogs", "public", "Cats are cool"}
    # Option 3: List
    option_3 = [["secret", "I like dogs"], ["public", "Cats are cool"]]
    # Option 4: Linked List
    option_4 = LinkedList("Secret: I like dogs")
    option_4.insert_beginning("Public: Cats are cool")

option_3
option_1
- [x] option_2
option_4


#### What is the Big O runtime of the following code?

def print_even_pairs(list):
  for element1 in list:
    for element2 in list:
      if (element1 + element2) % 2 == 0:
        print(element1, element2)


Logarithmic: O(logN)
- [x] Quadratic: O(N^2)
Linear: O(N)
Constant: O(1)

#### What is the Big O runtime of this code?

    def find_max(list):
      max = list[0]
      for value in list:
        if value > max:
          max = value
      return max


- [x] Linear: O(N)
Logarithmic: O(logN)
Quadratic: O(N^2)
Constant: O(1)


#### Which function has the least efficient Big O runtime?

      def func_one(list):
        for element in list:
          print(element)

        for element2 in list:
          print(element2)

        for element3 in list:
          print(element3)

      def func_two(list):
        for element in list:
          continue

      def func_three(list):
        return list[0] + list[1]

      def func_four(list):
        for element in list:
          print(list[0 : len(list)])


func_three()
- [x] func_four()
func_one()
func_two()

#### What is the Big O runtime of the following code? hint: Given a list of a certain length, how many iterations will be performed in the worst case?

    def mystery_function(list, target):
      start_idx = 0
      end_idx = len(list) - 1

      while start_idx <= end_idx:
        mid = (start_idx + end_idx) // 2
        mid_value = list[mid]

        if mid_value == target:
          return mid

        if mid_value > target:
          end_idx = mid - 1
        else:
          start_idx = mid + 1

      raise ValueError("{0} is not in list".format(target))


Linear: O(N)
Factorial: O(N!)
- [x] Logarithmic: O(logN)
Quadratic: O(N^2)
