from collections import deque

def find_shortest_path(n, m, k, roads, forbidden):
    # Create an adjacency list to represent the graph
    graph = [[] for _ in range(n + 1)]
    for x, y in roads:
        graph[x].append(y)
        graph[y].append(x)

    # Create a set to store the forbidden triplets
    forbidden_set = set()
    for triplet in forbidden:
        forbidden_set.add((triplet[0], triplet[1], triplet[2]))
        forbidden_set.add((triplet[1], triplet[0], triplet[2]))

    # Create a queue for BFS traversal
    queue = deque([(1, [1])])

    # Create a visited array to keep track of visited cities
    visited = [False] * (n + 1)
    visited[1] = True

    while queue:
        city, path = queue.popleft()

        if city == n:
            return len(path) - 1, path

        for neighbor in graph[city]:
            if not visited[neighbor] and (city, city, neighbor) not in forbidden_set:
                visited[neighbor] = True
                queue.append((neighbor, path + [neighbor]))

    return -1, []

# Read input
n, m, k = map(int, input().split())
roads = [tuple(map(int, input().split())) for _ in range(m)]
forbidden = [tuple(map(int, input().split())) for _ in range(k)]

# Find the shortest path
d, path = find_shortest_path(n, m, k, roads, forbidden)

# Print the result
if d == -1:
    print(-1)
else:
    print(d)
    print(*path)
