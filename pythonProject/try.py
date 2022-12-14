import main

# ghost game board is for calculating appropraite moves
ghost_game_board = [["N", "N", "N"], ["N", "N", "N"], ["N", "N", "N"]]

print("---ARRAY INITIALLY---")
main.print_board(ghost_game_board)

# starting position
ghost_game_board[1][0] = "R"
position_of_r = [1,0]

print("\n---ARRAY FILLED---")
main.print_board(ghost_game_board)

goal_states = [main.GoalState("R", [2, 2])]

# Example for uniform cost search

# COSTS FOR "R"
# right or left move - cost = 1
# up of down move - cost = 1
# if the all paths has the same cost, priority ordering is right > left > up > down

class Node:
def observe(board, colorInitial):


def move_R(board):
    if position_of_r == goal_states[0].place:
        print("R is at goal state")
    else:

