#### Select the missing portion of code.

    from random import randrange

    def quicksort(list, start, end):
      if start >= end:
        return

      pivot_idx = randrange(start, end + 1)
      pivot_element = list[pivot_idx]

        # WHAT CODE GOES HERE?
      # ?????????????

      less_than_pointer = start

      for i in range(start, end):
        if list[i] < pivot_element:
          list[i], list[less_than_pointer] = list[less_than_pointer], list[i]
          less_than_pointer += 1

      list[end], list[less_than_pointer] = list[less_than_pointer], list[end]

      quicksort(list, start, less_than_pointer - 1)
      quicksort(list, less_than_pointer + 1, end)


- [ ] pivot_idx += start
- [ ] list[start], list[end] = list[end], list[start]
- [x] list[end], list[pivot_idx] = list[pivot_idx], list[end]
- [ ] start -= pivot_idx


#### Fill in the missing portion of code.

    def quicksort(list, start, end):
      if start >= end:
        return

      pivot_idx = randrange(start, end + 1)
      pivot_element = list[pivot_idx]

      list[end], list[pivot_idx] = list[pivot_idx], list[end]

      less_than_pointer = start

      for i in range(start, end):
        # WHAT OCCURS BELOW?
        if # ??????????:
          list[i], list[less_than_pointer] = list[less_than_pointer], list[i]
          less_than_pointer += 1

      list[end], list[less_than_pointer] = list[less_than_pointer], list[end]

      quicksort(list, start, less_than_pointer - 1)
      quicksort(list, less_than_pointer + 1, end)

- [x] list[i] < pivot_element
- [ ] list[i] > pivot_element
- [ ] list[i] == pivot_element
- [ ] list[i] is not pivot_element


#### Explain the purpose of the highlighted portion of code.

    def quicksort(list, start, end):
      if start >= end:
        return

      pivot_idx = randrange(start, end + 1)
      pivot_element = list[pivot_idx]

      list[end], list[pivot_idx] = list[pivot_idx], list[end]

      less_than_pointer = start

      for i in range(start, end):
        if list[i] < pivot_element:
          list[i], list[less_than_pointer] = list[less_than_pointer], list[i]
          less_than_pointer += 1

        #### EXPLAIN THE PURPOSE OF THE LINE BELOW #####
      list[end], list[less_than_pointer] = list[less_than_pointer], list[end]

      quicksort(list, start, less_than_pointer - 1)
      quicksort(list, less_than_pointer + 1, end)


- [x] This line moves the pivot_element into the correct placement within the list.
- [ ] This line checks whether we’ve reached the base case of the algorithm.
- [ ] This line selects a pivot_element from the list.
- [ ] This line recursively calls quicksort on the “lesser than” and “greater than” sub-lists.


#### Select the reasoning for the highlighted portion of code.

    def quicksort(list, start, end):
      if start >= end:
        return

      pivot_idx = randrange(start, end + 1)
      pivot_element = list[pivot_idx]

      list[end], list[pivot_idx] = list[pivot_idx], list[end]

      less_than_pointer = start

      for i in range(start, end):
        if list[i] < pivot_element:
          list[i], list[less_than_pointer] = list[less_than_pointer], list[i]
          less_than_pointer += 1

      list[end], list[less_than_pointer] = list[less_than_pointer], list[end]

      ##### EXPLAIN LINES BELOW ########
      quicksort(list, start, less_than_pointer - 1)
      quicksort(list, less_than_pointer + 1, end)


- [ ] These lines partition the list into sub-lists of “lesser than” or “greater than” values.
- [ ] These lines are the base case of the algorithm.
- [x] These lines recursively call quicksort on the “lesser than” and “greater than” sub-lists created from the partition.
- [ ] These lines select a pivot element from the “lesser than” and “greater than” sub-lists.


#### Explain the base case highlighted in the code snippet.

    def quicksort(list, start, end):
      ### BASE CASE ####
      if start >= end:
        return
      ##################
      pivot_idx = randrange(start, end + 1)
      pivot_element = list[pivot_idx]

      list[end], list[pivot_idx] = list[pivot_idx], list[end]

      less_than_pointer = start

      for i in range(start, end):
        if list[i] < pivot_element:
          list[i], list[less_than_pointer] = list[less_than_pointer], list[i]
          less_than_pointer += 1

      list[end], list[less_than_pointer] = list[less_than_pointer], list[end]

      quicksort(list, start, less_than_pointer - 1)
      quicksort(list, less_than_pointer + 1, end)


- [ ] Using pointers, we’re checking if the value at start is greater than end.
- [ ] Using pointers, we’re partitioning the list into sub-lists.
- [x] Using pointers, we’re checking if the portion of the list between start and end contains one or less elements.
- [ ] Compares the pivot_element with the end and start elements.


#### The following code represents an in-place implementation of the quicksort algorithm.

    def qs(arr):
      if len(arr) <= 1:
        return arr

      smaller = []
      larger = []

      pivot = 0
      pivot_element = arr[pivot]

      for i in range(1, len(arr)):
        if arr[i] > pivot_element:
          larger.append(arr[i])
        else:
          smaller.append(arr[i])

      sorted_smaller = qs(smaller)
      sorted_larger = qs(larger)

      return sorted_smaller + [pivot_element] + sorted_larger

- [ ] True.
- [x] False.


#### What does an “in-place” quicksort mean?

- [ ] Values are sorted in descending order as opposed to ascending order.
- [x] Values are swapped within the original list, and no additional memory is used.
- [ ] Values are swapped according to their values.
- [ ] Values are placed inside a dictionary from the list.
