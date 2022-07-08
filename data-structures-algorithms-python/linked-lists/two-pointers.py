# Two Pointers Moving in Parallel
# Consider the following problem:
# Create a method that returns the nth last element of a singly linked list.
# For example: given a linked list with the following elements 1 -> 2 -> 3 -> 4 -> 5, return the 2nd to last element. The answer would be element 4.
# In order to do this, you’ll need some way of knowing how far you are from the end of the list itself. However, in a singly linked list, there’s no easy way to iterate back through the list when you find the end.


from LinkedList import LinkedList

# Complete this function:
def nth_last_node(linked_list, n):
  nth_last_pointer = None
  tail_pointer = linked_list.head_node
  count = 1

  while tail_pointer:
    tail_pointer = tail_pointer.get_next_node()
    count += 1

    if count >= n + 1:
      if nth_last_pointer is None:
        nth_last_pointer = linked_list.head_node
      else:
        nth_last_pointer = nth_last_pointer.get_next_node()

  return nth_last_pointer

def generate_test_linked_list():
  linked_list = LinkedList()
  for i in range(50, 0, -1):
    linked_list.insert_beginning(i)
  return linked_list


test_list = generate_test_linked_list()
print(test_list.stringify_list())
nth_last = nth_last_node(test_list, 4)
print(nth_last.value)
