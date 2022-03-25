from tictactoe import *

EMPTY = None

x = "X"
o = "O"
board = [[EMPTY, "X", "O"],
         ["O", "X", "X"],
         ["X", EMPTY, "O"]]


max_player = x
min_player = o
next_player = player(board)

possible_boards = []
possible_actions = actions(board)
for action in possible_actions:
    possible_boards.append(result(board, action))

for boards in possible_boards:
    possible_action = actions(boards)
    resultant_board =
