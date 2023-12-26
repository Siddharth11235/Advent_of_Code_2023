with open("day14/input.txt", mode="r") as input_stream:
    rock_info_map = input_stream.read().splitlines()


def update_rock_info_north(rock_info_map):
    updated_rock_info_map = rock_info_map.copy()
    num_changes = 100000
    while num_changes > 0:
        current_changes = 0
        rock_info_map = updated_rock_info_map.copy()
        for i in range(1, len(rock_info_map)):
            upper_rock_line = [x for x in rock_info_map[i - 1]]
            lower_rock_line = [x for x in rock_info_map[i]]
            for j in range(len(upper_rock_line)):
                if upper_rock_line[j] == "." and lower_rock_line[j] == "O":
                    current_changes += 1
                    updated_rock_info_map[i - 1] = (
                        updated_rock_info_map[i - 1][:j]
                        + "O"
                        + updated_rock_info_map[i - 1][j + 1 :]
                    )
                    updated_rock_info_map[i] = (
                        updated_rock_info_map[i][:j]
                        + "."
                        + updated_rock_info_map[i][j + 1 :]
                    )
        num_changes = current_changes

    return updated_rock_info_map


updated_rock_info = update_rock_info_north(rock_info_map)
total_soln = 0
for i, rock_row in enumerate(updated_rock_info):
    scale = len(updated_rock_info) - i
    movable_rocks = rock_row.count("O")
    total_soln += scale * movable_rocks

print(f"Solution to Part 1: {total_soln}")


# Part 2
def rotate_list(rock_info_map):
    rotated_rock_info_map = [""] * len(rock_info_map[0])

    # Iterate over each row and column to build the column strings
    potential_origins = []
    for row in rock_info_map:
        for i, char in enumerate(row):
            rotated_rock_info_map[i] += char

    return rotated_rock_info_map


def update_rock_info_south(rock_info_map):
    updated_rock_info_map = rock_info_map.copy()
    num_changes = 100000
    while num_changes > 0:
        current_changes = 0
        rock_info_map = updated_rock_info_map.copy()
        for i in range(1, len(rock_info_map)):
            upper_rock_line = [x for x in rock_info_map[i - 1]]
            lower_rock_line = [x for x in rock_info_map[i]]
            for j in range(len(upper_rock_line)):
                if upper_rock_line[j] == "O" and lower_rock_line[j] == ".":
                    current_changes += 1
                    updated_rock_info_map[i - 1] = (
                        updated_rock_info_map[i - 1][:j]
                        + "."
                        + updated_rock_info_map[i - 1][j + 1 :]
                    )
                    updated_rock_info_map[i] = (
                        updated_rock_info_map[i][:j]
                        + "O"
                        + updated_rock_info_map[i][j + 1 :]
                    )
        num_changes = current_changes

    return updated_rock_info_map


def update_rock_info_east(rock_info_map):
    rock_info_map = rotate_list(rock_info_map)
    updated_rock_info_map = rock_info_map.copy()
    num_changes = 100000
    while num_changes > 0:
        current_changes = 0
        rock_info_map = updated_rock_info_map.copy()
        for i in range(1, len(rock_info_map)):
            upper_rock_line = [x for x in rock_info_map[i - 1]]
            lower_rock_line = [x for x in rock_info_map[i]]
            for j in range(len(upper_rock_line)):
                if upper_rock_line[j] == "O" and lower_rock_line[j] == ".":
                    current_changes += 1
                    updated_rock_info_map[i - 1] = (
                        updated_rock_info_map[i - 1][:j]
                        + "."
                        + updated_rock_info_map[i - 1][j + 1 :]
                    )
                    updated_rock_info_map[i] = (
                        updated_rock_info_map[i][:j]
                        + "O"
                        + updated_rock_info_map[i][j + 1 :]
                    )
        num_changes = current_changes
    updated_rock_info_map = rotate_list(updated_rock_info_map)
    return updated_rock_info_map


def update_rock_info_west(rock_info_map):
    rock_info_map = rotate_list(rock_info_map)
    updated_rock_info_map = rock_info_map.copy()
    num_changes = 100000
    while num_changes > 0:
        current_changes = 0
        rock_info_map = updated_rock_info_map.copy()
        for i in range(1, len(rock_info_map)):
            upper_rock_line = [x for x in rock_info_map[i - 1]]
            lower_rock_line = [x for x in rock_info_map[i]]
            for j in range(len(upper_rock_line)):
                if upper_rock_line[j] == "." and lower_rock_line[j] == "O":
                    current_changes += 1
                    updated_rock_info_map[i - 1] = (
                        updated_rock_info_map[i - 1][:j]
                        + "O"
                        + updated_rock_info_map[i - 1][j + 1 :]
                    )
                    updated_rock_info_map[i] = (
                        updated_rock_info_map[i][:j]
                        + "."
                        + updated_rock_info_map[i][j + 1 :]
                    )
        num_changes = current_changes
    updated_rock_info_map = rotate_list(updated_rock_info_map)
    return updated_rock_info_map


def perform_single_cycle(rock_info_map):
    rock_info_map_north = update_rock_info_north(rock_info_map)
    rock_info_map_west = update_rock_info_west(rock_info_map_north)
    rock_info_map_south = update_rock_info_south(rock_info_map_west)
    rock_info_map_final = update_rock_info_east(rock_info_map_south)
    return rock_info_map_final


output_list = []
rock_state = rock_info_map
for index in range(1000):
    output = perform_single_cycle(rock_state)
    rock_state = output

target = 1000000000 % index


total_soln = 0
for i, rock_row in enumerate(output):
    scale = len(output) - i
    movable_rocks = rock_row.count("O")
    total_soln += scale * movable_rocks


print(f"Solution to Part 2: {total_soln}")
