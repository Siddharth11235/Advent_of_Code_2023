with open("day15/input.txt", mode="r") as input_stream:
    instruction_string = input_stream.read()

instruction_list = instruction_string.split(",")


def get_hash_code(instruction):
    hash_code = 0
    for character in instruction:
        ascii_code = ord(character)
        hash_code += ascii_code
        hash_code = (hash_code * 17) % 256
    return hash_code


# Part 1
total_soln = 0
for instruction in instruction_list:
    out = get_hash_code(instruction)
    total_soln += out
print(f"Solution to Part 1: {total_soln}")

# Part 2
boxes = {i: {} for i in range(256)}
for instruction in instruction_list:
    lens_label = instruction[:-2]

    operation = instruction[-2]
    if instruction[-2] == "=":
        lens_label = instruction[:-2]
        lens_box = get_hash_code(lens_label)
        lens_power = instruction[-1]
        boxes[lens_box][lens_label] = int(lens_power)
    else:
        lens_label = instruction[:-1]
        lens_box = get_hash_code(lens_label)
        if lens_label in boxes[lens_box].keys():
            del boxes[lens_box][lens_label]
total_soln = 0

for box_num, lenses in boxes.items():
    for i, lens_power in enumerate(lenses.values()):
        total_soln += (box_num + 1) * (i + 1) * lens_power

print(f"Solution to Part 2: {total_soln}")
