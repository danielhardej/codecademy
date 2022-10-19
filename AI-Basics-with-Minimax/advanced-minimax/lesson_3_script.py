# Using the evaluation function

from connect_four import *
import random
random.seed(108)

def evaluate_board(board):
    if has_won(board, "X"):
      return float("Inf")
    elif has_won(board, "O"):
      return -float("Inf")
    else:
      num_top_x = 0
      num_top_o = 0
      for column in board:
        for square in column:
          if square == "X":
            num_top_x += 1
            break
          if square == "O":
            num_top_o += 1
            break
      return num_top_x - num_top_o

print_board(board_one)
print(evaluate_board(board_one))
print_board(board_two)
print(evaluate_board(board_two))
print_board(board_three)
print(evaluate_board(board_three))
