import pathlib

path = pathlib.Path(__file__)
DATA_FOLDER = path.parent.parent / "data"

DATA_TEST = DATA_FOLDER / "input_test.txt"
DATA = DATA_FOLDER / "input.txt"


def read_file(file_path: pathlib.Path):
    with open(file_path) as f:
        data = f.read().splitlines()
        return data


# Part 1


def part1(data_path: pathlib.Path) -> int:
    data: list[str] = read_file(data_path)

    idx, accumulator = 0, 0
    saved_idx = set()

    while idx < len(data):
        if idx in saved_idx:
            break
        else:
            saved_idx.add(idx)

        instruction: str = data[idx]
        operation, argument = instruction.split(" ")

        match operation:
            case "nop":
                idx += 1
                continue
            case "acc":
                idx += 1
                accumulator += (
                    int(argument[1:]) if "+" in argument else -int(argument[1:])
                )
            case "jmp":
                idx += int(argument[1:]) if "+" in argument else -int(argument[1:])
                continue
    return accumulator


answer_test: bool = part1(DATA_TEST) == 5
answer: bool = part1(DATA) == 1709

print("Part 1: ", answer_test, answer)

# Part 2


def part2(data_path: pathlib.Path) -> int:
    data: list[str] = read_file(data_path)

    idx, accumulator = 0, 0
    saved_idx = set()
    saved_change_command_idx = set()
    CHANGED_THAT_TURN = False

    while idx < len(data):
        if idx in saved_idx:
            CHANGED_THAT_TURN = False
            saved_idx = set()
            idx, accumulator = 0, 0
            continue
        else:
            saved_idx.add(idx)

        instruction: str = data[idx]
        operation, argument = instruction.split(" ")

        if (
            operation in {"nop", "jmp"}
            and not CHANGED_THAT_TURN
            and idx not in saved_change_command_idx
        ):
            CHANGED_THAT_TURN = True
            saved_change_command_idx.add(idx)
            operation = "nop" if operation == "jmp" else "jmp"

        match operation:
            case "nop":
                idx += 1
                continue
            case "jmp":
                idx += int(argument[1:]) if "+" in argument else -int(argument[1:])
            case "acc":
                idx += 1
                accumulator += (
                    int(argument[1:]) if "+" in argument else -int(argument[1:])
                )
    return accumulator


answer_test: bool = part2(DATA_TEST) == 8
answer: bool = part2(DATA) == 1976


print("Part 2: ", answer_test, answer)
