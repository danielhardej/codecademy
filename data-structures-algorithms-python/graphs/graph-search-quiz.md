####In a DFS implementation looking for a path between two points, what happens if the current vertex has the target value?

    if current_vertex is target_value:
      # what lines goes here?

- [x] return visited
- [ ] return current_vertex
- [ ] return target_value
- [ ] return graph


#### Inside a breadth-first search implementation, you have a for loop of the current vertex’s neighboring vertices. What needs to be true in this loop in order for the path to be returned?

- [ ] The current vertex has the target value.
- [ ] The neighboring vertex has not been visited.
- [x] The neighboring vertex has not been visited AND the neighboring vertex has the target value.
- [ ] The neighboring vertex has been visited AND the neighboring vertex has the target value.


#### Why is visited included in the parameters of this depth-first search implementation?

    def dfs(graph, current_vertex, target_value, visited = None):
      if visited is None:
        visited = []

      visited.append(current_vertex)

      if current_vertex is target_value:
        return visited

      for neighbor in graph[current_vertex]:
        if neighbor not in visited:
          return dfs(graph, neighbor, target_value, visited)

- [ ] It isn’t possible to define variables inside the function body.
- [ ] It doesn’t need to be; it could be defined as an empty list on the first line of the function body.
- [x] visited will be passed in to continue building out the path during recursive calls.
- [ ] It might be necessary to pass in a value to visited if starting the search from a different point on the graph than the first-added vertex.


#### Which for loop might be part of a breadth-first search Python implementation?

    # A:
    for neighbor in graph[current_vertex]:
      if neighbor not in visited:
        if neighbor is target_value:
          return path + [neighbor]
        else:
          search_queue.append([neighbor, path + [neighbor]])

    # B:
    for neighbor in graph[current_vertex]:
      if neighbor not in visited:
        return search(graph, neighbor, target_value, visited)

- [x] A
- [ ] B

#### Complete the return statement for the base case of this DFS implementation:

    def dfs(graph, current_vertex, target_value, visited = None):
      if visited is None:
        visited = []
      visited.append(current_vertex)
      if current_vertex is target_value:
        return # What goes here?

      for neighbor in graph[current_vertex]:
        if neighbor not in visited:
          return dfs(graph, neighbor, target_value, visited)

- [ ] path
- [x] visited
- [ ] target_value
- [ ] graph
- [ ] current_vertex

#### What’s the purpose of having a set called visited in a BFS Python implementation?

- [ ] To keep track of vertices that still need to be explored.
- [x] To store up all visited vertices so as not to revisit any.
- [ ] In order to check the target_value against.
- [ ] To collect all visited vertices and return them as the BFS path.


#### Complete the if statement in this depth-first search implementation.

    def dfs(graph, current_vertex, target_value, visited = None):
      if #What goes here? <---- :
        visited = []
      visited.append(current_vertex)
      if current_vertex is target_value:
        return visited

      for neighbor in graph[current_vertex]:
        if neighbor not in visited:
          return dfs(graph, neighbor, target_value, visited)

    some_important_graph = {
        'lava': set(['sharks', 'piranhas']),
        'sharks': set(['lava', 'bees', 'lasers']),
        'piranhas': set(['lava', 'crocodiles']),
        'bees': set(['sharks']),
        'lasers': set(['sharks', 'crocodiles']),
        'crocodiles': set(['piranhas', 'lasers'])
      }

- [ ] target_value in visited
- [ ] current_vertex != target_value
- [ ] visited
- [x] visited is None
- [ ] graph[0] is current_vertex
