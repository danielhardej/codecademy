# Pointers at Different Speeds
# Using two pointers moving in parallel was a good solution to the previous problem. However, there are other problems where having two pointers moving in parallel wouldn’t be as useful. Let’s take a look at one of those problems and consider a new strategy that uses two pointers moving at different speeds.
#
# Consider the following problem:
#
# Create a method that returns the middle node of a linked list.
#
# For example, given the linked list with the following elements 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7, the middle node would be the element with value 4.
#

from LinkedList import LinkedList

# Complete this function:
def find_middle(linked_list):
  fast_pointer = linked_list.head_node
  slow_pointer = linked_list.head_node
  while fast_pointer:
    fast_pointer = fast_pointer.get_next_node()
    if fast_pointer:
      fast_pointer = fast_pointer.get_next_node()
      slow_pointer = slow_pointer.get_next_node()
  return slow_pointer

def generate_test_linked_list(length):
  linked_list = LinkedList()
  for i in range(length, 0, -1):
    linked_list.insert_beginning(i)
  return linked_list



test_list = generate_test_linked_list(7)
print(test_list.stringify_list())
middle_node = find_middle(test_list)
print(middle_node.value)
