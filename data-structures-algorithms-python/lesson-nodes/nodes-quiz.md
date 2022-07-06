#### Consider the following nodes and links: a -> n -> t. If you want to remove node n, but preserve node t, what are the steps you would take?

- [x] Change the link on a to point to t using a.set_link_node(t).
- [ ] Delete the link on a that points to n using a.set_link_node(None).
- [ ] Remove the link on n using n.set_link_node(None).
- [ ] Change the link on a to point to t using t.set_link_node(a).

#### Consider the following nodes and links: a -> n -> t. If you want to remove node n, but preserve node t, what should the resulting structure look like?

- [ ] a -> n
- [x] a -> t
- [ ] t -> a
- [ ] a n->t

#### Which two features do most nodes contain?

- [x] Data and links to other nodes.
- [ ] Data and null pointers.
- [ ] Arrays and pointers to other nodes.
- [ ] Data and an array containing other nodes.

#### A node containing only null pointers indicates what?

- [ ] There are no other nodes in the data structure.
- [ ] The node has no data.
- [x] You are at the end of the node path you were following.
- [ ] No other nodes link to this node.

#### Which of the following methods implemented in the Node class are required to establish a Node class with an accessible but immutable value?

  class Node:
    def __init__(self, value, link_node=None):
         self.value = value
         self.link_node = link_node
    def get_value(self):
     return self.value
    def get_link_node(self):
     return self.link_node
    def set_link_node(self, link_node):
     self.link_node = link_node
    def set_value(self, value):
     self.value = value
    def increment_value(self):
      self.value = self.value + 1

- [ ] .__init__(), .get_value(), .get_link_node(), .set_value() and .set_link_node()
- [ ] .__init__(), .get_link_node(), and .set_link_node()
- [ ] .__init__(), .get_value(), .get_link_node(), .set_link_node(), and .increment_value()
- [x] .__init__(), .get_value(), .get_link_node(), and .set_link_node()
