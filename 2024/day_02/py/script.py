import pathlib

DATA_FOLDER = pathlib.Path("2024/day_02/data")

DATA = DATA_FOLDER / "input.txt"
DATA_TEST = DATA_FOLDER / "input_test.txt"


def read_file(file_path: pathlib.Path):
    with open(file_path) as f:
        data = [[int(i) for i in line.split()] for line in f]
        return data


# Part 1


def is_safe(report: list[int]) -> bool:
    return all(report[0] * i > 0 and abs(i) <= 3 for i in report)


def part1(data_path: pathlib.Path):
    data = read_file(data_path)
    levels = []

    for a in data:
        report = [a[i] - a[i - 1] for i in range(1, len(a))]
        safe = is_safe(report)
        levels.append(safe)

    return sum(levels)


answer_test = part1(DATA_TEST) == 2
answer = part1(DATA) == 332

print("Part 1: ", answer_test, answer)

# Part 2


def is_safe_part2(a):
    report = [a[i] - a[i - 1] for i in range(1, len(a))]
    safe = is_safe(report)

    if not safe:
        for i in range(0, len(a)):
            b = a[:i] + a[i + 1 :]
            report = [b[i] - b[i - 1] for i in range(1, len(b))]
            safe = is_safe(report)
            if safe:
                break
    return safe


def part2(data_path: pathlib.Path):
    data = read_file(data_path)
    safe_reports = 0

    for a in data:
        safe = is_safe_part2(a)
        safe_reports += 1 if safe else 0

    return safe_reports


answer_test = part2(DATA_TEST) == 4
answer = part2(DATA) == 398

print("Part 2: ", answer_test, answer)
