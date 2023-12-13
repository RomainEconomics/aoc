
import pathlib

path = pathlib.Path(__file__)
DATA_FOLDER = path.parent.parent / "data"

DATA_TEST = DATA_FOLDER / "input_test.txt"
DATA = DATA_FOLDER / "input.txt"

def read_file(file_path: pathlib.Path):
    with open(file_path) as f:
        data = f.read().splitlines()
        return data 

data = read_file(DATA)

def format_data(file_path: pathlib.Path):
    data = read_file(file_path)
    return [
        [int(i) for i in line.split(" ")]
        for line in data
    ]

# Part 1

def part1(data_path: pathlib.Path):
    data = format_data(data_path)

    val = 0
    for line in data:
        new_data = [line]
        diff = line
        while any(i != 0 for i in diff):
            diff = [diff[idx] - diff[idx - 1] for idx in range(1, len(diff))]
            new_data.append(diff)
        sum_val = sum(i[-1] for i in new_data)
        val += sum_val
    return val

answer_test = part1(DATA_TEST) == 114
answer = part1(DATA) == 1731106378

print("Part 1: ", answer_test, answer)

# Part 2

def part2(data_path: pathlib.Path):
    data = format_data(data_path)

    final_val = 0
    for line in data:
        new_data = [line]
        diff = line

        while any(i != 0 for i in diff):
            diff = [diff[idx] - diff[idx - 1] for idx in range(1, len(diff))]
            new_data.append(diff)

        val = new_data[-1][0]
        for i in list(reversed(range(len(new_data)-1))):
            val = new_data[i][0] - val

        final_val += val
    return final_val

answer_test = part2(DATA_TEST) == 2
answer = part2(DATA) == 1087

print("Part 2: ", answer_test, answer)
