# This is a sample Python script.
import a_star_algorithm
from a_star_algorithm import astar


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

class State:
    initial = ""
    place = [0, 0]

    def __init__(self, initial, place):
        self.initial = initial
        self.place = place


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def print_board(board):
    print("-------------")
    for row in board:
        print("| ", end="")
        for tile in row:
            print(tile + " | ", end="")
        print("\n-------------")


def is_replacement_in_board(row, col):
    if 2 >= row >= 0:
        if 2 >= col >= 0:
            return 1
    else:
        return 0


def is_initial_valid(initial):
    if initial == "R" or initial == "G" or initial == "B":
        return 1


def go_left(array, color_initial):
    for i in range(3):
        for j in range(3):
            if array[i][j] == color_initial:
                print("FOUND: " + color_initial)
                if j != 0:
                    if array[i][j - 1] == "N":
                        array[i][j] = "N"
                        array[i][j - 1] = color_initial
                        return
                    else:
                        # TODO: What happens if it cannot go because there is another color?
                        print("Given value is on [" + str(i) + "][" + str(j) + "] - there is another color - cannot "
                                                                               "go left")
                else:
                    # TODO: What happens if it cannot go because of board boundary?
                    print("Given value is on [" + str(i) + "][" + str(j) + "] - left is empty - cannot go left")


def go_right(array, color_initial):
    for i in range(3):
        for j in range(3):
            if array[i][j] == color_initial:
                print("FOUND: " + color_initial)
                if j != 2:
                    if array[i][j + 1] == "N":
                        array[i][j] = "N"
                        array[i][j + 1] = color_initial
                        return
                    else:
                        # TODO: What happens if it cannot go because there is another color?
                        print("Given value is on [" + str(i) + "][" + str(j) + "] - there is another color - cannot "
                                                                               "go right")
                else:
                    # TODO: What happens if it cannot go because of board boundary?
                    print("Given value is on [" + str(i) + "][" + str(j) + "] - left is empty - cannot go right")


def go_up(array, color_initial):
    for i in range(3):
        for j in range(3):
            if array[i][j] == color_initial:
                print("FOUND: " + color_initial)
                if i != 0:
                    if array[i - 1][j] == "N":
                        array[i][j] = "N"
                        array[i - 1][j] = color_initial
                        return
                    else:
                        # TODO: What happens if it cannot go because there is another color?
                        print("Given value is on [" + str(i) + "][" + str(j) + "] - there is another color - cannot "
                                                                               "go up")
                else:
                    # TODO: What happens if it cannot go because of board boundary?
                    print("Given value is on [" + str(i) + "][" + str(j) + "] - left is empty - cannot go up")


def go_down(array, color_initial):
    for i in range(3):
        for j in range(3):
            if array[i][j] == color_initial:
                print("FOUND: " + color_initial)
                if i != 2:
                    if array[i + 1][j] == "N":
                        array[i][j] = "N"
                        array[i + 1][j] = color_initial
                        return
                    else:
                        # TODO: What happens if it cannot go because there is another color?
                        print("Given value is on [" + str(i) + "][" + str(j) + "] - there is another color - cannot "
                                                                               "go down")
                else:
                    # TODO: What happens if it cannot go because of board boundary?
                    print("Given value is on [" + str(i) + "][" + str(j) + "] - left is empty - cannot go down")


# Press the green button in the gutter to run the script.


# See PyCharm help at https://www.jetbrains.com/help/pycharm/


# Our array is 3x3 and it represents the boars. "N" represents null tiles.
# All tiles are null at the beginning.
game_board = [["N", "N", "N"], ["N", "N", "N"], ["N", "N", "N"]]

print("---ARRAY INITIALLY---")
print_board(game_board)

rowR = 0
colR = 0
rowG = 0
colG = 0
rowB = 0
colB = 0

will_break = 0
while will_break == 0:
    print("\nPlease enter the initial state of R:")
    rowR = int(input("row: "))
    colR = int(input("column: "))
    print(str(rowR) + " " + str(colR))
    if is_replacement_in_board(rowR, colR) == 1:
        break
    else:
        print("\nPlease enter a value considering 3x3 board")

will_break = 0
while will_break == 0:
    print("\nPlease enter the initial state of G:")
    rowG = int(input("row: "))
    colG = int(input("column: "))
    if is_replacement_in_board(rowG, colG) == 1:
        if rowG == rowR & colG == colR:
            print("\nPlease enter a value that does not overlap with other colors")
        else:
            break
    else:
        print("\nPlease enter a value considering 3x3 board")

will_break = 0
while will_break == 0:
    print("\nPlease enter the initial state of B:")
    rowB = int(input("row: "))
    colB = int(input("column: "))
    if is_replacement_in_board(rowG, colG) == 1:
        if (rowB == rowR and colB == colR) or (rowB == rowG and colB == colG):
            print("\nPlease enter a value that does not overlap with other colors")
        else:
            break
    else:
        print("\nPlease enter a value considering 3x3 board")

