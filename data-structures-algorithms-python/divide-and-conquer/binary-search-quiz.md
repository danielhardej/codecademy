#### Which of the following is not a possible printed in-order traversal of a Binary Search Tree? The method is given in the code block, for reference.

    def depth_first_traversal(self):
      if (self.left is not None):
        self.left.depth_first_traversal()
      print(f'Depth={self.depth}, Value={self.value}')
      if (self.right is not None):
        self.right.depth_first_traversal()

- [ ] 2, 6, 18, 31, 65, 89, 94
- [x] 24, 11, 17, 37, 29
- [ ] 15
- [ ] 1, 1, 1, 4, 5, 8, 8, 8, 15, 16, 22

#### What will be the result of .get_node_by_value(34) on this Binary Search Tree?

        56
       /  \
      28  72
     /  \   \
    22  34   89

##### The .get_node_by_value() method code is provided in the code block, for reference.

    def get_node_by_value(self, value):
      if (self.value == value):
        return self
      elif ((self.left is not None) and (value < self.value)):
        return self.left.get_node_by_value(value)
      elif (self.right is not None):
        return self.right.get_node_by_value(value)
      else:
        return None

- [ ] None
- [x] The BinarySearchTree instance containing the value 34.
- [ ] True


#### Which of these is not an instance variable in our Binary Search Tree class?

- [ ] left
- [ ] depth
- [ ] right
- [ ] value
- [x] size


#### Fill in the code below to correctly implement the .insert() method.

    def insert(self, value):
      if (value < self.value):
        if (self.left is None):
          self.left = BinarySearchTree(value, self.depth + 1)
        else:
          self.left.insert(value)
      else:
        if (self.right is None):
          self.right = BinarySearchTree(value, self.depth + 1)
        else:
          self.right.insert(value)


#### What is the time complexity for .insert() and .get_node_by_value() performed on an average, relatively balanced, Binary Search Tree with N nodes?

- [ ] O(1)
- [x] O(logN)
- [ ] O(N)

#### What will be the result of .get_node_by_value(40) on this Binary Search Tree?

        56
       /  \
      28  72
     /  \   \
    22  34   89

##### The .get_node_by_value() method code is provided in the code block, for reference.

    def get_node_by_value(self, value):
      if (self.value == value):
        return self
      elif ((self.left is not None) and (value < self.value)):
        return self.left.get_node_by_value(value)
      elif (self.right is not None):
        return self.right.get_node_by_value(value)
      else:
        return None


- [ ] The BinarySearchTree instance containing the value 40
- [ ] False
- [x] None

#### Fill in .get_node_by_value() so that it searches the BinarySearchTree and correctly returns either a BinarySearchTree instance with matching data or None.

    def get_node_by_value(self, value):
      if (self.value == value):
        return self
      elif ((self.left is not None) and (value < self.value)):
        return self.left.get_node_by_value(value)
      elif (self.right is not None):
        return self.right.get_node_by_value(value)
      else:
        return None


#### Based on the constructor we implemented, which is a correct way of instantiating a Binary Search Tree node?

    def __init__(self, value, depth=1):
      self.value = value
      self.depth = depth
      self.left = None
      self.right = None


- [ ] root = BinarySearchTree(25) \n
      root.left = BinarySearchTree(14)\n
      root.right = BinarySearchTree(45)

- [ ] root = BinarySearchTree("groot")\n
      root.left = BinarySearchTree("word1", 2)\n
      root.right = BinarySearchTree("word2", 2)

- [x] root = BinarySearchTree(25)
      root.left = BinarySearchTree(14, 2)
      root.right = BinarySearchTree(45, 2)

- [ ] root = BinarySearchTree(25)
      root.left = BinarySearchTree(14, root.depth)
      root.right = BinarySearchTree(45, root.depth)

#### True or False: The following code will correctly insert a value into a tree.

    def insert(self, value):
      if (value < self.value):
        if (self.left is None):
          self.left.insert(value)
        else:
          self.left = BinarySearchTree(value, self.depth + 1)
      else:
        if (self.right is None):
          self.right.insert(value)
        else:
          self.right = BinarySearchTree(value, self.depth + 1)


- [x] False
- [ ] True

#### Fill in the .depth_first_traversal() method such that it prints an in-order traversal of a Binary Search Tree.


    def depth_first_traversal(self):
      if (self.left is not None):
        self.left.depth_first_traversal()
      print(f'Depth={self.depth}, Value={self.value}')
      if (self.right is not None):
        self.right.depth_first_traversal()
