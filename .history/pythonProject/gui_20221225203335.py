import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from main import *
from cost  import calculateCost

class State:
    initial = ""
    place = [0, 0]

    def __init__(self, initial, place):
        self.initial = initial
        self.place = place

def move_tile(board, color_initial, state_list, goal_state_list):
    red_x = goal_states[0].place[0]
    red_y = goal_states[0].place[1]
    green_x = goal_states[1].place[0]
    green_y = goal_states[1].place[1]
    blue_x = goal_states[2].place[0]
    blue_y = goal_states[2].place[1]

    # global correctPlace

    print(state_list[2].initial)
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
                 (goal_state_list[index].place[0], goal_state_list[index].place[1]), color_initial, correct_places, searchingAlgorithm)

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


def move(array, color_initial, where):
    print("COLOR: " +color_initial)
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




root = tk.Tk()
root.title("Board Game")
root.geometry("900x600")

frameInitial = tk.Frame(root)
frameInitial.pack(padx=400, pady=50)

frameGoal = tk.Frame(root)
frameGoal.pack(padx=400, pady=100)

# INITIAL STATES

mainLabel = Label(root, text="Please enter inital states of nodes: ", font=('Times New Roman','18'), fg='black')
mainLabel.place(x=10,y=10)

# red initial

labelRed = Label(root, text="Red -> ", font=('Times New Roman','18'), fg='red')
labelRed.place(x=10,y=50)

labelRedRow = Label(root, text="row index:", font=('Times New Roman','18'), fg='red')
labelRedRow.place(x=100,y=50)

labelRedCol = Label(root, text="column index:", font=('Times New Roman','18'), fg='red')
labelRedCol.place(x=285,y=50)

RedRow = ttk.Combobox(root, width = 5)
RedRow.place(x=210,y=55)
RedRow['values'] = (0,1,2)

RedCol = ttk.Combobox(root, width = 5)
RedCol.place(x=430,y=55)
RedCol['values'] = (0,1,2)

# green initial

labelGreen = Label(root, text="Green -> ", font=('Times New Roman','18'), fg='green')
labelGreen.place(x=10,y=80)

labelGreenRow = Label(root, text="row index:", font=('Times New Roman','18'), fg='green')
labelGreenRow.place(x=100,y=80)

labelGreenCol = Label(root, text="column index:", font=('Times New Roman','18'), fg='green')
labelGreenCol.place(x=285,y=80)

GreenRow = ttk.Combobox(root, width = 5)
GreenRow.place(x=210,y=85)
GreenRow['values'] = (0,1,2)

GreenCol = ttk.Combobox(root, width = 5)
GreenCol.place(x=430,y=85)
GreenCol['values'] = (0,1,2)

# blue initial

labelBlue = Label(root, text="Blue -> ", font=('Times New Roman','18'), fg='blue')
labelBlue.place(x=10,y=110)

labelBlueRow = Label(root, text="row index:", font=('Times New Roman','18'), fg='blue')
labelBlueRow.place(x=100,y=110)

labelBlueCol = Label(root, text="column index:", font=('Times New Roman','18'), fg='blue')
labelBlueCol.place(x=285,y=110)

BlueRow = ttk.Combobox(root, width = 5)
BlueRow.place(x=210,y=115)
BlueRow['values'] = (0,1,2)

BlueCol = ttk.Combobox(root, width = 5)
BlueCol.place(x=430,y=115)
BlueCol['values'] = (0,1,2)

# GOAL STATES

mainLabelGoal = Label(root, text="Please enter goal states of nodes: ", font=('Times New Roman','18'), fg='black')
mainLabelGoal.place(x=10,y=300)

# red goal

labelRedGoal = Label(root, text="Red -> ", font=('Times New Roman','18'), fg='red')
labelRedGoal.place(x=10,y=340)

labelRedRowGoal = Label(root, text="row index:", font=('Times New Roman','18'), fg='red')
labelRedRowGoal.place(x=100,y=340)

labelRedColGoal = Label(root, text="column index:", font=('Times New Roman','18'), fg='red')
labelRedColGoal.place(x=285,y=340)

RedRowGoal = ttk.Combobox(root, width = 5)
RedRowGoal.place(x=210,y=345)
RedRowGoal['values'] = (0,1,2)

RedColGoal = ttk.Combobox(root, width = 5)
RedColGoal.place(x=430,y=345)
RedColGoal['values'] = (0,1,2)

# green goal

labelGreenGoal = Label(root, text="Green -> ", font=('Times New Roman','18'), fg='green')
labelGreenGoal.place(x=10,y=370)

labelGreenRowGoal = Label(root, text="row index:", font=('Times New Roman','18'), fg='green')
labelGreenRowGoal.place(x=100,y=370)

labelGreenColGoal = Label(root, text="column index:", font=('Times New Roman','18'), fg='green')
labelGreenColGoal.place(x=285,y=370)

