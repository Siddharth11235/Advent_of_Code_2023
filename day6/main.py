with open("day6/input.txt", mode="r") as input_stream:
    all_races = input_stream.read().splitlines()


# Common
def get_num_methods(distance, time):
    num_methods = 0
    for i in range(time + 1):
        if i * (time - i) > distance:
            num_methods += 1

    return num_methods


# Part 1
distances = [int(x) for x in all_races[1].split(":")[1].split()]
times = [int(x) for x in all_races[0].split(":")[1].split()]


def get_num_methods(distance, time):
    for i in range(time + 1):
        if i * (time - i) > distance:
            break
    return time - 2 * i + 1


total_num_methods = 1
for distance, time in zip(distances, times):
    total_num_methods = total_num_methods * get_num_methods(distance, time)
print(f"Solution to Part 1: {total_num_methods}")

# Part 2
distance = int(all_races[1].split(":")[1].replace(" ", ""))
time = int(all_races[0].split(":")[1].replace(" ", ""))

print(f"Solution to Part 2: {get_num_methods(distance, time)}")
