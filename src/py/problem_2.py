from collections import deque

def bfs(row, col, j):
    queue = deque([(row, col, j)])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    while queue:
        curr_row, curr_col, curr_j = queue.popleft()

        if curr_row < 0 or curr_row >= n or curr_col < 0 or curr_col >= m:
            continue

        if maze[curr_row][curr_col] == 'x':
            return True

        if maze[curr_row][curr_col] == '#':
            continue

        if maze[curr_row][curr_col] == 's':
            if curr_j == 0:
                continue
            curr_j -= 1

        if visited[curr_row][curr_col]:
            continue

        visited[curr_row][curr_col] = True

        for direction in directions:
            new_row = curr_row + direction[0]
            new_col = curr_col + direction[1]
            queue.append((new_row, new_col, curr_j))

    return False

# Read input values
n, m, j = map(int, input().split())

# Create a 2D grid to represent the maze
maze = []
visited = [[False for _ in range(m)] for _ in range(n)]

# Read the maze configuration
for _ in range(n):
    row = input().strip()
    maze.append(row)

# Find the starting position (entrance)
for i in range(n):
    for j in range(m):
        if maze[i][j] == '@':
            start_row, start_col = i, j
            break

# Call the BFS algorithm from the starting position
if bfs(start_row, start_col, j):
    print("SUCCESS")
else:
    print("IMPOSSIBLE")