with open("day3/input.txt", mode="r") as input_stream:
    engineering_specs = input_stream.read().splitlines()

spec_sum = 0

RATIO_DICT = {}
gear_index_list = []


def check_for_symbol(pos_list, num, line_num):
    pos_rectangle = []
    if line_num > 0:
        for col in pos_list:
            pos_rectangle.append((line_num - 1, col))
        if pos_list[0] > 0:
            pos_rectangle.append((line_num - 1, pos_list[0] - 1))

        if pos_list[-1] < len(engineering_specs) - 1:
            pos_rectangle.append((line_num - 1, pos_list[-1] + 1))
    if line_num < len(engineering_specs) - 1:
        for col in pos_list:
            pos_rectangle.append((line_num + 1, col))
        if pos_list[0] > 0:
            pos_rectangle.append((line_num + 1, pos_list[0] - 1))

        if pos_list[-1] < len(engineering_specs) - 1:
            pos_rectangle.append((line_num + 1, pos_list[-1] + 1))

    if pos_list[0] > 0:
        pos_rectangle.append((line_num, pos_list[0] - 1))
    if pos_list[-1] < len(engineering_specs[line_num]) - 1:
        pos_rectangle.append((line_num, pos_list[-1] + 1))

    for position in pos_rectangle:
        if engineering_specs[position[0]][position[1]] == "*":
            if str((position[0], position[1])) not in RATIO_DICT.keys():
                RATIO_DICT[str((position[0], position[1]))] = {}
                RATIO_DICT[str((position[0], position[1]))]["val"] = num
                RATIO_DICT[str((position[0], position[1]))]["valid"] = False

            else:
                RATIO_DICT[str((position[0], position[1]))]["val"] = (
                    RATIO_DICT[str((position[0], position[1]))]["val"] * num
                )
                RATIO_DICT[str((position[0], position[1]))]["valid"] = True

    for position in pos_rectangle:
        if (
            not engineering_specs[position[0]][position[1]].isdigit()
            and engineering_specs[position[0]][position[1]] != "."
        ):
            return True

    return False


def get_line_sum(spec_line, line_num):
    digit_tracker = ""
    line_sum = 0
    i = 0

    pos = []
    while i < len(spec_line):
        while spec_line[i].isdigit() == True and i < len(spec_line):
            digit_tracker = digit_tracker + str(spec_line[i])
            pos.append(i)
            if i == len(spec_line) - 1:
                break
            i += 1

        if len(pos) > 0:
            if check_for_symbol(pos, int(digit_tracker), line_num) == True:
                line_sum += int(digit_tracker)
            digit_tracker = ""
            pos = []
        i += 1
    return line_sum


total_sum = 0
ratio_sum = 0
for line_num, spec_line in enumerate(engineering_specs):
    line_sum = get_line_sum(spec_line, line_num)
    total_sum += line_sum

for _, val in RATIO_DICT.items():
    if val["valid"] == True:
        ratio_sum += val["val"]
print(f"Solution to Part 1: {total_sum}")
print(f"Solution to Part 2: {ratio_sum}")
