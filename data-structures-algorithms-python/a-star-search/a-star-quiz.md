#### Given a current vertex, how would the A* algorithm determine the likely cost of following a path in the direction of a neighboring vertex?

- [ ] A* would use sum of the distance up to the current vertex, the edge weight to the neighbor, and the heuristic distance calculation from the current vertex to the target.
- [ ] A* would use sum of the distance up to the current vertex and the heuristic distance calculation from the neighbor to the target.
- [x] A* would use sum of the distance up to the current vertex, the edge weight to the neighbor, and the heuristic distance calculation from the neighbor to the target.
- [ ] A* would use sum of the distance up to the current vertex and the edge weight to the neighbor.

#### Which heuristic is depicted?

    def heuristic(start, target):
      x_distance = abs(start.position[0] - target.position[0])
      y_distance = abs(start.position[1] - target.position[1])
      return x_distance + y_distance

- [ ] Diagonal distance heuristic
- [ ] Euclidean heuristic
- [x] Manhattan heuristic

#### When determining the best path from one city to another, which heuristic would be admissible? (You can assume that at least some of these cities have paths between them that are curved or diagonal.)

- [ ] The Manhattan heuristic
- [x] The Euclidean heuristic

#### Fix the code so that new_path is equal to the correct path to neighbor!

    class graph_vertex:
      def __init__(self, name, x, y):
        self.name = name
        self.position = (x, y)

    def a_star(graph, start, target):
      paths_and_distances = {}
      for vertex in graph:
        paths_and_distances[vertex] = [inf, [start.name]]

      paths_and_distances[start][0] = 0
      vertices_to_explore = [(0, start)]
      while vertices_to_explore and paths_and_distances[target][0] == inf:
        current_dist, current_vtx = heappop(vertices_to_explore)
        for neighbor, edge_weight in graph[current_vtx]:
          new_distance = current_dist + edge_weight + heuristic(neighbor, target)
          # Fix the line below:
          new_path

- [x] = paths_and_distances[current_vtx][1] + [neighbor.name]
- [ ] += paths_and_distances[neighbor][1]
- [ ] = paths_and_distances[neighbor][1] - [neighbor.name]
- [ ] = paths_and_distances[neighbor][1] + [current_vtx.name]

#### Which of the following is NOT a difference between the Dijkstra’s and A* algorithms?

- [ ] A* can tell if it is heading in the correct direction while Dijsktra’s cannot.
- [ ] The A* algorithm uses a heuristic while Dijkstra’s algorithm does not.
- [x] Dijskra’s algoritm uses edge weights while A* does not.
- [ ] Dijkstra’s algorithm can be used to find paths to all vertices from a given start vertex, while A* requires a target vertex.

#### What would be an ideal situation to use the Manhattan heuristic with A*?

- [x] When vertices are distributed across a grid with no diagonal movement.
- [ ] When the vertices have latitudinal and longitudinal values.
- [ ] When the start and target vertices have the same positional x or y values.
- [ ] When diagonal movement is allowed between vertices.

#### How is the Euclidean heuristic calculated?

- [ ] The difference between the x-distance and the y-distance.
- [ ] The x-distance multiplied by the y-distance.
- [x] The square root of the sum of the x-distance squared and the y-distance squared.
- [ ] The sum of the x-distance and the y-distance.
