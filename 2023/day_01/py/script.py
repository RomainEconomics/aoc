import pathlib
import re

path = pathlib.Path(__file__)
DATA_FOLDER = path.parent.parent / "data"

DATA_TEST = DATA_FOLDER / "input_test.txt"
DATA_TEST_PART2 = DATA_FOLDER / "input_test_part2.txt"
DATA = DATA_FOLDER / "input.txt"


def read_file(file_path: pathlib.Path):
    with open(file_path) as f:
        data = f.read().splitlines()
        return data


# Part 1


def part1(data_path: pathlib.Path):
    data = read_file(data_path)
    digits = [re.findall(r"\d", row) for row in data]
    calibration_values = [int(digit[0] + digit[-1]) for digit in digits]
    return sum(calibration_values)


answer_test = part1(DATA_TEST) == 142
answer = part1(DATA) == 55816

print("Part 1: ", answer_test, answer)

# Part 2


digits_mapping = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def replace_digits(string: str):
    numbers = re.findall(r'(?=(\d|one|two|three|four|five|six|seven|eight|nine))', string)
    first = numbers[0] if numbers[0].isdigit() else digits_mapping[numbers[0]]
    last = numbers[-1] if numbers[-1].isdigit() else digits_mapping[numbers[-1]]
    return int(first + last)


def part2(data_path: pathlib.Path):
    data = read_file(data_path)
    digits = [replace_digits(s) for s in data]
    return sum(digits)


answer_test = part2(DATA_TEST_PART2) == 281
answer = part2(DATA) == 54980

print("Part 2: ", answer_test, answer)
