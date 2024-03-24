import pathlib

path = pathlib.Path(__file__)
DATA_FOLDER = path.parent.parent / "data"

DATA_TEST = DATA_FOLDER / "input_test.txt"
DATA = DATA_FOLDER / "input.txt"


def read_file(file_path: pathlib.Path) -> list[list[str]]:
    with open(file_path) as f:
        data = f.read().split("\n\n")
        data = [row.split("\n") for row in data]
    return data


# Part 1


def find_reflexion(pattern: list[str], part1=True):
    for row_idx in range(1, len(pattern)):
        above = pattern[:row_idx][::-1]
        below = pattern[row_idx:]

        above = above[: len(below)]
        below = below[: len(above)]

        if part1 and (above == below):
            return row_idx

        if not part1 and (
            sum(
                sum(0 if a == b else 1 for a, b in zip(x, y))
                for x, y in zip(above, below)
            )
            == 1
        ):
            return row_idx
    return 0


def part1(data_path: pathlib.Path):
    data: list[list[str]] = read_file(data_path)

    total = 0

    for pattern in data:
        idx = find_reflexion(pattern)
        total += 100 * idx

        # transpose: list(zip(*pattern))
        idx = find_reflexion(list(zip(*pattern)))
        total += idx
    return total


answer_test = part1(DATA_TEST) == 405
answer = part1(DATA) == 33047

print("Part 1: ", answer_test, answer)

# Part 2


def part2(data_path: pathlib.Path):
    data: list[list[str]] = read_file(data_path)

    total = 0

    for pattern in data:
        idx = find_reflexion(pattern, part1=False)
        total += 100 * idx

        # transpose: list(zip(*pattern))
        idx = find_reflexion(list(zip(*pattern)), part1=False)
        total += idx
    return total


answer_test = part2(DATA_TEST) == 400
answer = part2(DATA) == 28806

print("Part 2: ", answer_test, answer)
