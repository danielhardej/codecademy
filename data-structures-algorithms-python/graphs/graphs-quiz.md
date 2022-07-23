#### Select the code snippet which completes this definition of the Graph class.

    class Graph:
      def __init__(self, directed = False):
        self.graph_dict = {}
        self.directed = directed

      def add_vertex(self, node):
        self.graph_dict[node.value] = node

      def add_edge(self, from_node, to_node, weight = 0):
        self.graph_dict[from_node.value].add_edge(to_node.value, weight)
        # ????????:
          self.graph_dict[to_node.value].add_edge(from_node.value, weight)

      def find_path(self, from_node, to_node):
        start = [from_node]
        seen = {}
        while len(start) > 0:
          current_node = start.pop(0)
          seen[current_node] = True
          print("Visiting " + current_node)
          if current_node == to_node:
            return True
          else:
            nodes_to_visit = set(self.graph_dict[current_node].edges.keys())
            start += [node for node in nodes_to_visit if node not in seen]
        return False

- [ ] if self.directed:
- [x] if not self.directed:

#### Select the code snippet which completes this definition of the Graph class.

    class Graph:
      def __init__(self, directed = False):
        self.graph_dict = {}
        self.directed = directed

      def add_vertex(self, node):
        # ???????

      def add_edge(self, from_node, to_node, weight = 0):
        self.graph_dict[from_node.value].add_edge(to_node.value, weight)
        if not self.directed:
          self.graph_dict[to_node.value].add_edge(from_node.value, weight)

      def find_path(self, from_node, to_node):
        start = [from_node]
        seen = {}
        while len(start) > 0:
          current_node = start.pop(0)
          seen[current_node] = True
          print("Visiting " + current_node)
          if current_node == to_node:
            return True
          else:
            nodes_to_visit = set(self.graph_dict[current_node].edges.keys())
            start += [node for node in nodes_to_visit if node not in seen]
        return False

- [ ] self.graph_dict.append(node)
- [x] self.graph_dict[node.value] = node
- [ ] self.graph_dict += node
- [ ] self.graph_dict = node

#### Select the code snippet which completes this definition of the Vertex class.

    class Vertex:
      def __init__(self, value):
        self.value = value
        # ???????

      def add_edge(self, adjacent_value, weight = 0):
        self.edges[adjacent_value] = weight

      def get_edges(self):
        return list(self.edges.keys())

- [ ] self.edges = ""
- [x] self.edges = {}
- [ ] self.edges = []
- [ ] self.edges = None

#### What is the purpose of the following code?

    def ???????(self, from_node, to_node):
      start = [from_node]
      seen = {}
      while len(start) > 0:
        current_node = start.pop(0)
        seen[current_node] = True
        print("Visiting " + current_node)
        if current_node == to_node:
          return True
        else:
          nodes_to_visit = set(self.graph_dict[current_node].edges.keys())
          start += [node for node in nodes_to_visit if node not in seen]
      return False

- [ ] This method will return True if a cycle exists, and False otherwise.
- [ ] This method sets up a path between two vertices.
- [x] This method will return True or False depending on whether a path exists between from_node and to_node.
- [ ] This method will return a vertex instance if it exists in the graph.

#### Select the code snippet which completes this definition of the Vertex class.

    class Vertex:
      def __init__(self, value):
        self.value = value
        self.edges = {}

      def add_edge(self, adjacent_value, weight = 0):
        # ???????

      def get_edges(self):
        return list(self.edges.keys())

- [x] self.edges[adjacent_value] = weight
- [ ] self.edges = adjacent_value + weight
- [ ] self.adjacent_value = adjacent_value
- [ ] self.edges[weight] = adjacent_value

#### What is the purpose of the following code?

  def ???????(self, from_node, to_node, weight = 0):
    self.graph_dict[from_node.value].add_edge(to_node.value, weight)
    if not self.directed:
      self.graph_dict[to_node.value].add_edge(from_node.value, weight)

- [ ] This method removes an edge between two vertices.
- [ ] This method adds up the weights of two vertices.
- [x] This method sets an edge between two vertices.
- [ ] This method checks whether a path exists between two vertices.

#### Complete the missing line from the Graph method: .find_path().

     def find_path(self, from_node, to_node):
        # ????????
        seen = {}
        while len(start) > 0:
          current_node = start.pop(0)
          seen[current_node] = True
          print("Visiting " + current_node)
          if current_node == to_node:
            return True
          else:
            nodes_to_visit = set(self.graph_dict[current_node].edges.keys())
            start += [node for node in nodes_to_visit if node not in seen]
        return False

- [ ] start = [from_node, to_node]
- [ ] start = from_node
- [ ] start = [to_node]
- [x] start = [from_node]

#### Select the code snippet which completes this definition of the Graph class.

    class Graph:
      def __init__(self, directed = False):
        self.graph_dict = {}
        self.directed = directed

      def add_vertex(self, node):
        self.graph_dict[node.value] = node

      def add_edge(self, from_node, to_node, weight = 0):
        self.graph_dict[from_node.value].add_edge(to_node.value, weight)
        if not self.directed:
          self.graph_dict[to_node.value].add_edge(from_node.value, weight)

      def find_path(self, from_node, to_node):
        start = [from_node]
        seen = {}
        while len(start) > 0:
          current_node = start.pop(0)
          seen[current_node] = True
          print("Visiting " + current_node)
          if current_node == to_node:
            return True
          else:
            nodes_to_visit = set(self.graph_dict[current_node].edges.keys())
            # ????????
        return False

- [ ] start += nodes_to_visit
- [x] start += [node for node in nodes_to_visit if node not in seen]
- [ ] start = nodes_to_visit
