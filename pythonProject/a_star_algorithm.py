def print_board(board):
    print("-------------")
    for row in board:
        print("| ", end="")
        for tile in row:
            print(tile + " | ", end="")
        print("\n-------------")


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


def astar(maze, start, end):
    """Returns a list of tuples as a path from the given start to the given end in the given maze"""

    print("\n\nA star algorithm started!")
    # Create start and end node
    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0

    print("Start Node: " + str(start_node.position))

    end_node = Node(None, end)
    end_node.g = end_node.h = end_node.f = 0

    print("End Node: " + str(end_node.position))

    print("\n")

    # Initialize both open and closed list
    open_list = []
    closed_list = []

    # Add the start node
    open_list.append(start_node)
    expansion_order = []

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
        # print("LENGTH open: " + str(len(open_list)))
        print("Expanding node at position: " + str(open_list[current_index].position) + " => f = g + h = " +
              str(open_list[current_index].g) + " + " + str(open_list[current_index].h) + " = " + str(
            open_list[current_index].f) + "\n")

        expansion_order.append(open_list[current_index])
        open_list.pop(current_index)
        closed_list.append(current_node)

        # Found the goal
        if current_node == end_node:
            print("GOAL NODE FOUND!")

            print("Expansion order: ")
            for index in range(len(expansion_order)):
                print(expansion_order[index].position, end="")
                if index != len(expansion_order) - 1:
                    print(" => ", end="")
                # if index != (len(expansion_order) - 1):
                #   print(" => ", end="")

            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1]  # Return reversed path

        # Generate children
        children = []
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0)]:  # Adjacent squares

            # Get node position
            node_position = (current_node.position[0] + new_position[0],
                             current_node.position[1] + new_position[1])  # a possible node we can go

            # Make sure within range
            if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (
                    len(maze[len(maze) - 1]) - 1) or node_position[1] < 0:
                continue

            # Make sure walkable terrain
            if maze[node_position[0]][node_position[1]] != "N":
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
            child.g = current_node.g + 1  # for "R" cost is always 1
            child.h = ((child.position[0] - end_node.position[0]) ** 2) + (
                    (child.position[1] - end_node.position[1]) ** 2)
            child.f = child.g + child.h

            # Child is already in the open list
            for open_node in open_list:
                if child == open_node and child.g > open_node.g:
                    continue

            # Add the child to the open list
            if len(open_list) < 25:
                open_list.append(child)
            else:
                print("FRINGE IS FULL!")


# ghost game board is for calculating appropraite moves
game_board = [["N", "N", "N"], ["N", "N", "N"], ["N", "N", "N"]]

print("---ARRAY INITIALLY---")
print_board(game_board)

# starting position
game_board[0][0] = "R"

print("\n---ARRAY FILLED---")
print_board(game_board)

print("\n\nPATH: " + str(astar(game_board, (0, 0), (2, 2))))
