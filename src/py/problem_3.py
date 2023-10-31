from collections import deque

def transform_number(a, b):
    queue = deque([(a, [])])  # Initialize the queue with the starting number and an empty sequence of transformations
    while queue:
        current_number, transformations = queue.popleft()
        if current_number == b:
            return transformations  # If we reached the target number, return the sequence of transformations
        # Perform the two possible operations and add the new numbers to the queue
        next_number_1 = current_number * 2
        next_number_2 = current_number * 10 + 1
        if next_number_1 <= b:
            queue.append((next_number_1, transformations + [next_number_1]))
        if next_number_2 <= b:
            queue.append((next_number_2, transformations + [next_number_2]))
    return None  # If we couldn't reach the target number, return None

# Read the input numbers
a, b = map(int, input().split())

# Call the function to transform the number
transformations = transform_number(a, b)

if transformations is None:
    print("NO")
else:
    print("YES")
    print(len(transformations))
    print(a, end=" ")
    for transformation in transformations[:-1]:  # Exclude the last element to avoid duplicate occurrence of b
        print(transformation, end=" ")
    print(b)