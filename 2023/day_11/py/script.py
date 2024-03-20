import pathlib
import re
from itertools import combinations

path = pathlib.Path(__file__)
DATA_FOLDER = path.parent.parent / "data"

DATA_TEST = DATA_FOLDER / "input_test.txt"
DATA = DATA_FOLDER / "input.txt"


def read_file(file_path: pathlib.Path):
    with open(file_path) as f:
        return f.read().splitlines()


# data = read_file(DATA_TEST)


# Part 1


def solution(data_path: pathlib.Path, size: int = 2):
    data = read_file(data_path)

    galaxies = {}

    for row_idx, row in enumerate(data):
        match_galaxies = re.finditer("#", row)
        for m in match_galaxies:
            galaxies[len(galaxies)] = [row_idx, m.start()]

    empty_rows = [idx for idx, row in enumerate(data) if all(i == "." for i in row)]
    empty_cols = [
        idx for idx in range(len(data[0])) if all(row[idx] == "." for row in data)
    ]

    r = 0
    for row_idx in empty_rows:
        row_idx += r
        for g in galaxies:
            if galaxies[g][0] > row_idx:
                galaxies[g][0] += size - 1
        r += size - 1

    c = 0
    for col_idx in empty_cols:
        col_idx += c
        for g in galaxies:
            if galaxies[g][1] > col_idx:
                galaxies[g][1] += size - 1
        c += size - 1

    combs = list(combinations(galaxies.keys(), 2))

    output = 0
    for x, y in combs:
        x1, x2 = galaxies[x]
        y1, y2 = galaxies[y]

        output += abs(x1 - y1) + abs(x2 - y2)

    return output


answer_test = solution(DATA_TEST) == 374
answer = solution(DATA) == 10292708

print("Part 1: ", answer_test, answer)

# Part 2

answer_test = solution(DATA_TEST, 100) == 8410
answer = solution(DATA, 1_000_000) == 790194712336

print("Part 2: ", answer_test, answer)
