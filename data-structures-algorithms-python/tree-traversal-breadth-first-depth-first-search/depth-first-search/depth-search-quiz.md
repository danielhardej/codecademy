#### Which of the following is a valid reason that a given tree might be unsearchable by DFS?

- [ ] The tree could be a disjoint tree, or tree with gaps.
- [x] The tree could have too many nodes.
- [ ] The tree could include some nodes that have multiple parent nodes.
- [ ] The tree could have a cycle. For example, one of the nodes could have the root node of the tree as its child.

#### When might it be appropriate to use DFS to solve a problem?

- [ ] Compressing a sequence of data
- [x] Locating a valid path through a maze
- [ ] Find the input to a function that minimizes the output
- [ ] Sorting an array of strings


#### What is the time complexity of depth-first search when searching through a tree with n nodes?

- [ ] O(1)
- [x] O(n)
- [ ] O(log n)
- [ ] O(n^2)

#### When implementing DFS, we ___

- [x] can use either recursion or iteration.
- [ ] must use recursion.
- [ ] must invert the tree.
- [ ] cannot use recursion.

#### What is the space complexity of depth-first search when searching through a tree with n nodes?

- [x] O(n)
- [ ] O(n^2)
- [ ] O(1)
- [ ] O(log n)

#### The iterative implementation of the DFS algorithm utilizes a _____.

- [x] Stack
- [ ] Trie
- [ ] Circular Linked-List
- [ ] Queue

#### What’s something we could change about an implementation of the DFS algorithm to search for items in a tree with infinite depth or is otherwise too deep to practically search all nodes?

- [ ] Use multi-threading to search subtrees in parallel.
- [ ] Use the iterative implementation.
- [ ] Use the recursive implementation
- [x] Limit the search depth.

#### Which of the following statements about Depth-First Search is true?

- [x] DFS is guaranteed to find a solution if one exists, but the search space must be finite.
- [ ] There is no guarantee DFS will find a solution in any search space.
- [ ] DFS will always halt if there is a known solution in a tree of infinite depth.
- [ ] Only the iterative implementation has any guarantees about halting, the recursive implementation can get stuck in infinite loops.
