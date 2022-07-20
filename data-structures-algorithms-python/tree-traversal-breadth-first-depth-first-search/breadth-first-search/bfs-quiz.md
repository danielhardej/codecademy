#### What two points of data are needed to perform a breadth-first search on a tree?

- [ ] A queue and a stack
- [x] The root node of a tree and a goal value
- [ ] A goal value and a node path
- [ ] The root node of a tree and a frontier queue

#### What type of algorithm is a breadth-first search?

- [ ] Binary Search
- [x] Tree traversal
- [ ] Heapsort
- [ ] Randomized

#### What is the purpose of the frontier queue in a breadth-first search?

- [ ] To store node values that will be checked against the goal value.
- [x] To store nodes, or paths to nodes, that will be searched.
- [ ] To store previously searched node values.
- [ ] To store all the unsearched nodes in a tree.

#### Complete the breadth-first search code that stores tree nodes in the frontier queue.

    while frontier_queue:
      current_node = frontier_queue.pop()

      if current_node.value == goal_value:
        return current_node

      for child in current_node.children:
        frontier_queue.appendleft(child)

#### True or False: If the next node to be searched has 3 children, the length of the queue will increase by 3 at the end of the search loop.

- [x] False
- [ ] True

#### During a breadth-first search of the following tree, the node with the value 2 is searched and the paths to its children need to be added to the frontier queue. Given what you know about the search pattern of the breadth-first search, what two path lists will be added to the frontier queue?

        1
       / \
      2   3
     / \ / \
    4  5 6  7

- [ ] [2, 4] [2, 5]
- [ ] [4, 2, 1] [5, 2, 1]
- [ ] [1,4] [1,5]
- [x] [1, 2, 4] [1, 2, 5]
