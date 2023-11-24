
from functools import reduce
import pathlib

path = pathlib.Path(__file__)
DATA_FOLDER = path.parent.parent / "data"

DATA_TEST =   DATA_FOLDER / "input_test.txt"
DATA = DATA_FOLDER / "input.txt"

def read_file(file_path: pathlib.Path):
    data = []
    with open(file_path) as f:
        data.extend(i.strip() * 100 for i in f)
        return data 

def toboggan(data: list[list[str]], move_x: int, move_y: int) -> int:

    x, y = 0, 0 
    tree = 0

    x, y = x + move_x, y + move_y

    while x < len(data[0]) and y < len(data):
        value = data[y][x]
        if value == "#":
            tree += 1 
        x += move_x
        y += move_y
    return tree

data_test = read_file(DATA_TEST)
data = read_file(DATA)

# Part 1

answer_test = toboggan(data_test, move_x=3, move_y=1) == 7
answer = toboggan(data, move_x=3, move_y=1) == 195

print("Part 1: ", answer_test, answer)


# Part 2

slopes = [
    {"move_x": 1, "move_y": 1},
    {"move_x": 3, "move_y": 1},
    {"move_x": 5, "move_y": 1},
    {"move_x": 7, "move_y": 1},
    {"move_x": 1, "move_y": 2},
]

answer_test = reduce(lambda x, y: x*y, [toboggan(data_test, **i) for i in slopes]) == 336
answer= reduce(lambda x, y: x*y, [toboggan(data, **i) for i in slopes]) == 3772314000

print("Part 2: ", answer_test, answer)
