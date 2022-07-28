# To build an A* implementation in Python, you begin with Dijkstra’s algorithm
# and then build on it. It means that most of the algorithm is already built out.
#
# There are only a few important changes you need to make:
#     Include a target for the search to find. No more searching in all directions for all destinations.
#     Collect and return the shortest path. A dictionary of distances is cool and all,
#     but A* is on a mission to get you to your target destination and tell you how to get there.
#     Build a heuristic that calculates the estimated distance between two points. This is
#     the crucial point of difference between Dijkstra’s and A*; A* has a real sense of direction.

from math import inf
from heapq import heappop, heappush
from manhattan_graph import manhattan_graph, thirty_sixth_and_sixth, grand_central_station

def modified_dijkstras(graph, start, target):
  print("Starting Dijkstra's algorithm!")
  count = 0
  paths_and_distances = {}
  for vertex in graph:
    paths_and_distances[vertex] = [inf, [start.name]]

  paths_and_distances[start][0] = 0
  vertices_to_explore = [(0, start)]

  while vertices_to_explore:
    current_distance, current_vertex = heappop(vertices_to_explore)
    for neighbor, edge_weight in graph[current_vertex]:
      new_distance = current_distance + edge_weight
      new_path = paths_and_distances[current_vertex][1] + [neighbor.name]
      if new_distance < paths_and_distances[neighbor][0]:
        paths_and_distances[neighbor][0] = new_distance
        paths_and_distances[neighbor][1] = new_path
        heappush(vertices_to_explore, (new_distance, neighbor))
        count += 1
        print("\nAt " + vertices_to_explore[0][1].name)
  print("Found a path in {0} steps: ".format(count), paths_and_distances[target][1])
  return paths_and_distances[target][1]

def heuristic(start, target):
  x_distance = abs(start.position[0] - target.position[0])
  y_distance = abs(start.position[1] - target.position[1])
  return x_distance + y_distance

def a_star(graph, start, target):
  print("Starting A* algorithm!")
  count = 0
  paths_and_distances = {}
  for vertex in graph:
    paths_and_distances[vertex] = [inf, [start.name]]

  paths_and_distances[start][0] = 0
  vertices_to_explore = [(0, start)]
  while vertices_to_explore and paths_and_distances[target][0] == inf:
    current_distance, current_vertex = heappop(vertices_to_explore)
    for neighbor, edge_weight in graph[current_vertex]:
      new_distance = current_distance + edge_weight + heuristic(neighbor, target)
      new_path = paths_and_distances[current_vertex][1] + [neighbor.name]

      if new_distance < paths_and_distances[neighbor][0]:
        paths_and_distances[neighbor][0] = new_distance
        paths_and_distances[neighbor][1] = new_path
        heappush(vertices_to_explore, (new_distance, neighbor))
        count += 1
        print("\nAt " + vertices_to_explore[0][1].name)

  print("Found a path in {0} steps: ".format(count), paths_and_distances[target][1])

  return paths_and_distances[target][1]


modified_dijkstras(manhattan_graph, thirty_sixth_and_sixth, grand_central_station)

a_star(manhattan_graph, thirty_sixth_and_sixth, grand_central_station)
