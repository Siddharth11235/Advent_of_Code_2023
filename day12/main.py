with open("day12/input.txt", mode="r") as input_stream:
    spring_status_map = input_stream.read().splitlines()

spring_status_info = []
contiguous_spring_info = []
for spring_info_line in spring_status_map:
    spring_info = spring_info_line.split()[0]
    contiguous_info = spring_info_line.split()[1]
    spring_status_info.append(spring_info)
    contiguous_spring_info.append([int(x) for x in contiguous_info.split(",")])


# Approach taken from
# https://github.com/tmo1/adventofcode/blob/main/2023/12.py
def calculate_potential_ways(spring_info, contiguous_info):
    positions = {0: 1}
    for i, contiguous in enumerate(contiguous_info):
        new_positions = {}
        for k, v in positions.items():
            for n in range(
                k,
                len(spring_info)
                - sum(contiguous_info[i + 1 :])
                + len(contiguous_info[i + 1 :]),
            ):
                if (
                    n + contiguous - 1 < len(spring_info)
                    and "." not in spring_info[n : n + contiguous]
                ):
                    if (
                        i == len(contiguous_info) - 1
                        and "#" not in spring_info[n + contiguous :]
                    ) or (
                        i < len(contiguous_info) - 1
                        and n + contiguous < len(spring_info)
                        and spring_info[n + contiguous] != "#"
                    ):
                        new_positions[n + contiguous + 1] = (
                            new_positions[n + contiguous + 1] + v
                            if n + contiguous + 1 in new_positions
                            else v
                        )
                if spring_info[n] == "#":
                    break
        positions = new_positions

    return sum(positions.values())


total_out = 0
for spring_status, contiguous_group in zip(spring_status_info, contiguous_spring_info):
    out = calculate_potential_ways(spring_status, contiguous_group)
    total_out += out
print(f"Solution to Part 1: {total_out}")

# Part 2
spring_status_info = []
contiguous_spring_info = []
for spring_info_line in spring_status_map:
    spring_info = spring_info_line.split()[0]
    updated_spring_info = spring_info
    for _ in range(4):
        updated_spring_info = updated_spring_info + "?" + spring_info
    contiguous_info = spring_info_line.split()[1]
    spring_status_info.append(updated_spring_info)
    contiguous_spring_info.append([int(x) for x in contiguous_info.split(",")] * 5)

total_out = 0
for spring_status, contiguous_group in zip(spring_status_info, contiguous_spring_info):
    out = calculate_potential_ways(spring_status, contiguous_group)
    total_out += out
print(f"Solution to Part 2: {total_out}")
