import re
import pathlib
from itertools import groupby
from itertools import permutations

path = pathlib.Path(__file__)
DATA_FOLDER = path.parent.parent / "data"

DATA_TEST = DATA_FOLDER / "input_test.txt"
DATA = DATA_FOLDER / "input.txt"


def read_file(file_path: pathlib.Path) -> list[list[str]]:
    with open(file_path) as f:
        data = f.read().splitlines()
        return list(map(lambda x: x.split(), data))


cache = {}


def count(springs: str, nums: tuple):
    # See: https://www.youtube.com/watch?v=g3Ms5e7Jdqo

    if not springs:
        return 0 if nums else 1

    if not nums:
        return 0 if "#" in springs else 1

    keys = (springs, nums)

    if keys in cache:
        return cache[keys]

    result = 0

    if springs[0] in ".?":
        result += count(springs[1:], nums)

    if springs[0] in "#?" and (
        nums[0] <= len(springs)
        and "." not in springs[: nums[0]]
        and (nums[0] == len(springs) or springs[nums[0]] != "#")
    ):
        result += count(springs[nums[0] + 1 :], nums[1:])

    cache[keys] = result

    return result


# part1(DATA_TEST)

# Part 1


def part1(data_path: pathlib.Path):
    data = read_file(data_path)

    arrangements = 0

    for springs, nums in data:
        nums = tuple(map(int, nums.split(",")))

        print(springs, nums)

        arrangements += count(springs, nums)
    return arrangements


answer_test = part1(DATA_TEST) == 21
answer = part1(DATA) == 8270

print("Part 1: ", answer_test, answer)

# Part 2


def part2(data_path: pathlib.Path):
    data = read_file(data_path)

    arrangements = 0

    for springs, nums in data:
        new_row = "?".join([springs] * 5) + " " + ",".join([nums] * 5)
        new_springs, new_nums = new_row.split()
        nums = tuple(map(int, new_nums.split(",")))

        arrangements += count(new_springs, nums)
    return arrangements


answer_test = part2(DATA_TEST) == 525152
answer = part2(DATA) == 204640299929836

print("Part 2: ", answer_test, answer)
