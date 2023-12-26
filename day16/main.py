from collections import deque

with open("day16/input.txt", mode="r") as input_stream:
    light_map = input_stream.read().splitlines()


def traverse_single_step(prev_position, current_position):
    current_char = light_map[current_position[0]][current_position[1]]
    if current_char == "|":
        if (
            prev_position[0] > current_position[0]
            and prev_position[1] == current_position[1]
        ):
            return [(current_position[0] - 1, current_position[1])]
        elif (
            prev_position[0] < current_position[0]
            and prev_position[1] == current_position[1]
        ):
            return [(current_position[0] + 1, current_position[1])]
        else:
            return [
                (current_position[0] + 1, current_position[1]),
                (current_position[0] - 1, current_position[1]),
            ]
    elif current_char == "-":
        if (
            prev_position[1] > current_position[1]
            and prev_position[0] == current_position[0]
        ):
            return [(current_position[0], current_position[1] - 1)]
        elif (
            prev_position[1] < current_position[1]
            and prev_position[0] == current_position[0]
        ):
            return [(current_position[0], current_position[1] + 1)]
        else:
            return [
                (current_position[0], current_position[1] + 1),
                (current_position[0], current_position[1] - 1),
            ]
    elif current_char == "/":
        if (
            prev_position[1] > current_position[1]
            and prev_position[0] == current_position[0]
        ):
            return [(current_position[0] + 1, current_position[1])]
        elif (
            prev_position[1] < current_position[1]
            and prev_position[0] == current_position[0]
        ):
            return [(current_position[0] - 1, current_position[1])]
        elif (
            prev_position[1] == current_position[1]
            and prev_position[0] > current_position[0]
        ):
            return [(current_position[0], current_position[1] + 1)]
        elif (
            prev_position[1] == current_position[1]
            and prev_position[0] < current_position[0]
        ):
            return [(current_position[0], current_position[1] - 1)]

    elif current_char == "\\":
        if (
            prev_position[1] > current_position[1]
            and prev_position[0] == current_position[0]
        ):
            return [(current_position[0] - 1, current_position[1])]
        elif (
            prev_position[1] < current_position[1]
            and prev_position[0] == current_position[0]
        ):
            return [(current_position[0] + 1, current_position[1])]
        elif (
            prev_position[1] == current_position[1]
            and prev_position[0] > current_position[0]
        ):
            return [(current_position[0], current_position[1] - 1)]
        elif (
            prev_position[1] == current_position[1]
            and prev_position[0] < current_position[0]
        ):
            return [(current_position[0], current_position[1] + 1)]
    elif current_char == ".":
        if prev_position[1] > current_position[1]:
            return [(current_position[0], current_position[1] - 1)]
        elif prev_position[1] < current_position[1]:
            return [(current_position[0], current_position[1] + 1)]
        elif prev_position[0] > current_position[0]:
            return [(current_position[0] - 1, current_position[1])]
        elif prev_position[0] < current_position[0]:
            return [(current_position[0] + 1, current_position[1])]
        elif (
            prev_position[0] == current_position[0]
            and prev_position[1] == current_position[1]
        ):
            return [(current_position[0], current_position[1] + 1)]


def bfs(grid, start):
    """
    Perform BFS on the light map, taking into account the previous position.
    """
    rows, cols = len(grid), len(grid[0])
    visited = set()
    queue = deque([start])  # (current_position, previous_position)

    while queue:
        (current_x, current_y), (prev_x, prev_y) = queue.popleft()

        # Mark the current node as visited
        visited.add(((current_x, current_y), (prev_x, prev_y)))
        next_steps = traverse_single_step((prev_x, prev_y), (current_x, current_y))
        # Iterate over all possible next steps
        for next_x, next_y in next_steps:
            if (
                0 <= next_x < rows
                and 0 <= next_y < cols
                and ((next_x, next_y), (current_x, current_y)) not in visited
            ):
                queue.append(((next_x, next_y), (current_x, current_y)))
    return visited


# Part 1
start = ((0, 0), (0, -1))  # Starting coordinates


# Perform BFS
visited = bfs(light_map, start)
visited_tile_set = set()
for cur, prev in list(visited):
    visited_tile_set.add(cur)
print(f"Solution to Part 1: {len(visited_tile_set)}")
# Part 2
rows, cols = len(light_map), len(light_map[0])
start_list = [start]
energised_list = []
for row in range(rows):
    start_list.append(((row, 0), (row, -1)))
    start_list.append(((row, cols - 1), (row, cols)))
for col in range(cols):
    start_list.append(((0, col), (-1, col)))
    start_list.append(((rows - 1, col), (rows, col)))

for start in start_list:
    # Perform BFS
    visited = bfs(light_map, start)
    visited_tile_set = set()
    for cur, prev in list(visited):
        visited_tile_set.add(cur)
    energised_list.append(len(visited_tile_set))

print(f"Solution to Part 2: {max(energised_list)}")
