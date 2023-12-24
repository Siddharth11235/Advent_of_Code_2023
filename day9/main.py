with open("day9/input.txt", mode="r") as input_stream:
    oasis_readings = input_stream.read().splitlines()


def get_next_value(line):
    line = [int(x) for x in line.split()]

    current_list = line
    next_value = current_list[-1]
    while list(set(current_list)) != [0]:
        diff_list = [
            current_list[i] - current_list[i - 1] for i in range(1, len(current_list))
        ]
        next_value += diff_list[-1]
        current_list = diff_list

    return next_value


total_sum = 0
for line in oasis_readings:
    total_sum += get_next_value(line)

print(f"Solution to Part 1: {total_sum}")

# Part 2


def get_prev_value(line):
    line = [int(x) for x in line.split()]

    current_list = line
    init_value_list = [current_list[0]]

    while list(set(current_list)) != [0]:
        diff_list = [
            current_list[i] - current_list[i - 1] for i in range(1, len(current_list))
        ]
        current_list = diff_list
        init_value_list.append(current_list[0])

    init_value = 0
    init_value_list.reverse()
    for i in init_value_list:
        init_value = i - init_value

    return init_value


total_sum = 0
for line in oasis_readings:
    total_sum += get_prev_value(line)

print(f"Solution to Part 2: {total_sum}")
