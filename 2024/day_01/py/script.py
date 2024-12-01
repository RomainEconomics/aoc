import pathlib

DATA_FOLDER = pathlib.Path("2024/day_01/data")

DATA_TEST = DATA_FOLDER / "input_test.txt"
DATA = DATA_FOLDER / "input.txt"


def read_file(file_path: pathlib.Path) -> tuple[list[int], list[int]]:
    with open(file_path) as f:
        l1, l2 = [], []
        for line in f:
            a, b = line.split()
            l1.append(int(a))
            l2.append(int(b))
        return l1, l2


# Part 1


def part1(data_path: pathlib.Path):
    l1, l2 = read_file(data_path)

    return sum([abs(x - y) for x, y in zip(sorted(l1), sorted(l2))])


answer_test = part1(DATA_TEST) == 11
answer = part1(DATA) == 3574690

print("Part 1: ", answer_test, answer)


# Part 2


def part2(data_path: pathlib.Path):
    l1, l2 = read_file(data_path)
    d = {}

    sim_score = 0

    for x in l1:
        if x not in d:
            d[x] = l2.count(x) * x
        sim_score += d[x]

    return sim_score


answer_test = part2(DATA_TEST) == 31
answer = part2(DATA) == 22565391

print("Part 2: ", answer_test, answer)
