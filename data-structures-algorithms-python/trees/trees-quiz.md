#### Complete the .traverse() method.

    class TreeNode:
      def __init__(self, value):
        self.value = value
        self.children = []

      def traverse(self):
        nodes_to_visit = [self]
        while len(nodes_to_visit) > 0:
          current_node = nodes_to_visit.pop()
          nodes_to_visit += current_node.children


####Tree nodes which have no references to other nodes (children) are known as what?

- [ ] Fringe nodes
- [ ] Depth nodes
- [ ] Branch nodes
- [x] Leaf nodes


#### What would make a wide tree?

- [ ] Many parent nodes per child node.
- [ ] Many different types of data in different nodes.
- [x] Many child nodes per parent node.



####Given the following code, in what order will we visit the nodes?

    class TreeNode:
      def __init__(self, value):
        self.value = value
        self.children = []

      def add_child(self, child_node):
        self.children.append(child_node)

      def traverse(self):
        nodes_to_visit = [self]
        while len(nodes_to_visit) > 0:
          current_node = nodes_to_visit.pop()
          nodes_to_visit += current_node.children

    root = TreeNode("A")
    first_child = TreeNode("B")
    second_child = TreeNode("C")

    root.add_child(first_child)
    root.add_child(second_child)

    root.traverse()

- [ ] "A" => "B" => "C"
- [x] "A" => "C" => "B"
- [ ] "C" => "B" => "A"
- [ ] "B" => "C" => "A"


#### A tree node that holds references to other tree nodes is called what?

- [ ] A root node
- [x] A parent node
- [ ] An owner node
- [ ] An executive node


#### Complete the .add_child() method.

    class TreeNode:
      def __init__(self, value):
        self.value = value
        self.children = []

      def add_child(self, child_node):
        self.children.append(child_node)


#### Tree nodes that share a parent node are called what?

- [x] Siblings
- [ ] Partners
- [ ] Buddies
- [ ] Co-workers


#### Which line of code would prevent adding a child node which already exists in self.children?

    class TreeNode:
      def __init__(self, value):
        self.value = value
        self.children = []

      def add_child(self, child_node):
        if child_node in self.children:  
            return
        self.children.append(child_node)


#### Fill in the blanks.

    In a binary search tree, values in the left child are lesser than their parent, and values in the right child are greater than their parent.


#### A tree node without a parent is called what?

- [ ] Stick
- [ ] Free
- [ ] Branch
- [x] Root

#### A tree node that is held as a reference by another tree node is called what?

- [x] A child node
- [ ] A sibling node
- [ ] An alpha node
- [ ] An uncle/aunt node
