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


def astar(board, start, end, color, correctPlace):
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

            """if color == "R":
                if board[node_position[0]][node_position[1]] != "N" and board[node_position[0]][
                    node_position[1]] != "B" and board[node_position[0]][node_position[1]] != "G":
                    continue

            if color == "G":
                if board[node_position[0]][node_position[1]] != "N" and board[node_position[0]][
                    node_position[1]] != "R" and board[node_position[0]][node_position[1]] != "B":
                    continue

            if color == "B":
                if board[node_position[0]][node_position[1]] != "N" and board[node_position[0]][
                    node_position[1]] != "R" and board[node_position[0]][node_position[1]] != "G":
                    continue"""

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
                print("FRINGE IS FULL! DELETING FIRST ONE!")
                open_list.pop()

            open_list.append(child)
