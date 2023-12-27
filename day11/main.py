with open("day11/input.txt", mode="r") as input_stream:
    initial_galaxy_map = input_stream.read().splitlines()


def get_manhattan_distance(initial_point, final_point):
    x_dist = abs(initial_point[0] - final_point[0])
    y_dist = abs(initial_point[1] - final_point[1])
    return x_dist + y_dist


def get_all_distances(position_list):
    dist = 0
    for initial_pos in position_list:
        for final_pos in position_list:
            dist += get_manhattan_distance(initial_pos, final_pos)
    return dist


# Part 1
final_galaxy_map = []
for row in initial_galaxy_map:
    galaxy_row_list = [x for x in row]
    final_galaxy_map.append(galaxy_row_list)
    if "#" not in row:
        final_galaxy_map.append(galaxy_row_list)

i = 0
while i < len(final_galaxy_map[0]):
    if "#" not in [row[i] for row in final_galaxy_map]:
        [row.insert(i, ".") for row in final_galaxy_map]
        i += 1
    i += 1

position_list = []

for i, row in enumerate(final_galaxy_map):
    for j, char in enumerate(row):
        if char == "#":
            position_list.append((i, j))

print(f"Solution to Part 1: {get_all_distances(position_list)/2}")


# Part 2
scale_factor = 1000000 - 1
final_galaxy_map = []
rows_position_mapping = {}
columns_position_mapping = {}


row_position_tracker = 0
for i, row in enumerate(initial_galaxy_map):
    galaxy_row_list = [x for x in row]
    final_galaxy_map.append(galaxy_row_list)
    if "#" not in row:
        row_position_tracker += scale_factor
    rows_position_mapping[i] = i + row_position_tracker

i = 0
column_position_tracker = 0
while i < len(final_galaxy_map[0]):
    if "#" not in [row[i] for row in final_galaxy_map]:
        column_position_tracker += scale_factor

    columns_position_mapping[i] = i + column_position_tracker
    i += 1

position_list = []

for i, row in enumerate(final_galaxy_map):
    for j, char in enumerate(row):
        x = rows_position_mapping[i]
        y = columns_position_mapping[j]
        if char == "#":
            position_list.append((x, y))

print(f"Solution to Part 2: {get_all_distances(position_list)/2}")
