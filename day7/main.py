with open("day7/input.txt", mode="r") as input_stream:
    all_hands_and_bids = input_stream.read().splitlines()


def check_freq(x):
    freq = {}
    for c in set(x):
        freq[c] = x.count(c)
    return dict(sorted(freq.items(), key=lambda x: x[1], reverse=True))


def get_hand_type(hand):
    character_frequency = check_freq(hand)
    character_frequency_list = list(character_frequency.values())
    if len(set(hand)) == 1:
        return 7
    if len(character_frequency) == 2:
        if character_frequency_list[0] == 4:
            return 6
        elif character_frequency_list[0] == 3 and character_frequency_list[1] == 2:
            return 5
    if len(character_frequency) == 3:
        if character_frequency_list[0] == 3:
            return 4
        if character_frequency_list[0] == 2 and character_frequency_list[1] == 2:
            return 3
    if character_frequency_list[0] == 2:
        return 2
    if character_frequency_list[0] == 1:
        return 1


# Part 1
HAND_DICT = {
    1: [],  # High card
    2: [],  # One pair
    3: [],  # Two pairs
    4: [],  # Three of a kind
    5: [],  # Full house
    6: [],  # Four of a kind
    7: [],  # Five of a kind
}


def get_card_mapping(hand_and_bid):
    # This is a mapping that makes sorting hands possible
    hand = hand_and_bid[0]
    out_str = ""
    face_card_mapping = {"A": "Z", "K": "Y", "Q": "X", "J": "W", "T": "T"}
    for card in hand:
        if card.isdigit():
            out_str = out_str + card
        else:
            out_str = out_str + face_card_mapping[card]
    return out_str


for hand_and_bid in all_hands_and_bids:
    hand, bid = hand_and_bid.split()
    bid = int(bid)
    hand_type = get_hand_type(hand)
    HAND_DICT[hand_type].append((hand, bid))

final_hand_list = []
for key in HAND_DICT.keys():
    if len(HAND_DICT[key]) > 0:
        HAND_DICT[key].sort(key=get_card_mapping)
        final_hand_list = final_hand_list + HAND_DICT[key]

total_winnings = 0
for i, hand_and_bid in enumerate(final_hand_list):
    hand_winnings = (i + 1) * hand_and_bid[1]
    total_winnings += hand_winnings

print(f"Solution to Part 1: {total_winnings}")


# Part 2
HAND_DICT = {
    1: [],  # High card
    2: [],  # One pair
    3: [],  # Two pairs
    4: [],  # Three of a kind
    5: [],  # Full house
    6: [],  # Four of a kind
    7: [],  # Five of a kind
}


def get_card_mapping(hand_and_bid):
    # This is a mapping that makes sorting hands possible
    # J is now the weakest card in this context
    hand = hand_and_bid[0]
    out_str = ""
    face_card_mapping = {"A": "Z", "K": "Y", "Q": "X", "J": "1", "T": "T"}
    for card in hand:
        if card.isdigit():
            out_str = out_str + card
        else:
            out_str = out_str + face_card_mapping[card]
    return out_str


def get_hand_type(hand):
    character_frequency = check_freq(hand)
    character_frequency_list = list(character_frequency.values())
    character_frequency_keys = list(character_frequency.keys())

    if len(set(hand)) == 1:
        return 7
    if len(character_frequency) == 2:
        if character_frequency_list[0] == 4:
            if "J" in hand:
                return 7
            else:
                return 6
        elif character_frequency_list[0] == 3 and character_frequency_list[1] == 2:
            if "J" in hand:
                return 7
            else:
                return 5
    if len(character_frequency) == 3:
        if character_frequency_list[0] == 3:
            if "J" in hand:
                return 6
            else:
                return 4
        if character_frequency_list[0] == 2 and character_frequency_list[1] == 2:
            if character_frequency_keys[0] == "J" or character_frequency_keys[1] == "J":
                return 6
            elif character_frequency_keys[2] == "J":
                return 5
            else:
                return 3
    if len(character_frequency) == 4:
        if character_frequency_list[0] == 2:
            if "J" in hand:
                return 4
            else:
                return 2
    if len(character_frequency) == 5:
        if "J" in hand:
            return 2
        else:
            return 1


for hand_and_bid in all_hands_and_bids:
    hand, bid = hand_and_bid.split()
    bid = int(bid)
    hand_type = get_hand_type(hand)
    HAND_DICT[hand_type].append((hand, bid))


final_hand_list = []
for key in HAND_DICT.keys():
    if len(HAND_DICT[key]) > 0:
        HAND_DICT[key].sort(key=get_card_mapping)
        final_hand_list = final_hand_list + HAND_DICT[key]

total_winnings = 0
for i, hand_and_bid in enumerate(final_hand_list):
    hand_winnings = (i + 1) * hand_and_bid[1]
    total_winnings += hand_winnings

print(f"Solution to Part 2: {total_winnings}")
