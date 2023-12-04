
import re
import pathlib

path = pathlib.Path(__file__)
DATA_FOLDER = path.parent.parent / "data"

DATA_TEST = DATA_FOLDER / "input_test.txt"
DATA = DATA_FOLDER / "input.txt"

def read_file(file_path: pathlib.Path):
    with open(file_path) as f:
        data = f.read().splitlines()
        return data 

def process_row(row):
    _, cards = row.split(':')
    winning_cards, my_cards = cards.split('|')
    winning_cards, my_cards = re.findall(r'\d+', winning_cards), re.findall(r'\d+', my_cards) 

    intersect = set(winning_cards) & set(my_cards)
    return intersect


# Part 1

def part1(data_path: pathlib.Path):
    data = read_file(data_path)

    points = 0
    for row in data:
        intersect = process_row(row)
        points += 2 ** (len(intersect) -1) if intersect else 0
    return points

answer_test = part1(DATA_TEST) == 13
answer = part1(DATA) == 23847

print("Part 1: ", answer_test, answer)

# Part 2

def part2(data_path: pathlib.Path):
    data = read_file(data_path)
    
    d = {i: 1 for i in range(1, len(data)+1)}

    for idx, row in enumerate(data, start=1):
        intersect = process_row(row)
        for i in range(idx+1, idx + len(intersect)+1):
            d[i] += d[idx]

    return sum(d.values())


answer_test = part2(DATA_TEST) == 30
answer = part2(DATA) == 8570000

print("Part 2: ", answer_test, answer)
