# Minimax Review Quiz

#### What is the advantage of alpha-beta pruning?

- [ ] The algorithm will stop before reaching the leaves of the tree, which drastically reduces the runtime.
- [x] The algorithm can explore deeper into the tree by ignoring branches known to be useless.
- [ ] Alpha-beta pruning speeds up the algorithm by optimizing the evaluation function of leaf nodes.
- [ ] Alpha-beta pruning speeds up the algorithm by ignoring the minimizing player’s moves and only focuses on the maximizing player.

#### In our implementation of the minimax algorithm, why do we return a list of two numbers?

- [x] The algorithm needs to keep track of the best value and the move associated with that value
- [ ] The algorithm needs to keep track of best possible move and the worst possible move.
- [ ] The algorithm needs to keep track of the minimum and maximum values for each node in the tree.
- [ ] The algorithm only needs to return a list of two values if we’re implementing alpha-beta pruning.

#### Given the following game tree, what will the value of the root node be?

![An tree with the leaves 5, 2, -1, -3, -10, -5, 27, and 4.](https://content.codecademy.com/courses/ds-minimax/quiz-tree.svg)

- [x] -1
- [ ] -5
- [ ] 5
- [ ] 27

#### Which evaluation function makes the most sense for a game of Connect Four?

- [x] The difference between the number of "X" streaks of three and the number of "O" streaks of three.
- [ ] The difference in the number of "X" pieces in odd columns and the number of "O" pieces in odd columns.
- [ ] The difference in the number of "X" pieces on the bottom row and the number of "O" pieces in the bottom row.
- [ ] The difference in the number of "X" pieces and the number of "O" pieces.

#### What does it mean for the value of a root node of the tree to be positive infinity? Assume it’s the maximizing player’s turn.

- [x] The maximizing player’s best move will eventually result in the maximizing player winning the game.
- [ ] It doesn’t matter what move the maximizing player picks - all moves will lead to their win.
- [ ] The maximizing player’s best move will eventually result in the minimizing player winning the game.
- [ ] It doesn’t matter what move the maximizing player picks - all moves will lead to the minimizing player winning.

#### What is the base case of the minimax algorithm for a complicated game like chess?

- [ ] depth = 0.
- [ ] The game is over.
- [ ] The game is over and depth = 0.
- [x] The game is over or depth = 0.

#### If our evaluation function counts the difference between the number of "X" pieces in odd columns and the number of "O" pieces in even columns, what would the value of this board be? (Note that this is a pretty lousy evaluation function in terms of finding a winner!)

![There are 3 Xs in odd columns and 5 Os in even columns.](https://content.codecademy.com/courses/ds-minimax/connect-four-quiz.svg)

- [ ] 0
- [x] -2
- [ ] 1
- [ ] -1

#### What does it mean for the value of a root node of the tree to be positive infinity? Assume it’s the minimizing player’s turn.


- [ ] If the minimizing player plays optimally, they are guaranteed to win the game.
- [ ] Only one of the minimizing players moves will result in the maximizing player winning the game.
- [ ] It doesn’t matter what the maximizing player does. They are guaranteed to win the game.
- [x] No matter what move the minimizing player makes, the maximizing player will win the game if they play optimally.

#### What does alpha represent when implementing alpha-beta pruning?

- [ ] alpha keeps track of the minimum value the minimizing player can get.
- [ ] alpha keeps track of the maximum value the minimizing player can get.
- [x] alpha keeps track of the minimum value the maximizing player can get.
- [ ] alpha keeps track of the maximum value the maximizing player can get.

#### What would it mean if the evaluation function of a non-leaf node returned -0.1.

- [ ] Your evaluation function thinks the minimizing player has won the game at that game state.
- [ ] Your evaluation function thinks the maximizing player has a slight advantage if the game reaches that game state.
- [x] Your evaluation function thinks the minimizing player has a slight advantage if the game reaches that game state.
- [ ] Your evaluation function thinks the maximizing player has won the game at that game state.
