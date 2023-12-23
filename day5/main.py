with open("day5/input.txt", mode="r") as input_stream:
    all_maps = input_stream.read().splitlines()
    text = input_stream.read()


# Common Logic
seeds = [int(num) for num in all_maps[0].split(":")[1].split() if num]

all_maps_orig = all_maps

all_maps = all_maps[1:]
range_maps_dict = {}
i = 0


def map_seed_to_location(seed, farming_range_maps):
    measured_var = seed
    for _, quantity_ranges in farming_range_maps.items():
        for quantity_range in quantity_ranges:
            max_val = quantity_range[1] + quantity_range[2]
            if measured_var >= quantity_range[1] and measured_var < max_val:
                diff = measured_var - quantity_range[1]
                measured_var = quantity_range[0] + diff
                break

    return measured_var


while i < len(all_maps):
    if all_maps[i] == "":
        current_key = all_maps[i + 1]
        range_maps_dict[current_key] = []
        i += 2
    else:
        range_maps_dict[current_key].append(
            [int(num) for num in all_maps[i].split() if num]
        )
        i += 1

# Part 1

cur_min_location = 10**12
for seed in seeds:
    seed_min_location = map_seed_to_location(seed, range_maps_dict)
    if seed_min_location < cur_min_location:
        cur_min_location = seed_min_location

print(f"Solution to Part 1: {cur_min_location}")


# Part 2:
def source_start_sort(map):
    return map["source_start"]


def start_sort(map):
    return map["start"]


seed_starts = [seeds[i] for i in range(len(seeds)) if i % 2 == 0]
seed_ranges = [seeds[i] for i in range(len(seeds)) if i % 2 == 1]

seed_map = [
    {"start": seed_start, "end": seed_start + seed_range - 1}
    for seed_start, seed_range in zip(seed_starts, seed_ranges)
]

seeds = []
farming_diff_map_list = []

for range_map in range_maps_dict.values():
    current_diff_map = []
    for map in range_map:
        diff_mapping = {}
        diff_mapping["source_start"] = map[1]
        diff_mapping["difference"] = map[1] - map[0]
        diff_mapping["source_end"] = map[1] + map[2] - 1
        current_diff_map.append(diff_mapping)
    farming_diff_map_list.append(current_diff_map)


for farming_diff_map in farming_diff_map_list:
    farming_diff_map.sort(key=source_start_sort)

current_map = seed_map
for farming_diff_map in farming_diff_map_list:
    next_element_map = []

    for seed_map_element in current_map:
        current_element_start = seed_map_element["start"]
        for single_map in farming_diff_map:
            potential_start = max(single_map["source_start"], current_element_start)

            if potential_start > seed_map_element["end"]:
                break

            potential_end = min(single_map["source_end"], seed_map_element["end"])

            if potential_end >= potential_start:
                if current_element_start < potential_start:
                    next_element_map.append(
                        {"start": current_element_start, "end": potential_start - 1}
                    )
                next_element_map.append(
                    {
                        "start": potential_start - single_map["difference"],
                        "end": potential_end - single_map["difference"],
                    }
                )
                current_element_start = potential_end + 1

        if current_element_start < seed_map_element["end"]:
            next_element_map.append(
                {"start": current_element_start, "end": seed_map_element["end"]}
            )

        current_map = next_element_map.copy()

next_element_map.sort(key=start_sort)

print(f"Solution to Part 2: {next_element_map[0]['start']}")