GreenRowGoal = ttk.Combobox(root, width = 5)
GreenRowGoal.place(x=210,y=375)
GreenRowGoal['values'] = (0,1,2)

GreenColGoal = ttk.Combobox(root, width = 5)
GreenColGoal.place(x=430,y=375)
GreenColGoal['values'] = (0,1,2)

# blue goal

labelBlueGoal = Label(root, text="Blue -> ", font=('Times New Roman','18'), fg='blue')
labelBlueGoal.place(x=10,y=400)

labelBlueRowGoal = Label(root, text="row index:", font=('Times New Roman','18'), fg='blue')
labelBlueRowGoal.place(x=100,y=400)

labelBlueColGoal = Label(root, text="column index:", font=('Times New Roman','18'), fg='blue')
labelBlueColGoal.place(x=285,y=400)

BlueRowGoal = ttk.Combobox(root, width = 5)
BlueRowGoal.place(x=210,y=405)
BlueRowGoal['values'] = (0,1,2)

BlueColGoal = ttk.Combobox(root, width = 5)
BlueColGoal.place(x=430,y=405)
BlueColGoal['values'] = (0,1,2)

algorithm = Label(root, text="Algorithm: ", font=('Times New Roman','18'), fg='black')
algorithm.place(x=10,y=570)

algorithmCbx = ttk.Combobox(root, width = 25)
algorithmCbx.place(x=130,y=575)
algorithmCbx['values'] = ("A*", "Uniform Cost Search")

def return_algorithm():
    if str(algorithmCbx.get()) == "Uniform Cost Search":
        return 1
    elif str(algorithmCbx.get()) == "A*":
        return 2

tileOrder = Label(root, text="Order of tile moves: ", font=('Times New Roman','18'), fg='black')
tileOrder.place(x=10,y=630)

tileOrderFirst = Label(root, text="First: ", font=('Times New Roman','18'), fg='black')
tileOrderFirst.place(x=10,y=670)

tileOrderSecond = Label(root, text="Second: ", font=('Times New Roman','18'), fg='black')
tileOrderSecond.place(x=10,y=710)

tileOrderThird = Label(root, text="Third: ", font=('Times New Roman','18'), fg='black')
tileOrderThird.place(x=10,y=750)

firstTileOrderValue = Text(root, height = 1, width = 10)
firstTileOrderValue.place(x=100,y=675)

secondTileOrderValue = Text(root, height = 1, width = 10)
secondTileOrderValue.place(x=100,y=715)

thirdTileOrderValue = Text(root, height = 1, width = 10)
thirdTileOrderValue.place(x=100,y=755)

def print_board(board):
    print("-------------")
    for row in board:
        print("| ", end="")
        for tile in row:
            print(tile + " | ", end="")
        print("\n-------------")

buttonsInitial = [[], [], []]
buttonsGoal = [[], [], []]
game_board = [["N", "N", "N"], ["N", "N", "N"], ["N", "N", "N"]]
game_board_goal = [["N", "N", "N"], ["N", "N", "N"], ["N", "N", "N"]]
states = []
goal_states = []

print("---ARRAY START---")
print_board(game_board)

def create_puzzle_initial():

    redx = int(float(RedRow.get()))
    redy = int(float(RedCol.get()))
    greenx = int(float(GreenRow.get()))
    greeny = int(float(GreenCol.get()))
    bluex = int(float(BlueRow.get()))
    bluey = int(float(BlueCol.get()))

    for i in range(3):
        for j in range(3):
            buttonsInitial[i].append(Button(frameInitial, height=2, width=5, bd=6))
            if i==redx and j==redy:
                buttonsInitial[i][j].configure(bg = 'red')
                game_board[i][j] = "R"
                states.append(State("R", [i,j]))
            elif i==greenx and j==greeny:
                buttonsInitial[i][j].configure(bg = 'green')
                game_board[i][j] = "G"
                states.append(State("G", [i,j]))
            elif i==bluex and j==bluey:
                buttonsInitial[i][j].configure(bg = 'blue')
                game_board[i][j] = "B"
                states.append(State("R", [i,j]))
            buttonsInitial[i][j].grid(row=i, column=j)
    print("---ARRAY INITIALLY---")
    print_board(game_board)

def create_puzzle_goal():

    redx = int(float(RedRowGoal.get()))
    redy = int(float(RedColGoal.get()))
    greenx = int(float(GreenRowGoal.get()))
    greeny = int(float(GreenColGoal.get()))
    bluex = int(float(BlueRowGoal.get()))
    bluey = int(float(BlueColGoal.get()))

    for i in range(3):
        for j in range(3):
            buttonsGoal[i].append(Button(frameGoal, height=2, width=5, bd=6))
            if i==redx and j==redy:
                buttonsGoal[i][j].configure(bg = 'red')
                game_board_goal[i][j] = "R"
                goal_states.append(State("R", [i,j]))
            elif i==greenx and j==greeny:
                buttonsGoal[i][j].configure(bg = 'green')
                game_board_goal[i][j] = "G"
                goal_states.append(State("G", [i,j]))
            elif i==bluex and j==bluey:
                buttonsGoal[i][j].configure(bg = 'blue')
                game_board_goal[i][j] = "B"
                goal_states.append(State("B", [i,j]))
            buttonsGoal[i][j].grid(row=i, column=j)
    
    print("---ARRAY GOAL---")
    print_board(game_board_goal)

        
