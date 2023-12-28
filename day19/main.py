import math
import re

with open("day19/input.txt", mode="r") as input_stream:
    process_list = input_stream.read()

workflows, parts = process_list.split("\n\n")
workflows = workflows.split("\n")
parts = parts.split("\n")


def split_condition(condition):
    pattern = r"([a-zA-Z]+)([<>]=?|==|=)(\d+)"
    # Match the pattern
    match = re.match(pattern, condition)
    if match:
        # Extract variable, operator, and value
        variable, operator, value = match.groups()
        return variable, operator, int(value)
    else:
        return None


def test_condition(char, operator, val, target):
    if operator == ">":
        return target > val
    else:
        return target < val


def split_rest(rest):
    rest = rest.split(",")
    last_case = rest[-1]
    flow = {}
    for step in rest[:-1]:
        condition, next_step = step.split(":")
        flow[condition] = next_step
    flow["LAST"] = last_case
    return flow


def get_workflow_map(workflow):
    workflow_name, rest = workflow.split("{")
    rest = rest[:-1]
    return workflow_name, rest


workflow_map = {}
for workflow in workflows:
    workflow_name, rest = get_workflow_map(workflow)
    workflow_map[workflow_name] = rest


part_list = []
for part in parts:
    part = part[1:-1]
    part_map = {}
    for part_char_string in part.split(","):
        part_char, _, char_value = split_condition(part_char_string)
        part_map[part_char] = char_value

    part_list.append(part_map)

total_sum = 0
for part_map in part_list:
    start_point = "in"
    while start_point not in ["A", "R"]:
        workflow = workflow_map[start_point]
        flow = split_rest(workflow)
        for condition in flow.keys():
            if condition != "LAST":
                char, operator, val = split_condition(condition)
                if test_condition(char, operator, val, part_map[char]):
                    default_workflow = False
                    start_point = flow[condition]
                    break
            else:
                start_point = flow["LAST"]
    if start_point == "A":
        part_sum = sum(list(part_map.values()))
        total_sum += part_sum

print(f"Solution to Part 1: {total_sum}")
# Part 2:
initial_ranges = {"x": (1, 4000), "m": (1, 4000), "a": (1, 4000), "s": (1, 4000)}


# Inspired by https://github.com/derailed-dash/Advent-of-Code/blob/master/src/AoC_2023/Dazbo's_Advent_of_Code_2023.ipynb
def count_ranges(
    initial_ranges: dict[str, tuple[int, int]],
    start_point: str,
    workflow_map: dict[str, str],
) -> int:
    # Base case
    if start_point == "R":
        return 0

    if start_point == "A":
        return math.prod((end - start + 1) for start, end in initial_ranges.values())

    workflow = workflow_map[start_point]
    flow = split_rest(workflow)
    default_case = False
    total = 0
    for condition in flow.keys():
        if condition[0] in "xmas":
            char, operator, val = split_condition(condition)
            low, high = initial_ranges[char]

            true_for_condition = (low, val - 1) if operator == "<" else (val + 1, high)

            false_for_condition = (val, high) if operator == "<" else (low, val)

            if true_for_condition[0] <= true_for_condition[1]:
                ranges_copy = dict(initial_ranges)  # make a copy of ranges
                ranges_copy[
                    char
                ] = true_for_condition  # pass through the new, true range
                total += count_ranges(ranges_copy, flow[condition], workflow_map)

            if false_for_condition[0] <= false_for_condition[1]:
                initial_ranges = dict(initial_ranges)
                initial_ranges[char] = false_for_condition
            else:
                break
        else:  # Default condition
            total += count_ranges(
                initial_ranges, flow[condition], workflow_map
            )  # recurse to next workflow

    return total


total_possibilities = count_ranges(
    initial_ranges, start_point="in", workflow_map=workflow_map
)
print(f"Solution to Part 2: {total_possibilities}")
