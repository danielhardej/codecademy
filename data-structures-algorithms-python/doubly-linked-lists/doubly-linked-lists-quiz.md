#### Doubly linked lists have all of the following EXCEPT?

- [ ] A tail
- [x] A direction
- [ ] A head
- [ ] Nodes with two pointers

#### The .add_to_head() and .add_to_tail() methods in DoublyLinkedList are the same as those in the LinkedList.

- [ ] True
- [x] False



#### What would you add to complete the following .add_to_tail() method?

    def add_to_tail(self, new_value):
      new_tail = Node(new_value)
      current_tail = self.tail_node

      if current_tail != None:
        current_tail.set_next_node(new_tail)
        new_tail.set_prev_node(current_tail)

      self.tail_node = new_tail

      if self.head_node == None:
        self.head_node = new_tail



#### Given the following code, how would you complete the .remove_by_value() method?

    def remove_by_value(self, value_to_remove):
      node_to_remove = None
      current_node = self.head_node

      while current_node != None:
        if current_node.get_value() == value_to_remove:
          node_to_remove = current_node
          break

        current_node = current_node.get_next_node()

      if node_to_remove == None:
        return None

      if node_to_remove == self.head_node:
        self.remove_head()
      elif node_to_remove == self.tail_node:
        self.remove_tail()
      else:
        next_node = node_to_remove.get_next_node()
        prev_node = node_to_remove.get_prev_node()
        next_node.set_prev_node(prev_node)
        prev_node.set_next_node(next_node)

      return node_to_remove



#### What would you add to complete the following .remove_tail() method?

    def remove_tail(self):
      removed_tail = self.tail_node

      if removed_tail == None:
        return None

      self.tail_node = removed_tail.get_prev_node()

      if self.tail_node != None:
        self.tail_node.set_next_node(None)

      if removed_tail == self.head_node:
        self.remove_head()

      return removed_tail.get_value()



#### Given a fully functioning DoublyLinkedList class, what will the following code output?

    test_list = DoublyLinkedList()
    test_list.add_to_head(9)
    test_list.remove_tail()
    test_list.add_to_tail(8)
    test_list.add_to_tail(2)
    test_list.remove_head()
    test_list.add_to_tail(4)
    test_list.remove_by_value(9)
    test_list.remove_head()
    print(test_list.head_node.get_value())


- [x] 4
- [ ] This will throw an error because the list is empty.
- [ ] 9
- [ ] This will throw an error because there is only a tail left in the list.



#### Which of the following is NOT true about the Python implementation of a DoublyLinkedList?

- [ ] There is an added .remove_tail() method.
- [ ] There is an added .remove_by_value() method.
- [x] Nodes are no longer in one order since the list has a tail.
- [ ] DoublyLinkedList has a tail_node property.
- [ ] DoublyLinkedList uses a different Node class.



#### Consider the doubly linked list: a <-> b <-> c. When removing node a, the pointers of which node(s) should be updated?

- [ ] Nodes a and b
- [ ] All of the nodes
- [ ] Node c
- [x] Node b


#### What is the difference between the DoublyLinkedList and LinkedList constructors?

- [ ] There are no differences, the constructors are the same.
- [ ] The DoublyLinkedList constructor has an added prev_node pointer.
- [x] The DoublyLinkedList has an added tail_node property.
- [ ] The DoublyLinkedList constructor takes a parameter while the LinkedList constructor does not.


#### What would you add to complete the .remove_head() method?

    def remove_head(self):
      removed_head = self.head_node
      if removed_head == None:
         return None
      self.head_node = removed_head.get_next_node()
      if self.head_node != None:
        self.head_node.set_prev_node(None)
      if removed_head == self.tail_node:
        self.remove_tail()
      return removed_head.get_value()



#### What would you add to complete the following .add_to_head() method?

    def add_to_head(self, new_value):
      new_head = Node(new_value)
      current_head = self.head_node

      if current_head != None:
        current_head.set_prev_node(new_head)
        new_head.set_next_node(current_head)

      self.head_node = new_head

      if self.tail_node == None:
        self.tail_node = new_head