def create_puzzle(redx, redy, greenx, greeny, bluex, bluey):
    buttons = [[], [], []]
    for i in range(3):
        for j in range(3):
            buttons[i].append(Button(height=2, width=5, bd=6))
            if i==redx and j==redy:
                buttons[i][j].configure(bg = 'red')
            elif i==greenx and j==greeny:
                buttons[i][j].configure(bg = 'green')
            elif i==bluex and j==bluey:
                buttons[i][j].configure(bg = 'blue')
            buttons[i][j].grid(row=i, column=j)

def getInputs():
    print("Please enter the order of tiles that will do an action. Enter R for red, G for green and B for blue")
    order = []
    while true==1:
        order.append(str(firstTileOrderValue.get("1.0",END)).strip())
        if is_initial_valid(order[0]) == 1:
            order.remove(str(firstTileOrderValue.get("1.0",END)).strip())
            messagebox.showinfo("Information","Informative message")
        else:
            break
    
    while true==1:
        order.append(str(secondTileOrderValue.get("1.0",END)).strip())
        if is_initial_valid(order[1]) == 1:
            if order[0] == order[1]:
                order.remove(str(firstTileOrderValue.get("1.0",END)).strip())
                messagebox.showinfo("Information","Please enter a valid initial")
            else:
                break
        else:
            messagebox.showinfo("Information","Please enter a valid initial")
    while true == 1:
        order.append(str(thirdTileOrderValue.get("1.0",END)).strip())
        if is_initial_valid(order[2]) == 1:
            if order[0] == order[2] or order[1] == order[2]:
                order.remove(str(firstTileOrderValue.get("1.0",END)).strip())
                messagebox.showinfo("Information","Please enter a valid initial")
            else:
                break
        else:
            messagebox.showinfo("Information","Please enter a valid initial")

    print(states)
    return order

def start_calculation():
    true = 1
    while true == 1:
    # print("Please choose a searching strategy:")
    # print("1) Uniform cost search")
    # print("2) A* search")

        searchingAlgorithm = return_algorithm()

        if searchingAlgorithm == 1:
            #states = ["N", "N", "N"]
            order = []
            order = getInputs()

            while (1):
               decision_point1 = move_tile(game_board, order[0], states, goal_states)
               decision_point2 = move_tile(game_board, order[1], states, goal_states)
               decision_point3 = move_tile(game_board, order[2], states, goal_states)

               if decision_point1 == 0 and decision_point2 == 0 and decision_point3 == 0:
                   break
            break
            # TODO: UNIFORM COST
        elif searchingAlgorithm == 2:

            print("Please enter the order of tiles")
            order = []
            order = getInputs()
            # first = str(firstTileOrderValue.get("1.0",END)).strip()
            # second = str(secondTileOrderValue.get("1.0",END)).strip()
            # third = str(thirdTileOrderValue.get("1.0",END)).strip()

            # print(game_board)
            # print(states)
            # print("R: " + str(states[0].place[0]) + " " + str(states[0].place[1]) + " G: " + str(states[1].place[0]) + " " + str(states[1].place[1]) + " B: " + str(states[2].place[0]) + " " + str(states[2].place[1]) + " ")
            # print("R: " + str(goal_states[0].place[0]) + " " + str(goal_states[0].place[1]) + " G: " + str(goal_states[1].place[0]) + " " + str(goal_states[1].place[1]) + " B: " + str(goal_states[2].place[0]) + " " + str(goal_states[2].place[1]) + " ")
            # print(goal_states)
            # print("FIRST: " + first + " SECOND: " + second + " THIRD: " + third)

            while (1):
                decision_point1 = move_tile(game_board, order[0], states, goal_states)
                decision_point2 = move_tile(game_board, order[1], states, goal_states)
                decision_point3 = move_tile(game_board, order[2], states, goal_states)

                if decision_point1 == 0 and decision_point2 == 0 and decision_point3 == 0:
                    break
            break

Button(root, text="Create Initial Board", height=3, width=15, bd=6, command=create_puzzle_initial).place(x=10,y=175)
Button(root, text="Create Goal Board", height=3, width=15, bd=6, command=create_puzzle_goal).place(x=10,y=465)
Button(root, text="START", height=3, width=15, bd=6, command=start_calculation).place(x=10,y=800)

root.mainloop()