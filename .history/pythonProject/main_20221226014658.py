# This is a sample Python script.
import cost
from cost import calculateCost


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

class State:
    initial = ""
    place = [0, 0]

    def __init__(self, initial, place):
        self.initial = initial
        self.place = place


# correctPlace = 0


def move_tile(board, color_initial, state_list, goal_state_list):
    red_x = goal_states[0].place[0]
    red_y = goal_states[0].place[1]
    green_x = goal_states[1].place[0]
    green_y = goal_states[1].place[1]
    blue_x = goal_states[2].place[0]
    blue_y = goal_states[2].place[1]

    # global correctPlace

    # print(state_list[2].initial)
    index = 0 if color_initial == "R" else 1 if color_initial == "G" else 2

    correct_places = 0

    # print("WE ARE ON COLOR: " + color_initial)

    # print("CORRECT: " + str(correct_places))
    # print("       STATES       X      GOAL STATES")
    # print("       (" + str(state_list[0].place[0]) + ", " + str(state_list[0].place[1]) + ")              (" + str(
    #     goal_state_list[0].place[0]) + ", " + str(goal_state_list[0].place[1]) + ")")
    # print("       (" + str(state_list[1].place[0]) + ", " + str(state_list[1].place[1]) + ")              (" + str(
    #     goal_state_list[1].place[0]) + ", " + str(goal_state_list[1].place[1]) + ")")
    # print("       (" + str(state_list[2].place[0]) + ", " + str(state_list[2].place[1]) + ")              (" + str(
    #     goal_state_list[2].place[0]) + ", " + str(goal_state_list[2].place[1]) + ")")

    if state_list[0].place[0] == red_x and state_list[0].place[1] == red_y:
        correct_places = correct_places + 1
        # print("\nCorrect place if 1: \n" + str(correct_places))
        # print("R IS IN CORRECT PLACE")
    if state_list[1].place[0] == green_x and state_list[1].place[1] == green_y:
        correct_places = correct_places + 1
        # print("\nCorrect place if 2: \n" + str(correct_places))
        # print("G IS IN CORRECT PLACE")
    if state_list[2].place[0] == blue_x and state_list[2].place[1] == blue_y:
        correct_places = correct_places + 1
        # print("\nCorrect place if 3: \n" + str(correct_places))
        # print("B IS IN CORRECT PLACE")

    # print("\nCorrect place main: \n" + str(correct_places))

    path = calculateCost(board, (state_list[index].place[0], state_list[index].place[1]),
                 (goal_state_list[index].place[0], goal_state_list[index].place[1]), color_initial, correct_places,searchingAlgorithm)

    if path == 0:
        print("EXCEED EXPANSION CAPACITY! GOAL NODE NOT FOUND! SWITCHING TO THE NEXT COLOR!")
    else:
        if len(path) < 2:
            return 0
        state_list[index].place[0] = path[1][0]
        state_list[index].place[1] = path[1][1]
        move(board, color_initial, (path[1][0], path[1][1]))
        print_board(board)

        # print("CORRECT PLACE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!  :   " + str(correctPlace))

        if len(path) > 2:
            return 1


"""def move_tile(board, color_initial, state_list, goal_state_list):
    global correct_place
    print(state_list[2].initial)
    index = 0 if color_initial == "R" else 1 if color_initial == "G" else 2
    path = astar(board, (state_list[index].place[0], state_list[index].place[1]),
                 (goal_state_list[index].place[0], goal_state_list[index].place[1]), color_initial, correct_place)
    if len(path) < 2:
        return 0
    state_list[index].place[0] = path[1][0]
    state_list[index].place[1] = path[1][1]
    move(board, color_initial, (path[1][0], path[1][1]))
    print_board(board)
    if len(path) > 2:
        return 1"""


def move(array, color_initial, where):
    print("COLOR: " + color_initial)
    for i in range(3):
        for j in range(3):
            if array[i][j] == color_initial:
                print("FOUND: " + color_initial)
                array[where[0]][where[1]] = color_initial
                array[i][j] = "N"
                return


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
    # print(str(rowR) + " " + str(colR))
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
        if rowG == rowR and colG == colR:
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

states = [State("R", [rowR, colR]), State("G", [rowG, colG]), State("B", [rowB, colB])]

print("INITIALS: " + states[0].initial + " " + states[1].initial + " " + states[2].initial)

print("Please enter goal states of red, green and blue.")

while 1:
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
        if rowG == rowR and colG == colR:
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
        # states = ["N", "N", "N"]

        print("Please enter the order of tiles that will do an action. Enter R for red, G for green and B for blue")

        while true == 1:
            states[0] = input("First: ")
            if is_initial_valid(states[0]) == 1:
                break
            else:
                print("Please enter a valid initial")

        while true == 1:
            states[1] = input("Second: ")
            if is_initial_valid(states[1]) == 1:
                if states[0] == states[1]:
                    print("Please enter another initial to continue")
                else:
                    break
            else:
                print("Please enter a valid initial")

        while true == 1:
            states[2] = input("Third: ")
            if is_initial_valid(states[2]) == 1:
                if states[0] == states[2] or states[1] == states[2]:
                    print("Please enter another initial to continue")
                else:
                    break
            else:
                print("Please enter a valid initial")

        print(states)
        while (1):
               decision_point1 = move_tile(game_board, first, states, goal_states)
               decision_point2 = move_tile(game_board, second,states, goal_states)
               decision_point3 = move_tile(game_board, third, states, goal_states)

               if decision_point1 == 0 and decision_point2 == 0 and decision_point3 == 0:
                   break
        break
       
    elif searchingAlgorithm == "2":

        print("Please enter the order of tiles")
        first = input("First: ")
        second = input("Second: ")
        third = input("Third: ")

        while (1):
            decision_point1 = move_tile(game_board, first, states, goal_states)
            decision_point2 = move_tile(game_board, second, states, goal_states)
            decision_point3 = move_tile(game_board, third, states, goal_states)

            if decision_point1 == 0 and decision_point2 == 0 and decision_point3 == 0:
                break
        break