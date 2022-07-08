class Node:
  def __init__(self, value, next_node=None, prev_node=None):
    self.value = value
    self.next_node = next_node
    self.prev_node = prev_node

  def set_next_node(self, next_node):
    self.next_node = next_node

  def get_next_node(self):
    return self.next_node

  def set_prev_node(self, prev_node):
    self.prev_node = prev_node

  def get_prev_node(self):
    return self.prev_node

  def get_value(self):
    return self.value


class DoublyLinkedList:
  def __init__(self, head_node=None, tail_node=None):
    self.head_node = head_node
    self.tail_node = tail_node
