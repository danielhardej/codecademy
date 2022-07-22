#### What is the difference between .heapify_down() and .heapify_up()?

- [ ] The .heapify_down() method only works with max-heaps while .heapify_up() method only works with min-heaps.
- [x] The .heapify_down() method starts at the root of the heap while the .heapify_up() method starts at the end of the heap.
- [ ] The .heapify_down() method only works with min-heaps while .heapify_up() method only works with max-heaps.
- [ ] The .heapify_down() method starts at the end of the heap while the .heapify_up() method starts at the root of the heap.

#### Fill in the blanks to complete the .heapify_down() method.

    def heapify_down(self):
      idx = 1
      while self.child_present(idx):
        print("Heapifying down!")
        larger_child_idx = self.get_larger_child_idx(idx)
        child = self.heap_list[larger_child_idx]
        parent = self.heap_list[idx]
        if parent < child:
          self.heap_list[idx] = child
          self.heap_list[larger_child_idx] = parent
        idx = larger_child_idx
      print("HEAP RESTORED! {0}".format(self.heap_list))

#### Imagine we had the following heap and wanted to remove the largest value:

    [None, 40, 19, 18, 2, 13, 12]

##### After swapping 40 and 12 and then removing 40, our list looks like this:

    [None, 12, 19, 18, 2, 13]

##### Having 12 as the root value breaks the heap property that a child must be smaller than its parent. What value will be swapped with 12 to restore the heap?


- [x] 19
- [ ] 18
- [ ] 2
- [ ] 13

#### Fill in the blanks to complete the following heapsort() function.

    def heapsort(lst):
      sort = []
      max_heap = MaxHeap()
      for idx in lst:
        max_heap.add(idx)
      while max_heap.count > 0:
        max_value = max_heap.retrieve_max()
        sort.insert(0, max_value)
      return sort

#### Fill in the code to complete the .retrieve_max() method.

    def retrieve_max(self):
      if self.count == 0:
        print("No items in heap")
        return None
      max_value = self.heap_list[1]
      print("Removing: {0} from {1}".format(max_value, self.heap_list))
      self.heap_list[1] = self.heap_list[self.count]
      self.count -= 1
      self.heap_list.pop()
      print("Last element moved to first: {0}".format(self.heap_list))    
      self.heapify_down()
      return max_value

#### What would a heapsort algorithm return if the following list was sent as an input value?

    [12, 18, 8, 4, 2]

- [ ] [12, 18, 8, 4, 2]
- [x] [2, 4, 8, 12, 18]
- [ ] [18, 12, 8, 4, 2]
- [ ] [18, 12, 8, 2, 4]

#### Fill in the blanks to complete the .get_larger_child_idx() method.

    def get_larger_child_idx(self, idx):
      if self.right_child_idx(idx) > self.count:
        print("There is only a left child")
        return self.left_child_idx(idx)
      else:
        left_child = self.heap_list[self.left_child_idx(idx)]
        right_child = self.heap_list[self.right_child_idx(idx)]
        if left_child > right_child:
          print("Left child "+ str(left_child) + " is larger than right child " + str(right_child))
          return self.left_child_idx(idx)
        else:
          print("Right child " + str(right_child) + " is larger than left child " + str(left_child))
          return self.right_child_idx(idx)

#### True or False: The last step in implementing a heapsort algorithm is to place a list of values inside a heap.

- [ ] True
- [x] False

#### When trying to extract the largest value from the heap, what value should be swapped with the first element in the list?

- [ ] No values get swapped.
- [ ] The second-to-last element in the list.
- [ ] The element with the second largest value in the list.
- [x] The last element in the list.
