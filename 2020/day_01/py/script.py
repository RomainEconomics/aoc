
import pathlib

path = pathlib.Path(__file__)
DATA_FOLDER = path.parent.parent / "data"

DATA_TEST =   DATA_FOLDER / "input_test.txt"
DATA = DATA_FOLDER / "input.txt"

def read_file(file_path: pathlib.Path):
    with open(file_path) as f:
        data = f.read().splitlines()
        return list(map(int, data)) 

data = read_file(DATA_TEST)


# Part 1

def target_two_sum(data_path: pathlib.Path, target: int = 2020):
    data = read_file(data_path)
    
    d = set()
    for value in data:
        val = target - value
        if val in d:
            return value * val
        d.add(value)
    return 0

test_answer = target_two_sum(DATA_TEST) == 514579
answer = target_two_sum(DATA) == 935419

print("Part 1: ", test_answer, answer)

# Part 2


# Brute force

def target_three_sum(data_path: pathlib.Path, target: int = 2020):
    data = read_file(data_path)

    for L in range(len(data)-2):
        for M in range(L, len(data)-1):
            for R in range(M, len(data)):
                if data[L] + data[M] + data[R] == target:
                    return data[L] * data[M] * data[R]
                


test_answer = target_three_sum(DATA_TEST) == 241861950
answer = target_three_sum(DATA) == 49880012

print("Part 2: ", test_answer, answer)