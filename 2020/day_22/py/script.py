
import pathlib

path = pathlib.Path(__file__)
DATA_FOLDER = path.parent.parent / "data"

DATA_TEST = DATA_FOLDER / "input_test.txt"
DATA = DATA_FOLDER / "input.txt"

def read_file(file_path: pathlib.Path):
    with open(file_path) as f:
        data = f.read().splitlines()
        return data 

data = read_file(DATA_TEST)


# Part 1

def part1(data_path: pathlib.Path):
    data = read_file(data_path)
    return 0

# answer_test = part1(DATA_TEST) == 0
# answer = part1(DATA) == 0

# print("Part 1: ", answer_test, answer)

# Part 2

def part2(data_path: pathlib.Path):
    data = read_file(data_path)
    return 0

# answer_test = part2(DATA_TEST) == 0
# answer = part2(DATA) == 0

# print("Part 2: ", answer_test, answer)
