import random

class BinarySearchTree:

  def __init__(self, value, depth=1):
    self.value = value
    self.depth = depth
    self.left = None
    self.right = None


  def insert(self, value):

    if value < self.value:
      if self.left is None:
        self.left = BinarySearchTree(value, self.depth + 1)
        print(f'Tree node {value} added to the left of {self.value} at depth {self.depth + 1}')
      else:
        self.left.insert(value)

    else:
      if self.right is None:
        self.right = BinarySearchTree(value, self.depth + 1)
        print(f'Tree node {value} added to the right of {self.value} at depth {self.depth + 1}')
      else:
        self.right.insert(value)


  def get_node_by_value(self, value):
    if value == self.value:
      return self
    elif (self.left is not None) and (value < self.value):
      return self.left.get_node_by_value(value)
    elif (self.right is not None) and (value >= self.value):
      return self.right.get_node_by_value(value)
    else:
      return None


  def depth_first_traversal(self):

    if self.left is not None:
      self.left.depth_first_traversal()
    print(f'Depth={self.depth}, Value={self.value}')

    if self.right is not None:
      self.right.depth_first_traversal()


# Test 1
root = BinarySearchTree(100)
root.insert(50)
root.insert(125)
root.insert(75)
root.insert(25)
print(root.get_node_by_value(75).value)
print(root.get_node_by_value(55))

# Test 2
tree = BinarySearchTree(48)
tree.insert(24)
tree.insert(55)
tree.insert(26)
tree.insert(38)
tree.insert(56)
tree.insert(74)
# Print depth-first traversal:
tree.depth_first_traversal()

# Finally...
print("Creating Binary Search Tree rooted at value 15:")
tree = BinarySearchTree(15)

for x in range(10):
  tree.insert(random.randint(0, 100))

print("Printing the inorder depth-first traversal:")
tree.depth_first_traversal()
