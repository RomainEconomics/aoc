import pathlib
import re

DATA_FOLDER = pathlib.Path("2024/day_03/data")

DATA_TEST = DATA_FOLDER / "input_test.txt"
DATA = DATA_FOLDER / "input.txt"


def read_file(file_path: pathlib.Path):
    with open(file_path) as f:
        data = f.read().strip()
        return data


def clean_instruction(s: str) -> int:
    left, right = s.split(",")
    left, right = re.findall(r"\d+", left), re.findall(r"\d+", right)
    return int(left[0]) * int(right[0])


# Part 1


def part1(data_path: pathlib.Path):
    data = read_file(data_path)
    operations = re.findall(r"mul\(\d+,\d+\)", data)
    res = 0

    for op in operations:
        res += clean_instruction(op)
    return res


answer_test = part1(DATA_TEST) == 161
answer = part1(DATA) == 187825547

print("Part 1: ", answer_test, answer)

# Part 2


def flatten(data: list[tuple[str]]):
    flat = []
    for x in data:
        flat += [i for i in x if i]
    return flat


def part2(data_path: pathlib.Path):
    data = read_file(data_path)
    r = re.compile(r"(mul\(\d+,\d+\))|(don\'t\(\))|(do\(\))")

    match = r.findall(data)
    instructions = flatten(match)

    do = True
    res = 0

    for i in instructions:
        if i == "don't()":
            do = False
        elif i == "do()":
            do = True
        else:
            if do:
                res += clean_instruction(i)

    return res


answer = part2(DATA) == 85508223

print("Part 2: ", answer)
