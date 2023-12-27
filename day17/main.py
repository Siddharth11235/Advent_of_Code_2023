import heapq
from collections import deque

with open("day17/input.txt", mode="r") as input_stream:
    heat_map = input_stream.read().splitlines()


rows, cols = len(heat_map), len(heat_map[0])

start = (0, 0)
end = (rows - 1, cols - 1)


from collections import defaultdict
from queue import PriorityQueue


def dijkstra(grid, start, end, max_moves=3, min_moves=0):
    rows, cols = len(grid), len(grid[0])

    pq = [(0, [start], (0, 0), 0)]
    visited = defaultdict(bool)
    while pq:
        cost, path, direction, num_moves = heapq.heappop(pq)
        x, y = path[-1]
        # If we reach the end, we can return the cost path
        if (x, y) == end:
            return cost, path
        if visited[((x, y), direction, num_moves)] == True:
            continue

        visited[((x, y), direction, num_moves)] = True

        if num_moves < max_moves and direction != (
            0,
            0,
        ):
            nx, ny = (x + direction[0], y + direction[1])
            if 0 <= nx < rows and 0 <= ny < cols:
                heapq.heappush(
                    pq,
                    (
                        cost + int(grid[nx][ny]),
                        list(path) + [(nx, ny)],
                        direction,
                        num_moves + 1,
                    ),
                )

        if min_moves and num_moves < min_moves and direction != (0, 0):
            continue

        # Check all four directions (up, down, left, right)
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            if (dx, dy) != direction and (dx, dy) != (-direction[0], -direction[1]):
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols:
                    new_cost = cost + int(grid[nx][ny])

                    heapq.heappush(pq, (new_cost, path + [(nx, ny)], (dx, dy), 1))


def reconstruct_path(prev, node):
    path = []
    while node:
        path.append(node)
        node = prev[node]
    return path  # Reverse the path


cost, path = dijkstra(heat_map, start, end)
print(f"Solution to Part 1: {cost}")

cost, path = dijkstra(heat_map, start, end, max_moves=10, min_moves=4)
print(f"Solution to Part 2: {cost}")
