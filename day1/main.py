with open("day1/input.txt", mode="r") as input_stream:
    improved_calibration_list = input_stream.readlines()

# Part 1
calibration_result = 0
for improved_calibration in improved_calibration_list:
    number_list = [i for i in improved_calibration.split()[0] if i.isdigit()]

    calibration = int("".join([number_list[0], number_list[-1]]))
    calibration_result += calibration
print(f"Solution to Part 1: {calibration_result}")

# Part 2
string_to_num_dict = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
    "zero": "0",
}


def extract_number_list(calibration_string):
    indexed_number_list = []
    for word, digit in string_to_num_dict.items():
        ind_list = [
            i
            for i in range(len(calibration_string))
            if calibration_string.startswith(word, i)
        ]

        for ind in ind_list:
            if ind != -1:
                indexed_number_list.append((ind, string_to_num_dict[word]))

        ind_list = [
            i
            for i in range(len(calibration_string))
            if calibration_string.startswith(digit, i)
        ]
        for ind in ind_list:
            if ind != -1:
                indexed_number_list.append((ind, digit))

    indexed_number_list.sort(key=lambda a: a[0])

    number_list = [indexed_tuple[1] for indexed_tuple in indexed_number_list]

    return number_list


calibration_result = 0
for improved_calibration in improved_calibration_list:
    number_list = extract_number_list(improved_calibration)
    calibration = int("".join([number_list[0], number_list[-1]]))
    calibration_result += calibration

print(f"Solution to Part 2: {calibration_result}")
