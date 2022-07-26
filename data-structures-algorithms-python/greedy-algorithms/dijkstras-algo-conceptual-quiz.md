#### Why must we initialize all the distances from the start vertex to infinity at the beginning of Dijkstra’s algorithm?

- [ ] Setting the distances to 0 would take longer.
- [ ] We need to initialize the values to something, so it might as well be infinity.
- [ ] In Dijkstra’s, we take the maximum distance, so we should initialize the distances to the highest value possible.
- [x] Since we haven’t searched the graph yet, we don’t know the distances, and thus, we must assume the maximum possible distance.

#### Challenge Question: Would Dijkstra’s Algorithm be able to work with negative edge weights?

- [x] No
- [ ] Yes

#### Why does Dijkstra’s algorithm run in O((V+E)log V)?

- [ ] In the worst case, we will visit all log V vertices and edges. In each visit, we may have to update our min-heap which takes V+E time. Thus, the runtime is O((V+E) log V)).
- [x] In the worst case, we will visit all V+E vertices and edges. In each visit, we may have to update our min-heap which takes log V time. Thus, the runtime is O((V+E) log V)).
- [ ] Breadth first search runs in O((V+E) log V), and because Dijkstra’s algorithm uses a breadth first search, it must have the same runtime.

#### What is wrong with the following pseudocode for Dijkstra’s algorithm?

    - Set all distances to all other vertices from start vertex to infinity
    - while heap exists:
        - pop vertex with mininum distance
        - check neighbors of that vertex:
              - new distance = distance to vertex + edge weight
              - if new distance > current distance:
                     - replace current distance with new distance
    - return distances

- [ ] We aren’t creating a new heap every iteration.
- [ ] We aren’t marking all of our neighbors as visited.
- [x] We are checking if the new distance is greater than the current distance but we should check if it is less than the current distance.
- [ ] We should be popping the vertex with the maximum distance.

#### True or False: Dijkstra’s algorithm follows a breadth first search rather than a depth-first-search.

- [ ] False
- [x] True
