
class TreeNode:
  def __init__(self, value):
    self.value = value
    self.children = []


  def add_child(self, child_node):
    # creates parent-child relationship
    print("Adding " + child_node.value)
    self.children.append(child_node)


  def remove_child(self, child_node):
    # removes parent-child relationship
    print("Removing " + child_node.value + " from " + self.value)
    #new_children = []
    #for child in self.children:
    #  if child != child_node:
    #    new_children.append(child)
    #self.children = new_children
    self.children = [child for child in self.children if child is not child_node]   # using list comprehension to replace code above


  def traverse(self):
    # moves through each node referenced from self downwards
    print("Traversing...")
    nodes_to_visit = [self]
    while len(nodes_to_visit) > 0:
      current_node = nodes_to_visit.pop()
      print(current_node.value)
      nodes_to_visit += current_node.children


root = TreeNode("CEO")
first_child = TreeNode("Vice-President")
second_child = TreeNode("Head of Marketing")
third_child = TreeNode("Marketing Assistant")

root.add_child(first_child)
root.add_child(second_child)
second_child.add_child(third_child)

root.traverse()
