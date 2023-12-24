from math import gcd


with open("day8/input.txt", mode="r") as input_stream:
    path_to_follow = input_stream.read().splitlines()

directions = path_to_follow[0]
path_nodes = path_to_follow[2:]
direction_to_list_mapping = {"L": 0, "R": 1}


path_map = {}
for path_node in path_nodes:
    path_key, path_val = path_node.split("=")
    path_key = path_key.replace(" ", "")
    path_val = path_val.replace("(", "")
    path_val = path_val.replace(")", "")
    path_val = path_val.replace(",", "")
    path_map[path_key] = path_val.split()
# Part 1
output = "AAA"

i = 0
while output != "ZZZ":
    index = i % len(directions)
    position = direction_to_list_mapping[directions[index]]
    output = path_map[output][position]
    i += 1
print(f"Solution to Part 1: {i}")


# Part 2
def calculate_lcm(list_of_ints):
    lcm = 1

    for i in list_of_ints:
        lcm = lcm * i // gcd(lcm, i)
    return lcm


starting_points = []


for path_node in path_nodes:
    path_key, path_val = path_node.split("=")
    path_key = path_key.replace(" ", "")
    if path_key[-1] == "A":
        starting_points.append(path_key)


def passing_test(test_points):
    print(test_points)

    for test_point in test_points:
        if test_point[-1] != "Z":
            return False
    return True


lowest_path_list = []
for starting_point in starting_points:
    i = 0
    while starting_point[-1] != "Z":
        index = i % len(directions)
        position = direction_to_list_mapping[directions[index]]
        starting_point = path_map[starting_point][position]
        i += 1
    lowest_path_list.append(i)

print(f"Solution to Part 2: {calculate_lcm(lowest_path_list)}")
