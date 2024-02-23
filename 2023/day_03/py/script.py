
import itertools
import re
import pathlib

path = pathlib.Path(__file__)
DATA_FOLDER = path.parent.parent / "data"

DATA_TEST = DATA_FOLDER / "input_test.txt"
DATA = DATA_FOLDER / "input.txt"

def read_file(file_path: pathlib.Path):
    with open(file_path) as f:
        return f.read().splitlines() 

neighbours = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1,-1), (-1, 0), (-1, 1)]


# Part 1

def find_adjacent_symbol(data: list, row_idx: int, match: re.Match[str]):
    start, end, number = match.start(), match.end(), match.group()
    for col_idx in range(start, end):
        for neighbor in neighbours:
            adjacent_col = col_idx + neighbor[0]
            adjacent_row = row_idx + neighbor[1]
            if 0 <= adjacent_row < len(data) and 0 <= adjacent_col < len(data[0]):
                x = data[adjacent_row][adjacent_col]
                if not x.isdigit() and x != ".":
                    return int(number)
    return 0

def part1(data_path: pathlib.Path):
    data = read_file(data_path)
 
    output = 0
    idx_row = 0
    while idx_row < len(data):
        for match in re.finditer(r"\d+", data[idx_row]):
            output += find_adjacent_symbol(data, idx_row, match) 
        idx_row += 1
    return output

answer_test = part1(DATA_TEST) == 4361
answer = part1(DATA) == 531932

print("Part 1: ", answer_test, answer)


# Part 2

def find_stars(data: list):
    return {
        (row_idx, col_idx)
        for row_idx, col_idx in itertools.product(
            range(len(data)), range(len(data[0]))
        )
        if data[row_idx][col_idx] == "*"
    }

def part2(data_path: pathlib.Path):
    data = read_file(data_path)

    stars = find_stars(data)
    output = 0

    for star in stars:

        adj_num = []
        for row_idx in range(star[0] - 1, star[0] + 2):
            if row_idx < 0 or row_idx >= len(data):
                continue

            star_neighbor_idx = [(star[0] + neighbour[0], star[1] + neighbour[1]) for neighbour in neighbours]
            for match in re.finditer(r"\d+", data[row_idx]):
                start, end, number = match.start(), match.end(), match.group()
                num_idx = {(row_idx, col_idx) for col_idx in range(start, end)}
                if any(i in num_idx for i in star_neighbor_idx):
                    adj_num.append(int(number))
        if len(adj_num) == 2:
            output += adj_num[0] * adj_num[1]

    return output


answer_test = part2(DATA_TEST) == 467835
answer = part2(DATA) == 73646890

print("Part 2: ", answer_test, answer)
