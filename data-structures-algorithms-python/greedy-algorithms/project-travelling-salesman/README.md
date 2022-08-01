### Codecademy Traveling Salesman Project

To be honest, this was a poorly thought out project from Codecademy - they're usually much better than this.

The tasks and the script they want you to write does not give a complete solution to the traveling salesman problem - it only covers part of it.
The test case they give you is also too basic, and even this one comes back with erratic results (try running it several times and see you get a different result every time, some of which give a a result close to the min but not the smallest possible path length.)

The improvements I made are as follows.
 - Adding a new function for building a more interesting and bigger graph (see build_graph, which can be found in a previous lesson on graphs.)
 - Adding a section of the main program that will repeat the path finding process multiple times (see variable n_attempts.)
 - In the main program, while the n_attempts at pathfinding are being completed, the shortest path is saved to the variable shortest_path, and the length of the shortest path is saved to the variable shortest_path_len (easy to remember!)
 - Finally, the different paths found and the number of times they're found are saved to the dict path_count. At the end we see how many times each path is taken and we should end up with the shortest path also being the most frequently taken.
