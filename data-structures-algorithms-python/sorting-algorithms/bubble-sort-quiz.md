#### The optimized version of bubble sort will have a more efficient big O runtime than the unoptimized version of bubble sort.

    def swap(arr, index_1, index_2):
      temp = arr[index_1]
      arr[index_1] = arr[index_2]
      arr[index_2] = temp

    def bubble_sort_unoptimized(arr):
      for el in arr:
        for index in range(len(arr) - 1):
          if arr[index] > arr[index + 1]:
            swap(arr, index, index + 1)


    def bubble_sort_optimized(arr):
      for i in range(len(arr)):
        for idx in range(len(arr) - i - 1):
          if arr[idx] > arr[idx + 1]:
            arr[idx], arr[idx + 1] = arr[idx + 1], arr[idx]

- [x] False.
- [ ] True.

#### Given the following implementation and function call, what would be the input list after 1 iteration of the outer loop?

    def bubble_sort(arr):
      for i in range(len(arr)):
        for idx in range(len(arr) - i - 1):
          if arr[idx] > arr[idx + 1]:
            arr[idx], arr[idx + 1] = arr[idx + 1], arr[idx]

    my_nums = [7, 3, 4, 2]

    bubble_sort(my_nums)

- [ ] [2, 3, 4, 7]
- [ ] [7, 3, 4, 2]
- [ ] [2, 3, 7, 4]
- [x] [3, 4, 2, 7]

#### Fill in the missing portion of the following implementation of bubble sort.

    def swap(arr, index_1, index_2):
      temp = arr[index_1]
      arr[index_1] = arr[index_2]
      arr[index_2] = temp

    def bubble_sort_unoptimized(arr):
      for el in arr:
        for index in range(len(arr) - 1):
          if arr[index] > arr[index + 1]:
            ????????????

- [ ] swap(arr, index, index - 1)
- [x] swap(arr, index, index + 1)
- [ ] swap(arr, index - 1, index + 1)

#### Which line in the following implementation performs a micro-optimization to reduce the number of overall iterations necessary to sort the input list?

    def bubble_sort(arr):
      for i in range(len(arr)):
        for idx in range(len(arr) - i - 1):
          if arr[idx] > arr[idx + 1]:
            arr[idx], arr[idx + 1] = arr[idx + 1], arr[idx]


- [ ] for i in range(len(arr)):
- [ ] if arr[idx] > arr[idx + 1]:
- [ ] arr[idx], arr[idx + 1] = arr[idx + 1], arr[idx]
- [x] for idx in range(len(arr) - i - 1):

#### Fill in the missing portion of the following implementation of bubble_sort().

def bubble_sort(arr):
  for i in range(len(arr)):
    for idx in range(len(arr) - i - 1):
      if ?????????:
        arr[idx], arr[idx + 1] = arr[idx + 1], arr[idx]

- [ ] arr[idx + 1] > arr[idx]
- [x] arr[idx] > arr[idx + 1]
- [ ] arr[idx + 1] > arr[idx - 1]
- [ ] arr[idx] < arr[idx + 1]


#### What is the bug in the following implementation of the swap() sub-routine function?

    def swap(arr, index_1, index_2):
      arr[index_1] = arr[index_2]
      arr[index_2] = arr[index_1]

- [ ] The value originally located at arr[index_2] is overwritten before it can be moved to arr[index_1].
- [ ] This function will not mutate the input list.
- [x] The value originally located at arr[index_1] is overwritten before it can be moved to arr[index_2].

#### The following implementation will perform the fewest number of iterations to sort a list.

    def bubble_sort(arr):
      for el in arr:
        for index in range(len(arr) - 1):
          if arr[index] > arr[index + 1]:
            swap(arr, index, index + 1)

- [ ] True.
- [x] False.
