import pathlib

path = pathlib.Path("__file__")
DATA_FOLDER = path.parent.parent / "data"

DATA_TEST = DATA_FOLDER / "input_test.txt"
DATA = DATA_FOLDER / "input.txt"


def read_file(file_path: pathlib.Path):
    with open(file_path) as f:
        data = [list(i) for i in f.read().splitlines()]
        return data


def move_rocks(data):
    for row_idx in range(1, len(data)):
        for col_idx in range(len(data[row_idx])):
            val = data[row_idx][col_idx]

            if val == "O":
                new_row_idx = row_idx
                while new_row_idx > 0 and data[new_row_idx - 1][col_idx] == ".":
                    new_row_idx -= 1

                if new_row_idx != row_idx:
                    data[new_row_idx][col_idx] = "O"
                    data[row_idx][col_idx] = "."
    return data


def calculate_score(data):
    n_rows = len(data)

    return sum(row.count("O") * (n_rows - idx) for idx, row in enumerate(data))


# Part 1


def part1(data_path: pathlib.Path):
    data = read_file(data_path)
    data = move_rocks(data)

    return calculate_score(data)


answer_test = part1(DATA_TEST) == 136
answer = part1(DATA) == 110274

print("Part 1: ", answer_test, answer)

# Part 2


def cycle(data):
    for _ in range(4):
        data = move_rocks(data)
        data = list(map(list, zip(*data[::-1])))
    return data


def part2(data_path: pathlib.Path, n):
    data = read_file(data_path)

    cache = {}

    for i in range(n):
        hash_id = hash("".join(map("".join, data)))

        if hash_id in cache:
            cycle_start = cache[hash_id]
            cycle_length = i - cycle_start
            for _ in range((n - cycle_start) % cycle_length):
                data = cycle(data)
            break

        cache[hash_id] = i
        data = cycle(data)

    return calculate_score(data)


answer_test = part2(DATA_TEST, 1000000000) == 64
answer = part2(DATA, 1000000000) == 90982

print("Part 2: ", answer_test, answer)
