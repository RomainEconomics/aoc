

import pathlib

path = pathlib.Path(__file__)
DATA_FOLDER = path.parent.parent / "data"

DATA_TEST =   DATA_FOLDER / "input_test.txt"
DATA = DATA_FOLDER / "input.txt"

def read_file(file_path: pathlib.Path):
    with open(file_path) as f:
        return f.read().splitlines() 

# Part 1

def part1(data_path: pathlib.Path) -> int:

    data: list[str] = read_file(data_path)

    output = 0
    group = set()
    for x in data:
        group.update(set(x))
        if x == "":
            output += len(group)
            group = set()
    output += len(group)
    return output

answer_test = part1(DATA_TEST) == 11
answer= part1(DATA) == 6768


print("Part 1: ", answer_test, answer)


# Part 2

def part2(data_path: pathlib.Path) -> int:
    data = read_file(data_path)

    output = 0
    d: dict[str, int] = {}
    person_in_group = 0

    for x in data: 
        if x == "":
            output += sum(v == person_in_group for v in d.values())
            person_in_group = 0
            d = {}
        else:
            for s in x:
                d[s] = d.get(s, 0) + 1
            person_in_group += 1

    output += sum(v == person_in_group for v in d.values())
    return output

            
answer_test = part2(DATA_TEST) == 6
answer = part2(DATA) == 3489

print("Part 2: ", answer_test, answer)
