# Write a function that takes a 2D binary array and returns the number of 1 islands.
# An island consists of 1s that are connected to the north, south, east or west.
#
# For example:

# Undirected graph

islands = [[0, 1, 0, 1, 0],
           [1, 1, 0, 1, 1],
           [0, 0, 1, 0, 0],
           [1, 0, 1, 0, 0],
           [1, 1, 0, 0, 0]]


# Visit each cell in the 2d array.
# When you come across a 1, traverse it and mark all connected nodes as visited
# then increment a counter

class Stack():
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None

    def size(self):
        return len(self.stack)


def get_island_neighbors(x, y, matrix):
    neighbors = []
    # Check if 1 to the north
    if y > 0 and matrix[y-1][x] == 1:
        neighbors.append((x, y-1))
    if y < len(matrix) - 1 and matrix[y+1][x] == 1:
        neighbors.append((x, y+1))
    if x < len(matrix) - 1 and matrix[y][x+1] == 1:
        neighbors.append((x+1, y))
    if x > 0 and matrix[y][x-1] == 1:
        neighbors.append((x-1, y))
    return neighbors


def dft_islands(start_x, start_y, matrix, visited):
    s = Stack()
    s.push((start_x, start_y))
    # While the stack is not empty...
    while s.size() > 0:
        # Pop the first vertex
        v = s.pop()
        x = v[0]
        y = v[1]
        # If that vertex has not been visited...
        if not visited[y][x]:
            # Markt is as visited...
            visited[y][x] = True
            # Then add all of its neighbors to the top of the stack
            for neighbor in get_island_neighbors(x, y, matrix):
                s.push(neighbor)
    return visited


def island_counter(matrix):
    visited = []
    matrix_height = len(matrix)
    matrix_width = len(matrix[0])
    for i in range(len(matrix)):
        visited.append([False] * matrix_width)
    counter = 0

    for x in range(matrix_width):
        for y in range(matrix_height):
            if not visited[y][x]:
                if matrix[y][x] == 1:
                    visited = dft_islands(x, y, matrix, visited)
                    counter += 1
    return counter


print(island_counter(islands))

big_islands = [[1, 0, 0, 1, 1, 0, 1, 1, 0, 1],
               [0, 0, 1, 1, 0, 1, 0, 0, 0, 0],
               [0, 1, 1, 1, 0, 0, 0, 1, 0, 1],
               [0, 0, 1, 0, 0, 1, 0, 0, 1, 1],
               [0, 0, 1, 1, 0, 1, 0, 1, 1, 0],
               [0, 1, 0, 1, 1, 1, 0, 1, 0, 0],
               [0, 0, 1, 0, 0, 1, 1, 0, 0, 0],
               [1, 0, 1, 1, 0, 0, 0, 1, 1, 0],
               [0, 1, 1, 0, 0, 0, 1, 1, 0, 0],
               [0, 0, 1, 1, 0, 1, 0, 0, 1, 0]]

print(island_counter(big_islands))
