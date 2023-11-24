
import pathlib

path = pathlib.Path(__file__)
DATA_FOLDER = path.parent.parent / "data"

DATA_TEST =   DATA_FOLDER / "input_test.txt"
DATA = DATA_FOLDER / "input.txt"

def read_file(file_path: pathlib.Path):
    with open(file_path) as f:
        return f.read().splitlines() 

def convert_bin_to_int(s: str, to_zero: str, to_one: str) -> str:
    b = s.replace(to_zero, "0").replace(to_one, "1")
    return int(b, 2)

def parse_data(data) -> list:
    items = []
    for item in data:
        row = convert_bin_to_int(item[:-3], "F", "B")
        col = convert_bin_to_int(item[-3:], "L", "R")
        items.append(row * 8 + col)
    return items

# Part 1

def part1(data_path: pathlib.Path):
    data = read_file(data_path)
    items = parse_data(data)
    return max(items)

answer_test = part1(DATA_TEST) == 357
answer= part1(DATA) == 974

print("Part 1:", answer_test, answer)


# Part 2

def part2(data_path: pathlib.Path) -> int:
    data = read_file(data_path)
    items = parse_data(data)
    items.sort()

    for i in range(len(items)-1):
        if items[i+1] - items[i] != 1:
            return items[i] + 1



answer = part2(DATA) == 646
print("Part 2:", answer)



