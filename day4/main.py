with open("day4/input.txt", mode="r") as input_stream:
    card_numbers = input_stream.read().splitlines()


## Part 1
total_winnings = 0

for card in card_numbers:
    card_winnings = 0
    card_info = card.split(":")[1].split("|")
    card_winning_nums = set(int(num) for num in card_info[0].split() if num)
    card_nums = set(int(num) for num in card_info[1].split() if num)

    matching_nums = card_nums & card_winning_nums  # Intersection of both sets

    for card_num in matching_nums:
        if card_winnings == 0:
            card_winnings += 1
        else:
            card_winnings = card_winnings * 2
    total_winnings += card_winnings

print(f"Solution to Part 1: {total_winnings}")


## Part 2
def process_card(card, cards):
    card_info = card.split(":")[1].split("|")
    card_winning_nums = set(int(num) for num in card_info[0].split() if num)
    card_nums = set(int(num) for num in card_info[1].split() if num)

    matching_nums = len(card_nums & card_winning_nums)
    return matching_nums


def process_cards(cards):
    card_count = [1] * len(cards)

    for i in range(len(cards)):
        match_count = process_card(cards[i], cards)
        for j in range(1, match_count + 1):
            if i + j < len(cards):
                card_count[i + j] += card_count[i]

    return sum(card_count)


total_cards = process_cards(card_numbers)
print(f"Total number of scratchcards: {total_cards}")
