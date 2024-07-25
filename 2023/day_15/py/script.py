import pathlib
from functools import reduce

path = pathlib.Path("__file__")
DATA_FOLDER = path.parent.parent / "data"

DATA_TEST = DATA_FOLDER / "input_test.txt"
DATA = DATA_FOLDER / "input.txt"


def read_file(file_path: pathlib.Path):
    with open(file_path, "rb") as f:
        data = f.read().strip().split(b",")
        return data


# Part 1


def compute_hash(s: bytes):
    return reduce(lambda x, y: ((x + y) * 17) % 256, s, 0)


def part1(data_path: pathlib.Path):
    data = read_file(data_path)
    return sum(compute_hash(s) for s in data)


answer_test = part1(DATA_TEST) == 1320
answer = part1(DATA) == 510013

print("Part 1: ", answer_test, answer)

# Part 2


def hashmap(data):
    boxes = [{} for _ in range(256)]

    for s in data:
        match s.strip(b"-").split(b"="):
            case [label, value]:
                boxes[compute_hash(label)][label] = int(value)
            case [label]:
                boxes[compute_hash(label)].pop(label, None)

    return boxes


def part2(data_path: pathlib.Path):
    data = read_file(data_path)

    return sum(
        box_id * slot * focal
        for box_id, box in enumerate(hashmap(data), start=1)
        for slot, focal in enumerate(box.values(), start=1)
    )


answer_test = part2(DATA_TEST) == 145
answer = part2(DATA) == 268497

print("Part 2: ", answer_test, answer)
