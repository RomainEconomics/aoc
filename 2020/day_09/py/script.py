from collections import deque, OrderedDict

d = OrderedDict()

d

import pathlib

path = pathlib.Path(__file__)
DATA_FOLDER = path.parent.parent / "data"

DATA = DATA_FOLDER / "input.txt"
DATA_TEST = DATA_FOLDER / "input_test.txt"


def read_file(file_path: pathlib.Path) -> list[int]:
    with open(file_path) as f:
        data: list[str] = f.read().splitlines()
        return list(map(int, data))


# Part 1


def part1(data_path: pathlib.Path, max_len: int) -> int:
    data: list[int] = read_file(data_path)

    prev_numbers = deque(data[:max_len], maxlen=max_len)

    for i in range(max_len, len(data)):
        next_val = data[i]

        NO_VALID_NUM = True
        for x in prev_numbers:
            try:
                prev_numbers.index(next_val - x)
                NO_VALID_NUM = False
                break
            except ValueError:
                continue

        if NO_VALID_NUM:
            return next_val

        prev_numbers.append(next_val)


answer_test = part1(DATA_TEST, max_len=5) == 127
answer = part1(DATA, max_len=25) == 14360655

print("Part 1:", answer_test, answer)

# Part 2


def part2(data_path: pathlib.Path, target_num: int) -> int:
    data = read_file(data_path)

    L, R = 0, 1

    while L < R and R < len(data):
        sum_a = sum(data[L:R])

        if sum_a == target_num:
            return min(data[L:R]) + max(data[L:R])

        if sum_a > target_num:
            L += 1
            continue
        R += 1


answer_test = part2(DATA_TEST, 127) == 62
answer = part2(DATA, 14360655) == 1962331

print("Part 2: ", answer_test, answer)
