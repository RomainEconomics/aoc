
import pathlib
import re

path = pathlib.Path(__file__)
DATA_FOLDER = path.parent.parent / "data"

DATA_TEST = DATA_FOLDER / "input_test.txt"
DATA = DATA_FOLDER / "input.txt"

def read_file(file_path: pathlib.Path):
    with open(file_path) as f:
        data = f.read().splitlines()
        return data 


# Part 1

def parse_digits(line: str):
    digits = re.findall(r"\d+", line)
    return [int(i) for i in digits]


def part1(data_path: pathlib.Path):
    data = read_file(data_path)

    race_lasts = parse_digits(data[0])
    race_distance = parse_digits(data[1])

    res = 1
    for last, dist in zip(race_lasts, race_distance):
        H = last
        output = []
        for h in range(1, H):
            init = 0
            init = (last - h) * h
            if init > dist:
                output.append(init)
        res *= len(output)

    return res

answer_test = part1(DATA_TEST) == 288
answer = part1(DATA) == 252000

print("Part 1: ", answer_test, answer)

# Part 2

def part2(data_path: pathlib.Path):
    data = read_file(data_path)
    
    last = int(data[0].split(":")[1].replace(" ", ""))
    dist = int(data[1].split(":")[1].replace(" ", ""))

    h = 0
    output = []
    REVERSE = False

    while 0 <= h < last and len(output) < 2:
        init = 0
        init = (last - h) * h
        if init > dist:
            output.append(h)
            REVERSE = True
            h = last
        h += -1 if REVERSE else 1

    return output[1] - output[0] + 1

answer_test = part2(DATA_TEST) == 71503
answer = part2(DATA) == 36992486

print("Part 2: ", answer_test, answer)
