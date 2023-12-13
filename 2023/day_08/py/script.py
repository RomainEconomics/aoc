import re
from math import lcm
from collections import OrderedDict
import pathlib

path = pathlib.Path(__file__)
DATA_FOLDER = path.parent.parent / "data"

DATA_TEST = DATA_FOLDER / "input_test.txt"
DATA_TEST_P2 = DATA_FOLDER / "input_test_p2.txt"
DATA = DATA_FOLDER / "input.txt"

def read_file(file_path: pathlib.Path):
    with open(file_path) as f:
        data = f.read().splitlines()
        return data 


def extract_nodes(data_path: pathlib.Path):
    data = read_file(data_path)
    data = iter(data)

    instructions = next(data)

    next(data)

    d = OrderedDict()

    for line in data:
        node, option1, option2 = re.findall(r"\w{3}", line)
        d[node] = (option1, option2)

    return instructions, d


# Part 1

def part1(data_path: pathlib.Path):
    instructions, d = extract_nodes(data_path)
    node = "AAA"

    idx_instruct = 0
    steps = 0
    while node != "ZZZ":
        option1, option2 = d[node]
        node = option2 if instructions[idx_instruct] == "R" else option1

        idx_instruct = (idx_instruct + 1) % len(instructions)
        steps += 1
    return steps

answer_test = part1(DATA_TEST) == 6
answer = part1(DATA) == 16409

print("Part 1: ", answer_test, answer)

# Part 2

def part2(data_path: pathlib.Path):

    instructions, d = extract_nodes(data_path)
    nodes = [k for k in d.keys() if k.endswith("A")]

    idx_instruct = 0
    steps = 1
    final_nodes = [0 for _ in nodes]

    while not all(bool(i) for i in final_nodes):
        new_nodes = []
        for idx, node in enumerate(nodes):
            option1, option2 = d[node]
            node = option2 if instructions[idx_instruct] == "R" else option1

            new_nodes.append(node)

            if node.endswith("Z"):
                final_nodes[idx] = steps
        
        idx_instruct = (idx_instruct + 1) % len(instructions)
        steps += 1

        nodes = new_nodes

    return lcm(*final_nodes)

answer_test = part2(DATA_TEST) == 6
answer = part2(DATA) == 11795205644011

print("Part 2: ", answer_test, answer)
