import random
from random import randrange
from Graph import Graph
from Vertex import Vertex

def print_graph(graph):
  print("\nHello this is your graph:")
  for vertex in graph.graph_dict:
    print("")
    print(vertex + " connected to")
    vertex_neighbors = graph.graph_dict[vertex].edges
    if len(vertex_neighbors) == 0:
      print("No edges!")
    for adjacent_vertex in vertex_neighbors:
      print("=> " + adjacent_vertex)

def build_tsp_graph(directed):
  g = Graph(directed)
  vertices = []
  for val in ['a', 'b', 'c', 'd', 'e', 'f']:
    vertex = Vertex(val)
    vertices.append(vertex)
    g.add_vertex(vertex)

  g.add_edge(vertices[0], vertices[1], 3)
  g.add_edge(vertices[0], vertices[2], 4)
  g.add_edge(vertices[0], vertices[3], 5)
  g.add_edge(vertices[1], vertices[0], 3)
  g.add_edge(vertices[1], vertices[2], 2)
  g.add_edge(vertices[1], vertices[3], 6)
  g.add_edge(vertices[2], vertices[0], 4)
  g.add_edge(vertices[2], vertices[1], 2)
  g.add_edge(vertices[2], vertices[3], 1)
  g.add_edge(vertices[3], vertices[0], 5)
  g.add_edge(vertices[3], vertices[1], 6)
  g.add_edge(vertices[3], vertices[2], 1)
  g.add_edge(vertices[4], vertices[0], 3)
  g.add_edge(vertices[4], vertices[2], 1)
  g.add_edge(vertices[4], vertices[3], 1)
  g.add_edge(vertices[5], vertices[0], 3)
  g.add_edge(vertices[5], vertices[1], 2)
  g.add_edge(vertices[5], vertices[4], 4)

  return g

def visited_all_nodes(visited_vertices):
  for vertex in visited_vertices:
    if visited_vertices[vertex] == "unvisited":
      return False
  return True

def traveling_salesman(graph):
  ts_path = ""
  visited_vertices = {x: "unvisited" for x in graph.graph_dict}
  current_vertex = random.choice(list(graph.graph_dict))
  visited_vertices[current_vertex] = "visited"
  ts_path += current_vertex
  visited_all_vertices = visited_all_nodes(visited_vertices)

  while not visited_all_vertices:
    current_vertex_edges = graph.graph_dict[current_vertex].get_edges()
    current_vertex_edge_weights = {}
    for edge in current_vertex_edges:
      current_vertex_edge_weights[edge] = graph.graph_dict[current_vertex].get_edge_weight(edge)

    found_next_vertex = False
    next_vertex = ""

    while not found_next_vertex:
      if current_vertex_edge_weights is None:
        break
      next_vertex = min(current_vertex_edge_weights, key=current_vertex_edge_weights.get)
      if visited_vertices[next_vertex] == "visited":
        current_vertex_edge_weights.pop(next_vertex)
      else:
        found_next_vertex = True
    if current_vertex_edge_weights is None:
      visited_all_vertices = True
    else:
      current_vertex = next_vertex
      visited_vertices[current_vertex] = "visited"
      ts_path += current_vertex

    visited_all_vertices = visited_all_nodes(visited_vertices)

  return ts_path


### Main program ###                TODO: tidy it up!
graph = build_tsp_graph(False)
print_graph(graph)
#print(graph.graph_dict)

n_attempts = 100
path_count = {}
shortest_path = ""
shortest_path_len = 10000

for n in range(n_attempts):
  current_path = traveling_salesman(graph)
  ts_path_list = [v for v in current_path]
  path_len = 0
  for i in range(len(ts_path_list) - 1):
    edge_len = graph.graph_dict[ts_path_list[i]].get_edge_weight(ts_path_list[i+1])
    path_len += edge_len
  # print("Path {0}: {1}".format(n+1, current_path))
  # print("Path length: " + str(path_len))
  if path_len < shortest_path_len:
    shortest_path = current_path
    shortest_path_len = path_len

  if shortest_path in path_count:
    path_count[shortest_path] += 1
  else:
    path_count[shortest_path] = 1

print("\nShortest path: " + shortest_path)
print("Shortest path len: " + str(shortest_path_len))
print(path_count)

most_common_path = [path for path, value in path_count.items() if value == max(path_count.values())]
print("Most common path: {}".format(most_common_path[0]))
