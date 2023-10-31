def dfs(fragments, visited, current_genome, min_genome):
    # Base case: if all fragments are visited, check if the current genome is shorter than the minimum genome
    if all(visited):
        if len(current_genome) < len(min_genome):
            return current_genome
        return min_genome

    # Iterate over each fragment
    for i in range(len(fragments)):
        # If the fragment is not visited
        if not visited[i]:
            # Mark the fragment as visited
            visited[i] = True

            # Check if the current genome already contains the fragment
            if fragments[i] in current_genome:
                # If it does, continue to the next fragment
                min_genome = dfs(fragments, visited, current_genome, min_genome)

            else:
                # If it doesn't, append the fragment to the current genome
                min_genome = dfs(fragments, visited, current_genome + fragments[i], min_genome)

            # Mark the fragment as unvisited for the next iteration
            visited[i] = False

    return min_genome


# Read the number of genome fragments
n = int(input())

# Read the fragments
fragments = []
for _ in range(n):
    fragment = input().strip()
    fragments.append(fragment)

# Initialize visited array to keep track of visited fragments
visited = [False] * n

# Initialize the current and minimum genome
current_genome = ""
min_genome = "z" * (26 * n)  # Initialize with a large string

# Restore the dinosaur genome using DFS
min_genome = dfs(fragments, visited, current_genome, min_genome)

# Print the result
print(min_genome)