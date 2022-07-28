#### Why is O(b^d) not the better way to describe the runtime of A* in comparison to O((V+E) log V)?

- [ ] It is better because A* actually runs slower than Dijkstra’s.
- [x] It is better because it doesn’t take into account the vertices and edges that you will not be visiting due to the optimization of A*.
- [ ] It is better because it considers all paths to the goal vertex!

#### Which of the following is a good reason to choose Dijkstra’s algorithm instead of A*?

- [ ] In some graphs, we can use heuristics to estimate the distance.
- [x] Sometimes we want the shortest pathways to several different vertices.
- [ ] Sometimes it is unecessary to traverse the entire graph.
- [ ] Sometimes we have a specific goal vertex we can optimize for.

#### True or False: For, A* algorithm, we want to pop off our minimum vertex while taking into consideration the heuristic distance.

- [x] True
- [ ] False

#### Which of the following statements is FALSE?

- [ ] In Dijkstra’s algorithm, we don’t have heuristic values.
- [ ] A* and Dijkstra’s both use a min-heap to keep track of distances.
- [x] Unlike in A*, in Dijkstra’s we iterate through the neighbors of the current vertex.
- [ ] A* and Dijkstra’s have different runtimes.

#### True or False: A* is a greedy algorithm.

- [x] True
- [ ] False