game_board[rowR][colR] = "R"
game_board[rowG][colG] = "G"
game_board[rowB][colB] = "B"

print_board(game_board)

initial_states = [State("R", [rowR, colR]), State("G", [rowG, colG]), State("B", [rowB, colB])]



print("Please enter goal states of red, green and blue.")
will_break = 0
while will_break == 0:
    print("\nPlease enter the goal state of R:")
    rowR = int(input("row: "))
    colR = int(input("column: "))
    print(str(rowR) + " " + str(colR))
    if is_replacement_in_board(rowR, colR) == 1:
        break
    else:
        print("\nPlease enter a value considering 3x3 board")

will_break = 0
while will_break == 0:
    print("\nPlease enter the goal state of G:")
    rowG = int(input("row: "))
    colG = int(input("column: "))
    if is_replacement_in_board(rowG, colG) == 1:
        if rowG == rowR & colG == colR:
            print("\nPlease enter a value that does not overlap with other colors")
        else:
            break
    else:
        print("\nPlease enter a value considering 3x3 board")

will_break = 0
while will_break == 0:
    print("\nPlease enter the goal state of B:")
    rowB = int(input("row: "))
    colB = int(input("column: "))
    if is_replacement_in_board(rowG, colG) == 1:
        if (rowB == rowR and colB == colR) or (rowB == rowG and colB == colG):
            print("\nPlease enter a value that does not overlap with other colors")
        else:
            break
    else:
        print("\nPlease enter a value considering 3x3 board")

goal_states = [State("R", [rowR, colR]), State("G", [rowG, colG]), State("B", [rowB, colB])]

print("\n---ARRAY---")
print_board(game_board)

# go_left(game_board, "R")

true = 1
while true == 1:
    print("Please choose a searching strategy:")
    print("1) Uniform cost search")
    print("2) A* search")

    searchingAlgorithm = input("Your choice: ")

    if searchingAlgorithm == "1":
        initial_states = ["N", "N", "N"]

        print("Please enter the order of tiles that will do an action. Enter R for red, G for green and B for blue")

        while true == 1:
            initial_states[0] = input("First: ")
            if is_initial_valid(initial_states[0]) == 1:
                break
            else:
                print("Please enter a valid initial")

        while true == 1:
            initial_states[1] = input("Second: ")
            if is_initial_valid(initial_states[1]) == 1:
                if initial_states[0] == initial_states[1]:
                    print("Please enter another initial to continue")
                else:
                    break
            else:
                print("Please enter a valid initial")

        while true == 1:
            initial_states[2] = input("Third: ")
            if is_initial_valid(initial_states[2]) == 1:
                if initial_states[0] == initial_states[2] or initial_states[1] == initial_states[2]:
                    print("Please enter another initial to continue")
                else:
                    break
            else:
                print("Please enter a valid initial")

        print(initial_states)

        # TODO: UNIFORM COST
        break
    if searchingAlgorithm == "2":

        path_R = astar(game_board, (initial_states[0].place[0], initial_states[0].place[1]), (goal_states[0].place[0], goal_states[0].place[1]), "R")
        path_G = astar(game_board, (initial_states[1].place[0], initial_states[1].place[1]), (goal_states[1].place[0], goal_states[1].place[1]), "G")
        path_B = astar(game_board, (initial_states[2].place[0], initial_states[2].place[1]), (goal_states[2].place[0], goal_states[2].place[1]), "B")

        # order = ["0", "0", "0"]

        ordered_paths = [("N", []), ("N", []), ("N", [])]

        print("\n\nPlease enter the order of tiles that will do an action. Enter R for red, G for green and B for blue")

        while true == 1:
            state = input("First: ")
            if is_initial_valid(state) == 1:
                ordered_paths[0] = (state, path_R if state == "R" else path_G if state == "G" else path_B)
                break
            else:
                print("Please enter a valid initial")

        while true == 1:
            state = input("Second: ")
            if is_initial_valid(state) == 1:
                if ordered_paths[0][0] == state:
                    print("Please enter another initial to continue")
                else:
                    ordered_paths[1] = (state, path_R if state == "R" else path_G if state == "G" else path_B)
                    break
            else:
                print("Please enter a valid initial")

        while true == 1:
            state = input("Third: ")
            if is_initial_valid(state) == 1:
                if ordered_paths[0][0] == state or ordered_paths[1][0] == state:
                    print("Please enter another initial to continue")
                else:
                    ordered_paths[2] = (state, path_R if state == "R" else path_G if state == "G" else path_B)
                    break
            else:
                print("Please enter a valid initial")

        print("BOARD INITIALLY")
        print_board(game_board)

        print("Algoritim is running with the order: " + str(ordered_paths))

        break
    else:
        print("Please make a valid choice")
