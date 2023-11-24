
import pathlib
from dataclasses import dataclass
import re

path = pathlib.Path(__file__)
DATA_FOLDER = path.parent.parent / "data"

DATA_TEST =   DATA_FOLDER / "input_test.txt"
DATA = DATA_FOLDER / "input.txt"

@dataclass
class PuzzleInput:
    min_val: int
    max_val: int
    target_word: str
    password: str


def read_file(file_path: pathlib.Path) -> list[PuzzleInput]:
    regex = r"(\d+)-(\d+) (\w): (\w+)"
    data: list[PuzzleInput] = []

    with open(file_path) as f:
        for line in f:
            match = re.match(regex, line)
            min_val, max_val, target_word, password = match.groups()
            data.append(
                PuzzleInput(
                    min_val=int(min_val),
                    max_val=int(max_val),
                    target_word=target_word,
                    password=password
                )
            )
    return data

def is_valid_password_part1(puzzle_input: PuzzleInput) -> bool:
    occurences = sum(s == puzzle_input.target_word for s in puzzle_input.password)
    return occurences >= puzzle_input.min_val and occurences <= puzzle_input.max_val 

def is_valid_password_part2(puzzle_input: PuzzleInput) -> bool:
    min_index = puzzle_input.password[puzzle_input.min_val-1] == puzzle_input.target_word
    max_index = puzzle_input.password[puzzle_input.max_val-1] == puzzle_input.target_word

    return min_index + max_index == 1

# Part 1

data_test: list[PuzzleInput] = read_file(DATA_TEST)
answer_test = sum(is_valid_password_part1(i) for i in data_test) == 2


data: list[PuzzleInput] = read_file(DATA)
answer = sum(is_valid_password_part1(i) for i in data) == 548

print("Part 1:", answer_test, answer)


# Part 2

data_test: list[PuzzleInput] = read_file(DATA_TEST)
answer_test = sum(is_valid_password_part2(i) for i in data_test) == 1


data: list[PuzzleInput] = read_file(DATA)
answer = sum(is_valid_password_part2(i) for i in data) == 502

print("Part 2:", answer_test, answer)