#### The following code is the first part of Dijkstra’s algorithm. What should the ??? be?

    distances = {}
    previous = {}
    distances[start] = 0
    heap = [(0, start)]
    visited = set()
    for vertex in graph:
      if vertex is not start:
        distances[vertex] = ???
        heapq.heappush(heap, (distances[vertex], vertex))

- [x] math.inf
- [ ] previous[start]
- [ ] 0
- [ ] distances[start]

#### What is the purpose of line 2?

    while heap:
      current_distance, current_vertex = heapq.heappop(heap)
      ......
      ......
      ......

- [x] We want to pop off the vertex with the mininum distance because in Dijkstra’s we want to keep track of the shortest path.
- [ ] We want to get rid of all of the smallest distances so we are left with the largest distance.
- [ ] We want to sum all the mininum distances!

#### What is wrong with the following code?

     for neighbor, edge_weight in graph[current_vertex]:
        new_distance = current_distance + edge_weight
        if new_distance == distances[neighbor]:
          distances[neighbor] = new_distance
          heapq.heappush(heap, (new_distance, neighbor))
          previous[neighbor] = current_vertex

- [x] We should check if new_distance < distances[neighbor] instead of checking if it’s equal.
- [ ] We should pop from the heap intead of pushing to it in the loop.
- [ ] We should check if new_distance > distances[neighbor] instead of checking if it’s equal.
- [ ] We should set distances[neighbor] = current_distance in the if statement.

#### True or False: Dijkstra’s algorithm checks all the neighbors of the current vertex.

- [x] True
- [ ] False

#### Why do we use heapq to implement Dijkstra’s Algorithm in python?

- [ ] Heaps have the same structure as graphs.
- [ ] It allows us to easily pop off the maximum distance and it only takes O(log V) to update the heapq.
- [x] It allows us to easily pop off the mininum distance and it only takes O(log V) to update the heapq.
- [ ] Heaps have the best runtime for adding elements.
