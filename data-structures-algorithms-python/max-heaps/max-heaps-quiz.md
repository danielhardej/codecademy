#### In a max-heap, what happens during the process of “heapifying up”?

- [x] While there is a parent for an element and the parent contains a smaller value than the child, the element swaps locations with the parent.
- [ ] A new element is added to the end of the heap list.
- [ ] A new element is added to the front of the list.
- [ ] While there is a parent for an element and the parent contains a larger value than the child, the element swaps locations with the parent.

#### In a max-heap, what is true of the first element in the array, or “root” element?

- [x] It is the maximum value.
- [ ] The root value can never be changed.
- [ ] It is the minimum value.
- [ ] Every value below the root will be larger than the root value.

#### Select the missing line of code to complete the method.

    def add(self, element):
      self.count += 1
      # ????????
      self.heapify_up()

- [x] self.heap_list.append(element)
- [ ] self.heap_list += element
- [ ] self.heap_list += 1
- [ ] self.heap_list.pop()

#### Select the missing line of code to complete the method.

    def heapify_up(self):
      # ??????????
      while self.parent_idx(idx) > 0:
        parent = self.heap_list[self.parent_idx(idx)]
        child = self.heap_list[idx]
        if parent < child:
          self.heap_list[idx] = parent
          self.heap_list[self.parent_idx(idx)] = child
        idx = self.parent_idx(idx)

- [x] idx = self.count
- [ ] idx = self.parent_idx(0)
- [ ] idx = 0
- [ ] idx = self.left_child_idx(1)

#### What are the two main properties a max-heap must always keep?

- [x] The root, or first element, contains the largest value and every parent must have a larger value than their children.
- [ ] The root, or first element, contains the largest value and every parent must have a smaller value than their children.
- [ ] The root, or first element, contains the smallest value and every parent must have a larger value than their children.
- [ ] The root, or first element, contains the smallest value and every parent must have a smaller value than their children.

#### A max-heap is an effective solution for what kind of problem?

- [x] When you need to efficiently maintain a maximum value in a dataset.
- [ ] When you need to efficiently maintain a minimum value in a dataset.
- [ ] When you need to create a relationship of connections between data in your dataset.
- [ ] When you need to maintain an ordering of when elements entered the dataset.

#### What is the purpose of these methods?

    def parent_idx(self, idx):
      return idx // 2

    def left_child_idx(self, idx):
      return idx * 2

    def right_child_idx(self, idx):
      return idx * 2 + 1

- [ ] They swap values within the MaxHeap instance.
- [ ] They return the appropriate value of either a parent, left child, or right child element.
- [x] They return the appropriate index of either a parent, left child, or right child element.
- [ ] They are used to initialize MaxHeap.

#### True or False: Heaps are often visualized as binary trees and implemented using a sequential data structure like an array.

- [ ] False
- [x] True
