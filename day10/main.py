import numpy as np

with open("day10/input.txt", mode="r") as input_stream:
    pipe_map = input_stream.read().splitlines()


# Part 1
def traverse_single_step(prev_position, current_position, current_char):
    if current_char == "|":
        if (
            prev_position[0] > current_position[0]
            and prev_position[1] == current_position[1]
        ):
            return (current_position[0] - 1, current_position[1])
        elif (
            prev_position[0] < current_position[0]
            and prev_position[1] == current_position[1]
        ):
            return (current_position[0] + 1, current_position[1])
        else:
            return (-1, -1)
    elif current_char == "-":
        if (
            prev_position[0] == current_position[0]
            and prev_position[1] > current_position[1]
        ):
            return (current_position[0], current_position[1] - 1)
        elif (
            prev_position[0] == current_position[0]
            and prev_position[1] < current_position[1]
        ):
            return (current_position[0], current_position[1] + 1)
        else:
            return (-1, -1)
    elif current_char == "L":
        if (
            prev_position[0] < current_position[0]
            and prev_position[1] == current_position[1]
        ):
            return (current_position[0], current_position[1] + 1)
        elif (
            prev_position[0] == current_position[0]
            and prev_position[1] > current_position[1]
        ):
            return (current_position[0] - 1, current_position[1])
        else:
            return (-1, -1)
    elif current_char == "J":
        if (
            prev_position[0] < current_position[0]
            and prev_position[1] == current_position[1]
        ):
            return (current_position[0], current_position[1] - 1)
        elif (
            prev_position[0] == current_position[0]
            and prev_position[1] < current_position[1]
        ):
            return (current_position[0] - 1, current_position[1])
        else:
            return (-1, -1)
    elif current_char == "7":
        if (
            prev_position[0] > current_position[0]
            and prev_position[1] == current_position[1]
        ):
            return (current_position[0], current_position[1] - 1)
        elif (
            prev_position[0] == current_position[0]
            and prev_position[1] < current_position[1]
        ):
            return (current_position[0] + 1, current_position[1])
        else:
            return (-1, -1)
    elif current_char == "F":
        if (
            prev_position[0] > current_position[0]
            and prev_position[1] == current_position[1]
        ):
            return (current_position[0], current_position[1] + 1)
        elif (
            prev_position[0] == current_position[0]
            and prev_position[1] > current_position[1]
        ):
            return (current_position[0] + 1, current_position[1])
        else:
            return (-1, -1)
    elif current_char == ".":
        return (-1, -1)


def get_potential_exploration_paths(starting_pos, pipe_list):
    potential_next_positions = []
    if starting_pos[1] > 0:
        if pipe_list[starting_pos[0]][starting_pos[1] - 1] in ["-", "L", "F"]:
            potential_next_positions.append((starting_pos[0], starting_pos[1] - 1))
    if starting_pos[1] + 1 < len(pipe_list[0]):
        if pipe_list[starting_pos[0]][starting_pos[1] + 1] in ["-", "7", "J"]:
            potential_next_positions.append((starting_pos[0], starting_pos[1] + 1))
    if starting_pos[0] + 1 < len(pipe_list):
        if pipe_list[starting_pos[0] + 1][starting_pos[1]] in ["|", "7", "F"]:
            potential_next_positions.append((starting_pos[0] + 1, starting_pos[1]))
    if starting_pos[0] > 0:
        if pipe_list[starting_pos[0] - 1][starting_pos[1]] in ["|", "L", "J"]:
            potential_next_positions.append((starting_pos[0] - 1, starting_pos[1]))

    return potential_next_positions


pipe_list = []

for i, line in enumerate(pipe_map):
    pipe_line = [x for x in line]
    if "S" in pipe_line:
        starting_pos = (i, pipe_line.index("S"))
    pipe_list.append(pipe_line)

current_char = None
current_pos = starting_pos
potential_next_positions = get_potential_exploration_paths(starting_pos, pipe_list)

next_pos = potential_next_positions[0]
current_pos = starting_pos
loop_of_positions = []
while current_char != "S":
    loop_of_positions.append(current_pos)
    prev_pos = current_pos
    current_pos = next_pos
    current_char = pipe_list[current_pos[0]][current_pos[1]]
    next_pos = traverse_single_step(prev_pos, current_pos, current_char)

if len(loop_of_positions) % 2 == 0:
    max_distance = len(loop_of_positions) / 2
else:
    max_distance = ceil(len(loop_of_positions) / 2)

print(f"Solution to Part 1: {max_distance}")


# Part 2
def shoelace_formula(loop_of_positions):
    # Gets area of a loop
    x = np.asarray([pos[0] for pos in loop_of_positions])

    y = np.asarray([pos[1] for pos in loop_of_positions])
    result = 0.5 * np.array(np.dot(x, np.roll(y, 1)) - np.dot(y, np.roll(x, 1)))
    return abs(result)


def picks_formula(total_area, max_distance):
    # Gets number of integer points inside an
    # enclosed space
    return total_area + 1 - max_distance


total_area = shoelace_formula(loop_of_positions)
print(f"Solution to Part 2: {picks_formula(total_area, max_distance)}")
