with open("day2/input.txt", mode="r") as input_stream:
    game_list = input_stream.read().splitlines()

max_acceptable_game = {"red": 12, "green": 13, "blue": 14}

acceptable_game_sum = 0  # Solution to Part 1
set_power_sum = 0  # Solution to Part 2

for game in game_list:
    max_game = {"red": 0, "green": 0, "blue": 0}

    # Lots of string manipulation to get the counts of balls
    game_index = int(game.split(":")[0].split(" ")[1])
    individual_games = game.split(":")[1].split(";")
    for individual_game in individual_games:
        ballsets = individual_game.split(",")
        for ballset in ballsets:
            ballset_split = ballset.split(" ")
            if int(ballset_split[1]) > max_game[ballset_split[2]]:
                max_game[ballset_split[2]] = int(ballset_split[1])

    good_game = True  # To check if a game is good for part 1
    set_power = 1  # To get the set power for part 2
    for colour_key in max_acceptable_game.keys():
        if max_acceptable_game[colour_key] < max_game[colour_key]:
            good_game = False
        set_power *= max_game[colour_key]
    if good_game:
        acceptable_game_sum += game_index
    set_power_sum += set_power

print(f"Solution to Part 1: {acceptable_game_sum}")
print(f"Solution to Part 2: {set_power_sum}")
