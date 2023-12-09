
import pathlib
from collections import Counter

path = pathlib.Path(__file__)
DATA_FOLDER = path.parent.parent / "data"

DATA_TEST = DATA_FOLDER / "input_test.txt"
DATA = DATA_FOLDER / "input.txt"

def read_file(file_path: pathlib.Path):
    with open(file_path) as f:
        data = f.read().splitlines()
        return data 

data = read_file(DATA_TEST)
data = read_file(DATA)

card_values = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10, '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3':3, '2': 2}

def check_hand_type(cards, joker=False):

    card_count = Counter(cards)

    # Part 2
    if joker:
        if j_value := card_count.pop("J", None):
            if j_value == 5:
                return 6
            most_common = card_count.most_common(1)[0]
            card_count[most_common[0]] += j_value

    card_count = sorted(card_count.items(), key=lambda x: x[1], reverse=True)
    card_count = [i[1] for i in card_count]
    match card_count:
        case [5]: return 6
        case [4, 1]: return 5
        case [3, 2]: return 4
        case [3, 1, 1]: return 3
        case [2, 2, 1]: return 2
        case [2, 1, 1, 1]: return 1
        case _: return 0

# Part 1

def solve(data_path: pathlib.Path, joker=False):
    data = read_file(data_path)
    hands = []

    for i in data:
        cards, bid = i.split(' ')
        hands.append((cards, int(bid)))

    hands = sorted(hands, key=lambda x: (check_hand_type(x[0], joker=joker), [card_values[i] for i in  list(x[0])]))

    return sum((idx) * hand[-1] for idx, hand in enumerate(hands, start=1))


answer_test = solve(DATA_TEST) == 6440
answer = solve(DATA) == 250951660

print("Part 1: ", answer_test, answer)

# Part 2

# J becomes the lowest card in the deck
card_values['J'] = 1

answer_test = solve(DATA_TEST, joker=True) == 5905
answer = solve(DATA, joker=True) == 251481660

print("Part 2: ", answer_test, answer)
