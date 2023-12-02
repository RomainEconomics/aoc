from collections import abc
from copy import deepcopy
from enum import Enum
from itertools import product
import pathlib

path = pathlib.Path(__file__)
DATA_FOLDER = path.parent.parent / "data"

DATA_TEST = DATA_FOLDER / "input_test.txt"
DATA = DATA_FOLDER / "input.txt"


def read_file(file_path: pathlib.Path):
    with open(file_path) as f:
        data = f.read().splitlines()
        return [list(i) for i in data]


class Position(str, Enum):
    FLOOR = "."
    EMPTY_SEAT = "L"
    OCCUPIED_SEAT = "#"


# Part 1


data: list[list[str]] = read_file(DATA)


def get_occupied_seats(seats: list[list[str]]) -> int:
    occupied_seats = 0
    for row in seats:
        for el in row:
            if el == Position.OCCUPIED_SEAT.value:
                occupied_seats += 1
    return occupied_seats


def part1(data_path: pathlib.Path) -> int:
    data = read_file(data_path)

    X: int = len(data[0]) - 1
    Y: int = len(data) - 1

    neighbors = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))

    while True:
        new_round: list[list[str]] = [[i for i in row] for row in data]

        for x, y in product(range(X + 1), range(Y + 1)):
            seat_position: tuple[int, int] = (x, y)
            seat_value: str = data[y][x]

            if seat_value == Position.FLOOR.value:
                continue

            around_values: list[str] = [
                data[y + seat_position[1]][x + seat_position[0]]
                for x, y in neighbors
                if 0 <= x + seat_position[0] <= X and 0 <= y + seat_position[1] <= Y
            ]

            if Position.OCCUPIED_SEAT.value not in around_values:
                new_round[y][x] = Position.OCCUPIED_SEAT.value

            if seat_value == Position.OCCUPIED_SEAT.value:
                occupied_seats = (
                    True if seat == Position.OCCUPIED_SEAT.value else False
                    for seat in around_values
                )
                if sum(occupied_seats) >= 4:
                    new_round[y][x] = Position.EMPTY_SEAT.value

        if data == new_round:
            return get_occupied_seats(new_round)

        data = new_round


answer_test = part1(DATA_TEST) == 37
answer = part1(DATA) == 2424

print("Part 1", answer_test, answer)

# Part 2
