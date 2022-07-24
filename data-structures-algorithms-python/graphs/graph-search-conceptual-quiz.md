#### In order to keep track of vertices throughout its search, DFS employs the use of a __ data structure.

- [ ] queue
- [ ] hash map
- [x] stack
- [ ] heap

#### When would it make more sense to use breadth-first search than depth-first search?

- [ ] When you want to find out if a solution exists for a maze.
- [x] When you want to build a GPS system that finds the shortest route between two points on a map.
- [ ] When you want to traverse all values in a graph.
- [ ] When you want to identify a cycle within the graph.

#### Which type of graph search generally employs recursion?

- [x] Depth-first search
- [ ] Breadth-first search

#### Which graph traversal could have given you this list?

    ["sharks", "bees", "crocodiles", "sharks (reprise)", "piranhas", "lava", "fire pit", "blow torches", "lasers"]

##### Note that this graph is undirected, so the search could move just as easily from “crocodiles” to “sharks” as the reverse. You can assume that the search will use alphabetical order to choose between two potential next vertices.

    https://content.codecademy.com/programs/cs-path/graph-search/graph%20search.svg

- [ ] A post-order traversal beginning with “lasers.”
- [ ] A reverse post-order traversal beginning with “sharks.”
- [x] A pre-order traversal beginning with “sharks.”

#### In order to keep track of vertices throughout its search, BFS employs the use of a __ data structure.

- [x] queue
- [ ] hash map
- [ ] stack
- [ ] heap

#### Which asymptotic notation describes the runtime for graph search algorithms?

    a. O(vertices−edges)
    b. Ω(vertices+edges)
    c. O(vertices+edges)
    d. Θ(vertices∗log edges)
​
- [ ] b.
- [ ] a.
- [x] c.
- [ ] d.

#### You can use a graph search algorithm to __.

- [ ] locate the largest or smallest value in a graph data structure
- [ ] locate a graph data structure within another data structure
- [x] traverse the entirety of a graph data structure to locate a specific value
- [ ] locate all values on the graph that are greater than the value passed in
