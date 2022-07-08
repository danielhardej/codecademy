

#### How is a linked list terminated (in Python)?

- [x] By a node with a pointer to None.
- [ ] By a node with data to None.
- [ ] By a node with a pointer to the head.
- [ ] By a node with a pointer to -1.

#### Linked lists are made up of what elements?

- [ ] Data
- [x] Nodes
- [ ] List Items
- [ ] Pointers

#### It is possible to traverse a linked list through its list property, which keeps track of each node in the list.

- [x] False
- [ ] True

#### Fix the Node class so that some_node = Node(6) can run without error.

  class Node:
    def __init__(self, value, next_node):
      self.value = value
      self.next_node = next_node

  some_node = Node(6)

- [x] Line 2 should be def __init__(self, value, next_node=None):.

#### Which of the following nodes is the head node of ll?

  class Node:
    def __init__(self, value, next_node=None):
      self.value = value
      self.next_node = next_node

  class LinkedList:
    def __init__(self, head_node=None):
      self.head_node = head_node

  a = Node(5)
  b = Node(70, a)
  c = Node(5675, b)
  d = Node(90, c)
  ll = LinkedList(d)

- [x] d
- [ ] b
- [ ] a
- [ ] c


#### What would you add to the .remove_node() method to properly maintain the linked list when removing a node?

    class Node:
      def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    class LinkedList:
      def __init__(self, head_node=None):
        self.head_node = head_node

      def remove_node(self, node_to_remove):
        current_node = self.head_node
        if current_node == node_to_remove:
          self.head_node = current_node.next_node
        else:
          while current_node:
            next_node = current_node.next_node
            if next_node == node_to_remove:
              # --------> what line of code goes here?
              current_node = None
            else:
              current_node = next_node

- [x] current_node.next_node = next_node.next_node
- [ ] next_node.next_node = current_node.next_node
- [ ] node_to_remove = next_node.next_node
- [ ] current_node = next_node.next_node


#### What output would you expect to see in the terminal if you ran this code?

    class LinkedList:
      def __init__(self, head_node=None):
        self.head_node = head_node

      def stringify_list(self):
        string_list = ""
        current_node = self.head_node
        while current_node:
          string_list += str(current_node.value) + "."
          current_node = current_node.next_node
        return string_list

    a = Node(5)
    b = Node(70, a)
    c = Node(5675, b)
    d = Node(90, c)
    ll = LinkedList(d)

    print(ll.stringify_list())

- [ ] Nothing - you would get stuck in an infinite while loop.
- [ ] PrintError
- [x] 90.5675.70.5.
- [ ] d.c.b.a
- [ ] 5.70.5675.90.

#### Given this code, what would you add to complete the .add_new_head() method?

    class Node:
      def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    class LinkedList:
      def __init__(self, head_node=None):
        self.head_node = head_node

      def add_new_head(self, new_head_node):
        # --------> what line of code goes here?
        self.head_node = new_head_node

- [x] new_head_node.next_node = self.head_node
- [ ] new_head_node.next_node = self.next_node
- [ ] new_head_node.next_node = self.head_node.value
- [ ] self.head_node = new_head_node.next_node

#### Consider the linked list: a -> b -> c. When removing b from the list, which node(s) need(s) to be updated?

- [ ] a, b, and c
- [ ] b and c
- [x] a
- [ ] b

#### Linked list nodes do not contain which of the following?

- [ ] Data
- [ ] Pointers
- [ ] Links
- [x] Roots


#### What is the head node in a linked list?

- [x] The first node in the list.
- [ ] The middle node in the list.
- [ ] The node with the smallest value.
- [ ] The last node in the list.
