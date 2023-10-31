from collections import defaultdict

def dfs(v, parent, distances, graph):
    for u in graph[v]:
        if u != parent:
            distances[u] = distances[v] + 1
            dfs(u, v, distances, graph)

# Read the number of vertices and the starting vertex
n, x = map(int, input().split())

# Create an adjacency list representation of the tree
graph = defaultdict(list)
for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# Initialize distances array
distances = [0] * (n+1)

# Calculate distances from vertex 1 to all other vertices using DFS
dfs(1, 0, distances, graph)

# Calculate the number of moves Alice and Bob will make
alice_moves = distances[x]
bob_moves = max(distances[i] for i in range(1, n+1) if i != x)

# Print the result
total_moves = 2 * bob_moves
print(total_moves)