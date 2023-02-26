from collections import deque

# QUESTION 1-B
def topological_sort(dag):
    sources = deque()
    ordering = []
    in_degree = {node: 0 for node in dag}

    # Count the indegree of each node
    for node in dag:
        for child in dag[node]:
            in_degree[child] += 1

    # Add nodes with indegree 0 to the sources list
    for node in in_degree:
        if in_degree[node] == 0:
            sources.append(node)

    # Repeat until the sources list is empty
    while sources:
        # Remove a node from the sources list and append it to the ordering
        node = sources.popleft()
        ordering.append(node)

        # Decrement the indegree of each of the node's children by 1
        for child in dag[node]:
            in_degree[child] -= 1

            # If a child's indegree becomes 0, add it to the sources list
            if in_degree[child] == 0:
                sources.append(child)

    # If the ordering list contains all nodes in the DAG, return the ordering
    if len(ordering) == len(dag):
        return ordering
    else:
        # Otherwise, the DAG contains a cycle and no topological ordering exists
        return None



dag = {
    1: [2, 3],
    2: [4, 5],
    3: [6],
    4: [],
    5: [6],
    6: []
}

ordering = topological_sort(dag)
print("1.b - topological sort of given dag:")
print(ordering)  

# END OF QUESTION 1-B

# QUESTION 2

def power(a, n):
    # Initialize the result to 1
    result = 1

    # While n is greater than 0
    while n > 0:
        # If n is odd, multiply the result by a
        if n % 2 == 1:
            result *= a

        # Divide n by 2
        n = n // 2

        # Multiply a by itself
        a *= a

    # Return the result
    return result

print("2 - power of a number:")
a = int(input("base: "))
n = int(input("exponential: "))
print(power(a,n))
# END OF QUESTION 2

# QUESTION 3
def solve_sudoku(map):
    # Initialize a list of empty cells
    empty_grids = [(i, j) for i in range(9) for j in range(9) if map[i][j] == 0]

    # If there are no empty cells, the puzzle is solved
    if not empty_grids:
        return True

    # Choose the next cell to fill
    cell = empty_grids[0]

    # Try all possible values for the chosen cell
    for value in range(1, 10):
        # If the value is valid for the cell, update the map and recurse
        if is_valid(map, cell, value):
            map[cell[0]][cell[1]] = value
            if solve_sudoku(map):
                return True

            # If the puzzle cannot be solved, restore the original value
            map[cell[0]][cell[1]] = 0

    # If no value works for the chosen cell, the puzzle is unsolvable
    return False

def is_valid(map, cell, value):
    # Check if the value is already present in the row, column, or box
    return (value not in map[cell[0]] and
            value not in [map[i][cell[1]] for i in range(9)] and
            value not in get_box(map, cell))

def get_box(map, cell):
    # Calculate the indices of the top-left cell of the box
    row = (cell[0] // 3) * 3
    col = (cell[1] // 3) * 3

    # Return the values of the cells in the box
    return [map[row+i][col+j] for i in range(3) for j in range(3)]

def test_solve_sudoku():
    # Create a sample Sudoku board
    board = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]

    # Solve the Sudoku puzzle
    assert solve_sudoku(board)

print(test_solve_sudoku())

# END OF QUESTION 3
