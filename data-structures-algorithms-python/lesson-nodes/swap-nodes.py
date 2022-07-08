# Swapping elements in a linked list
# Given an input of a linked list, val1, and val2, the general steps for swapping elements 
# in a linked list is as follows:
#
#     Iterate through the list looking for the node that matches val1 to be swapped (node1), keeping track of the node’s previous node as you iterate (node1_prev)
#     Repeat step 1 looking for the node that matches val2 (giving you node2 and node2_prev)
#     If node1_prev is None, node1 was the head of the list, so set the list’s head to node2
#     Otherwise, set node1_prev‘s next node to node2
#     If node2_prev is None, set the list’s head to node1
#     Otherwise, set node2_prev‘s next node to node1
#     Set node1‘s next node to node2‘s next node
#     Set node2‘s next node to node1‘s next node


import Node
import LinkedList

def swap_nodes(input_list, val1, val2):
  print(f'Swapping {val1} with {val2}')

  node1_prev = None
  node2_prev = None
  node1 = input_list.head_node
  node2 = input_list.head_node

  if val1 == val2:
    print("Elements are the same - no swap needed")
    return

  while node1 is not None:
    if node1.get_value() == val1:
      break
    node1_prev = node1
    node1 = node1.get_next_node()

  while node2 is not None:
    if node2.get_value() == val2:
      break
    node2_prev = node2
    node2 = node2.get_next_node()

  if (node1 is None or node2 is None):
    print("Swap not possible - one or more element is not in the list")
    return

  if node1_prev is None:
    input_list.head_node = node2
  else:
    node1_prev.set_next_node(node2)

  if node2_prev is None:
    input_list.head_node = node1
  else:
    node2_prev.set_next_node(node1)

  temp = node1.get_next_node()
  node1.set_next_node(node2.get_next_node())
  node2.set_next_node(temp)


ll = LinkedList.LinkedList()
for i in range(10):
  ll.insert_beginning(i)

print(ll.stringify_list())
swap_nodes(ll, 9, 5)
print(ll.stringify_list())
