with open("day13/input.txt", mode="r") as input_stream:
    combined_mirror_map = input_stream.read()

combined_mirror_map = combined_mirror_map.split("\n\n")


def common_soln(split_map):
    potential_origins = []
    if len(set(split_map)) < len(split_map):
        for i in range(1, len(split_map)):
            if split_map[i] == split_map[i - 1]:
                potential_origins.append(i)
    else:
        return []
    potential_outputs = []
    for origin in potential_origins:
        ind_above = origin - 1
        ind_below = origin
        completed_loop = True
        while ind_above >= 0 and ind_below < len(split_map):
            if split_map[ind_above] == split_map[ind_below]:
                ind_above -= 1
                ind_below += 1
            else:
                completed_loop = False
                break
        if completed_loop:
            potential_outputs.append(origin)

    return potential_outputs


# Part 1
def check_for_vertical_mirroring(split_map):
    output = common_soln(split_map)
    return output


def check_for_horizontal_mirroring(split_map):
    column_map = [""] * len(split_map[0])

    # Iterate over each row and column to build the column strings
    potential_origins = []
    for row in split_map:
        for i, char in enumerate(row):
            column_map[i] += char

    output = common_soln(column_map)
    return output


def get_mirror(split_map):
    row_val = check_for_vertical_mirroring(split_map)
    col_val = check_for_horizontal_mirroring(split_map)

    return row_val, col_val


total_sum = 0
solns = []
for mirror_map in combined_mirror_map:
    split_map = mirror_map.split("\n")
    row_val, col_val = get_mirror(split_map)
    if row_val:
        total_sum += row_val[0] * 100
        solns.append(("Row", row_val))
    else:
        total_sum += col_val[0]
        solns.append(("Column", col_val))
print(f"Solution to Part 1: {total_sum}")


# Part 2


def check_for_smudges(mirror_map):
    split_map = mirror_map.split("\n")
    orig_row, orig_col = get_mirror(split_map)
    for row in range(len(split_map)):
        for col in range(len(split_map[0])):
            split_map_copy = split_map.copy()
            line = split_map_copy[row]
            c = line[col]
            if c == ".":
                line = line[:col] + "#" + line[col + 1 :]
            else:
                line = line[:col] + "." + line[col + 1 :]
            split_map_copy[row] = line
            h_answers = check_for_vertical_mirroring(split_map_copy)
            v_answers = check_for_horizontal_mirroring(split_map_copy)

            if orig_row:
                h_answers = [
                    answer
                    for answer in h_answers
                    if answer != orig_row[0] and answer != 0
                ]
            else:
                v_answers = [
                    answer
                    for answer in v_answers
                    if answer != orig_col[0] and answer != 0
                ]
            if h_answers in [[], [0]] and v_answers in [[], [0]]:
                continue
            if h_answers:
                return "Row", h_answers[0]
            else:
                return "Column", v_answers[0]


total_sum = 0
for i, mirror_map in enumerate(combined_mirror_map):
    out = check_for_smudges(mirror_map)
    if out is not None:
        if out[0] == "Row":
            total_sum += out[1] * 100
        else:
            total_sum += out[1]

print(f"Solution to Part 2: {total_sum}")
