#### Given the following definition of merge_sort(), what would the arguments to the first call of merge() be for merge_sort([80, 55, 59, 70])?

      def merge_sort(items):
        if len(items) <= 1:
          return items

        middle_index = len(items) // 2
        left_split = items[:middle_index]
        right_split = items[middle_index:]

        left_sorted = merge_sort(left_split)
        right_sorted = merge_sort(right_split)

        return merge(left_sorted, right_sorted)

      def merge(left, right):
        result = []

        while (left and right):
          if left[0] < right[0]:
            result.append(left[0])
            left.pop(0)
          else:
            result.append(right[0])
            right.pop(0)

        if left:
          result += left
        if right:
          result += right

        return result


- [x] left = [80], right = [55]
- [ ] left = [55], right = [80]
- [ ] left = [80, 55], right = [59, 70]
- [ ] left = [55, 80], right = [59, 70]

#### What are the two functions involved in performing a merge sort?

- [ ] merge_sort() and sort()
- [x] merge_sort() and merge()


#### Given the following definition of merge_sort(). If we called merge_sort([12, 13, 14, 15]), what would be the first value assigned to right_sorted?

    def merge_sort(items):
      if len(items) <= 1:
        return items

      middle_index = len(items) // 2
      left_split = items[:middle_index]
      right_split = items[middle_index:]

      left_sorted = merge_sort(left_split)
      right_sorted = merge_sort(right_split)

      return merge(left_sorted, right_sorted)

    def merge(left, right):
      result = []

      while (left and right):
        if left[0] < right[0]:
          result.append(left[0])
          left.pop(0)
        else:
          result.append(right[0])
          right.pop(0)

      if left:
        result += left
      if right:
        result += right

      return result

- [ ] [12]
- [x] [13]
- [ ] [15]
- [ ] [14]


#### What does merge_sort() do when called with the argument [15, 3, 9]?

- [ ] It sorts that list and then the merge_sort() that called it will merge it with another list.
- [ ] It merges to produce a copy of the input into the list, [15, 3, 9, 15, 3, 9] and then removes the duplicates until the list is sorted.
- [x] Calls merge_sort() on [15] and also on [3, 9] and then calls merge() on the return values.


#### Fill in the missing piece of code in merge_sort().

    def merge_sort(items):
      if len(items) <= 1:
        return items

      middle_index = ???????
      left_split = items[:middle_index]
      right_split = items[middle_index:]

      left_sorted = merge_sort(left_split)
      right_sorted = merge_sort(right_split)

      return merge(left_sorted, right_sorted)

    def merge(left, right):
      result = []

      while (left and right):
        if left[0] < right[0]:
          result.append(left[0])
          left.pop(0)
        else:
          result.append(right[0])
          right.pop(0)

      if left:
        result += left
      if right:
        result += right

      return result

- [x] len(items) // 2
- [ ] items[0]
- [ ] items[len(items) // 2]
- [ ] len(items) - 1


#### Fill in the missing portion of the merge_sort() function.

    def merge_sort(items):
        if ?????????:
            return items

        middle_index = len(items) // 2
        left_split = items[:middle_index]
        right_split = items[middle_index:]

        left_sorted = merge_sort(left_split)
        right_sorted = merge_sort(right_split)

        return merge(left_sorted, right_sorted)

    def merge(left, right):
        result = []

        while (left and right):
            if left[0] < right[0]:
                result.append(left[0])
                left.pop(0)
            else:
                result.append(right[0])
                right.pop(0)

        if left:
            result += left
        if right:
            result += right

        return result

- [x] len(items) <= 1
- [ ] len(items) == 0
- [ ] len(items) >= 2
- [ ] len(items) == 1


#### Complete the missing portion of the merge() sub-routine.

def merge_sort(items):
    if len(items) <= 1:
        return items

    middle_index = len(items) // 2
    left_split = items[:middle_index]
    right_split = items[middle_index:]

    left_sorted = merge_sort(left_split)
    right_sorted = merge_sort(right_split)

    return merge(left_sorted, right_sorted)

def merge(left, right):
    result = []

    while (?????????):
        if left[0] < right[0]:
            result.append(left[0])
            left.pop(0)
        else:
            result.append(right[0])
            right.pop(0)

    if left:
        result += left
    if right:
        result += right

    return result


- [x] left and right
- [ ] len(left) > len(right)
- [ ] len(result) > len(left) or len(result) > len(right)
- [ ] len(left) < len(right)
