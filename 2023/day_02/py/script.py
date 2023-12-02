
from functools import reduce
import pathlib
import re


path = pathlib.Path(__file__)
DATA_FOLDER = path.parent.parent / "data"

DATA_TEST =   DATA_FOLDER / "input_test.txt"
DATA = DATA_FOLDER / "input.txt"

def read_file(file_path: pathlib.Path):
    with open(file_path) as f:
        data = f.read().splitlines()
        return data 

max_bag = {
    "red": 12,
    "green": 13,
    "blue": 14,
}

# Part 1

def check_game(line):
    game, cubes = line.split(":")
    game_id = int(game.split(" ")[1])

    for cube in cubes.split(";"):
        for i in cube.split(","):
            num, color = i.strip().split(" ")
            if int(num) > max_bag[color]:
                return 0

    return game_id

def part1(data_path: pathlib.Path):
    data = read_file(data_path)

    return sum([check_game(i) for i in data])

answer_test = part1(DATA_TEST) == 8
answer = part1(DATA) == 1734


print("Part 1: ", answer_test, answer)

# Part 2


def line_power(line: str):
    _, cubes = line.split(":")

    min_bag = {k: 0 for k in max_bag.keys()}

    for cube in cubes.split(";"):
        for i in cube.split(","):
            num, color = i.strip().split(" ")
            min_bag[color] = max(min_bag[color], int(num))

    return reduce(lambda x, y: x*y, list(min_bag.values()))

def part2(data_path: pathlib.Path):
    data = read_file(data_path)

    return sum([line_power(i) for i in data])


answer_test = part2(DATA_TEST) == 2286
answer = part2(DATA) == 70387


print("Part 2: ", answer_test, answer)