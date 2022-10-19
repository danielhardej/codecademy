# Implement Alpha-Beta Pruning
#
# Alpha-beta pruning is accomplished by keeping track of two variables for each
# node — alpha and beta. alpha keeps track of the minimum score the maximizing
# player can possibly get. It starts at negative infinity and gets updated as
# that minimum score increases.
#
# On the other hand, beta represents the maximum score the minimizing player
# can possibly get. It starts at positive infinity and will decrease as that
# maximum possible score decreases.
#
# For any node, if alpha is greater than or equal to beta, that means that
# we can stop looking through that node’s children.

from connect_four import *
import random
random.seed(108)

def minimax(input_board, is_maximizing, depth, alpha, beta):
  # alpha keeps track of the minimum score the maximizing player can possibly get
  # beta represents the maximum score the minimizing player can possibly get
  # Base case - the game is over, so we return the value of the board
  if game_is_over(input_board) or depth == 0:
    return [evaluate_board(input_board), "", alpha, beta]
  best_move = ""
  if is_maximizing == True:
    best_value = -float("Inf")
    symbol = "X"
  else:
    best_value = float("Inf")
    symbol = "O"
  for move in available_moves(input_board):
    new_board = deepcopy(input_board)
    select_space(new_board, move, symbol)
    hypothetical_value = minimax(new_board, not is_maximizing, depth - 1, alpha, beta)[0]
    if is_maximizing == True and hypothetical_value > best_value:
      best_value = hypothetical_value
      best_move = move
      alpha = max(alpha, best_value)
    if is_maximizing == False and hypothetical_value < best_value:
      best_value = hypothetical_value
      best_move = move
      beta = min(beta, best_value)
    if alpha >= beta:
      break
  return [best_value, best_move, alpha, beta]

print_board(board)
print(minimax(board, True, 6, -float("Inf"), float("Inf")))
