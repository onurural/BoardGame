import tkinter as tk
from tkinter import *
from tkinter import ttk


class Node():
    """A node class for A* Pathfinding"""

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position


root = tk.Tk()
root.title("Board Game")
root.geometry("900x600")

frameOperation = tk.Frame(root)
frameOperation.pack(padx=400, pady=200)

# class Result:
#     def __init__(self):
#         self.seconds = 0
#         self.frameOperation = tk.Frame(root)
#         self.frameOperation.pack(padx=400, pady=200)
#         self.frameOperation.after(1000, self.refresh_label)

#     def refresh_frame(self, path, color):
#     # increment the time
#         self.seconds += 1
#         # display new puzzle
#         create_puzzle(path, color)
#         # request tkinter to call self.refresh after 1s (the delay is given in ms)
#         self.frameOperation.after(1000, self.refresh_frame)

x = 0

current_path = []
current_color = ""


# def increase_x():
#     global x
#     x=x+1

def create_puzzle_beyza(path, color):
    # obj = Result()
    # for x in range(len(path)):

    print(len(path))
    print(color)
    print("Expansion order: ")
    for index in range(len(path)):
        print(path[index][0], path[index][1], end="")
        if index != len(path) - 1:
            print(" => ", end="")
        else:
            print("\n")

    # global x

    # pathX = path[x][0]
    # pathY = path[x][1]

    buttons = [[], [], []]
    for i in range(3):
        for j in range(3):
            buttons[i].append(Button(frameOperation, height=2, width=5, bd=6))
            # print("***********************" + str(path[i][0]) + "*******************" + str(path[i][1]))
            if color == "R" and i == path[i][0] and j == path[i][1]:
                buttons[i][j].configure(bg='red')
            elif color == "G" and i == path[i][0] and j == path[i][1]:
                buttons[i][j].configure(bg='green')
            elif color == "B" and i == path[i][0] and j == path[i][1]:
                buttons[i][j].configure(bg='blue')
            buttons[i][j].grid(row=i, column=j)
            # if color == "R" and i == pathX and j == pathY:
            #     buttons[i][j].configure(bg = 'red')
            # elif color == "G" and i == pathX and j == pathY:
            #     buttons[i][j].configure(bg = 'green')
            # elif color == "B" and i == pathX and j == pathY:
            #     buttons[i][j].configure(bg = 'blue')
            # buttons[i][j].grid(row=i, column=j)
            # obj.refresh_frame(obj, path, color)
        # increase_x()

    print("BUTTON LENGTH --------------------------- " + str(len(buttons)))

    for i in range(len(buttons)):
        print(buttons[i])


def create_puzzle(board):
    buttons = [[], [], []]

    for i in range(3):
        for j in range(3):
            buttons[i].append(Button(frameOperation, height=2, width=5, bd=6))
            if board[i][j] == "R":
                buttons[i][j].configure(bg='red')
            if board[i][j] == "G":
                buttons[i][j].configure(bg='green')
            if board[i][j] == "B":
                buttons[i][j].configure(bg='blue')
            buttons[i][j].grid(row=i, column=j)

    print("BUTTON LENGTH --------------------------- " + str(len(buttons)))

    for i in range(len(buttons)):
        print(buttons[i])


#Button(root, text="NEXT", height=3, width=15, bd=6, command=create_puzzle(current_path, current_color)).place(x=10,y=800)



