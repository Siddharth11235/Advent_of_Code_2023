from collections import deque

with open("day21/input.txt", mode="r") as input_stream:
    garden_map = input_stream.read().splitlines()

n_steps = 64

for start_x, row in enumerate(garden_map):
    if "S" in row:
        start_y = row.index("S")
        break


def traverse_single_step_multi_map(current_pos, current_map, garden_map):
    traversal_options = []
    x, y = current_pos
    map_x, map_y = current_map
    max_x, max_y = len(garden_map), len(garden_map[0])
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        nx, ny = x + dx, y + dy
        if 0 > nx:
            nx = max_x - 1
            if garden_map[nx][ny] != "#":
                traversal_options.append(((nx, ny), (map_x - 1, map_y)))
        elif 0 > ny:
            ny = max_y - 1
            if garden_map[nx][ny] != "#":
                traversal_options.append(((nx, ny), (map_x, map_y - 1)))
        elif nx >= max_x:
            nx = 0
            if garden_map[nx][ny] != "#":
                traversal_options.append(((nx, ny), (map_x + 1, map_y)))
        elif ny >= max_y:
            ny = 0
            if garden_map[nx][ny] != "#":
                traversal_options.append(((nx, ny), (map_x, map_y + 1)))
        else:
            if garden_map[nx][ny] != "#":
                traversal_options.append(((nx, ny), (map_x, map_y)))

    return traversal_options


def multi_map_bfs(garden_map, start, n_steps):
    current_steps = n_steps
    map_num = (0, 0)
    queue = deque([(start, map_num, current_steps)])

    visited = set()
    count = set()

    side_len = len(garden_map)
    maps_for_steps = (n_steps // side_len) + 1

    while queue:
        (x, y), (map_x, map_y), current_steps = queue.popleft()
        if current_steps >= 0:
            if current_steps % 2 == 0:
                count.add(((x, y), (map_x, map_y)))

            if current_steps > 0:
                current_steps -= 1
                neighbors = traverse_single_step_multi_map(
                    (x, y), (map_x, map_y), garden_map
                )
                for neighbor in neighbors:
                    new_pos, new_map = neighbor
                    if (new_pos, new_map) in visited:
                        continue

                    queue.append((new_pos, new_map, current_steps))
                    visited.add((new_pos, new_map))

    return len(count)


# Running the DFS algorithm with modified memoization
start = (start_x, start_y)
result = multi_map_bfs(garden_map, start, n_steps)
print(f"Solution to Part 1: {result}")
# Part 2:


# The quadratic idea taken from https://github.com/derailed-dash/Advent-of-Code/blob/master/src/AoC_2023/Dazbo's_Advent_of_Code_2023.ipynb
def reachable_plots(data, steps_available: int):
    grid = [[char for char in row] for row in data]
    grid_size = len(grid)

    assert grid_size == len(grid[0]), "The grid should be square"
    assert grid_size % 2 == 1, "The grid size is odd"

    (start,) = [
        (ri, ci)
        for ri, row in enumerate(grid)
        for ci, char in enumerate(row)
        if char == "S"
    ]

    assert start[0] == start[1] == grid_size // 2, "Start is in the middle"

    # For each location in the original grid (tile 0,0),
    # can we reach this same location in other tiles?
    answer = multi_map_bfs(grid, start, steps_available)

    return answer


step_counts = [65, 196, 327]


def solve_quadratic(data, plot_counts: list[int], steps: int):
    """Return the total number of reachable plots in a specified number of steps,
    by calculating the answer to the quadratic formula.
    Here we calculate the coefficients a, b and c by using three sample values,
    obtained from a smaller grid.

    Args:
        data (_type_): The original grid tile.
        plot_counts (list[int]): The plot counts determined for small step counts.
        steps (int): The number of steps we must take.
    """
    grid = [[char for char in row] for row in data]
    grid_size = len(grid)

    # determine coefficients
    c = plot_counts[0]
    b = (4 * plot_counts[1] - 3 * plot_counts[0] - plot_counts[2]) // 2
    a = plot_counts[1] - plot_counts[0] - b

    x = (steps - grid_size // 2) // grid_size  # number of whole tile lengths
    return a * x**2 + b * x + c


n_steps = 26501365

plot_counts = [
    (step_count, reachable_plots(garden_map, step_count)) for step_count in step_counts
]
ans = solve_quadratic(
    garden_map, plot_counts=[ct[1] for ct in plot_counts], steps=n_steps
)

print(f"Solution to Part 2: {ans}")