def astar(board, start, end, color, correctPlace):
    global current_color
    current_color = color

    first_entered = 1
    print("\n\nA star algorithm started!")
    # Create start and end node
    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0

    print("Start Node: " + str(start_node.position))

    end_node = Node(None, end)
    end_node.g = end_node.h = end_node.f = 0

    print("End Node: " + str(end_node.position))

    print("\n")

    open_list = []
    closed_list = []

    # Add the start node
    open_list.append(start_node)
    expansion_order = []

    heuristic = 0

    # Loop until you find the end
    while len(open_list) > 0:
        # Get the current node
        current_node = open_list[0]
        current_index = 0

        for index, item in enumerate(open_list):
            print(str(item.position) + " => " + str(item.f))
            if item.f < current_node.f:
                current_node = item
                current_index = index

        # Pop current off open list, add to closed list
        vertical = (end.__getitem__(0) - open_list[current_index].position[0])
        horizontal = (end.__getitem__(1) - open_list[current_index].position[1])

        # TODO: COULD THERE BE A BETTER CHANCE?
        print("Expanding node at position: " + str(open_list[current_index].position) + " => f = g + h = " +
              str(open_list[current_index].g) + " + " + str(
            open_list[current_index].h if first_entered != 1 else (3 - correctPlace)) + " = " + str(
            open_list[current_index].f if first_entered != 1 else (3 - correctPlace)) + ";\n" + str(abs(vertical)) + (
                  " tile" if vertical == 1 else " tiles") + " away " +
              " vertically and " + str(abs(horizontal)) + (
                  " tile" if horizontal == 1 else " tiles") + " away horizontally "
              + "from the goal state.\n")

        first_entered = 0
        expansion_order.append(open_list[current_index])
        open_list.pop(current_index)
        closed_list.append(current_node)

        if len(expansion_order) >= 10:
            return 0

        # Found the goal
        if current_node == end_node:
            print("GOAL NODE FOUND!")

            print("Expansion order: ")
            for index in range(len(expansion_order)):
                print(expansion_order[index].position, end="")
                if index != len(expansion_order) - 1:
                    print(" => ", end="")
                else:
                    print("\n")
                # if index != (len(expansion_order) - 1):
                #   print(" => ", end="")

            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
                print("PATH!!!!!!!!!!!!!!!!!!!!!!!!!!! " + str(path[0][0]))

            global current_path
            current_path = path
            #create_puzzle(current_path, current_color)
            create_puzzle(board)

            return path[::-1]  # Return reversed path

        # Generate children
        children = []
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0)]:  # left - right - up - down

            # Get node position
            node_position = (current_node.position[0] + new_position[0],
                             current_node.position[1] + new_position[1])  # a possible node we can go

            # Make sure within range
            if node_position[0] > (len(board) - 1) or node_position[0] < 0 or node_position[1] > (
                    len(board[len(board) - 1]) - 1) or node_position[1] < 0:
                continue

            if board[node_position[0]][node_position[1]] != "N":
                continue

            # Create new node
            new_node = Node(current_node, node_position)

            # Append
            children.append(new_node)

        # Loop through children
        for child in children:

            # Child is on the closed list
            for closed_child in closed_list:
                if child == closed_child:
                    continue

            # Calculating the f, g, and h values
            if color == "R":
                child.g = current_node.g + 1  # for "R" cost is always 1

            if color == "G":
                if new_position[1] == -1 or new_position[1] == 1:  # left or right
                    child.g = current_node.g + 1  # for "G" left-right cost is 1
                if new_position[0] == -1 or new_position[0] == 1:  # up or down
                    child.g = current_node.g + 2  # for "G" up-down cost is 2

            if color == "B":
                if new_position[1] == -1 or new_position[1] == 1:  # left or right
                    child.g = current_node.g + 2  # for "B" left-right cost is 2
                if new_position[0] == -1 or new_position[0] == 1:  # up or down
                    child.g = current_node.g + 1  # for "B" up-down cost is 1

            # child.h = ((child.position[0] - end_node.position[0]) ** 2) + (
            #         (child.position[1] - end_node.position[1]) ** 2)

            if child.position[0] == end_node.position[0] and child.position[1] - end_node.position[1]:
                child.h = 3 - correctPlace - 1
            else:
                child.h = 3 - correctPlace
            child.f = child.g + child.h

            # Child is already in the open list
            for open_node in open_list:
                if child == open_node and child.g > open_node.g:
                    continue

            # Add the child to the open list
            if len(open_list) >= 25:
                print("FRINGE IS FULL! DELETING THE NODE WITH MOST COST! COST IS: ", end="")
                node_to_be_deleted = None
                highest_node_f = -1
                for i in range(len(open_list)):
                    if highest_node_f < open_list[i].f:
                        highest_node_f = open_list[i].f
                        node_to_be_deleted = open_list[i]

                print(str(highest_node_f))
                open_list.remove(node_to_be_deleted)

            open_list.append(child)
