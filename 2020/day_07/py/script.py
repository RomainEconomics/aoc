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


def parse_line(line: str):
    outermost_bag, inside_bags = line.split(" contain ")

    return outermost_bag[:-1], inside_bags[:-1]  # remove "s" and "."


def find_outermost_bag(data, set_bag_pre: set, set_bag_post: set):
    for line in data:
        outermost_bag, inside_bags = parse_line(line)

        for b in set_bag_pre:
            if b in inside_bags:
                set_bag_post.add(outermost_bag)
    return set_bag_pre.union(set_bag_post), set_bag_pre


def part1(file_path: pathlib.Path) -> int:
    data: list[str] = read_file(file_path)

    target_bag = "shiny gold bag"
    set_bag_pre = set([target_bag])
    set_bag_post = set()

    while len(set_bag_pre) != len(set_bag_post):
        set_bag_pre, set_bag_post = find_outermost_bag(data, set_bag_pre, set_bag_post)

    return len(set_bag_pre) - 1


answer_test = part1(DATA_TEST) == 4
answer = part1(DATA) == 372

print("Part 1: ", answer_test, answer)

# Part 2


def create_bags(data: list[str]):
    bags = {}
    for line in data:
        outermost_bag, inside_bags = parse_line(line)

        bags[outermost_bag] = {}

        if "no other" in inside_bags:
            continue

        split_inside_bags = inside_bags.split(",")

        for inside_bag in split_inside_bags:
            bag_num, bag_name = inside_bag.strip().split(" ", 1)
            bag_name = bag_name[:-1] if bag_name[-1] == "s" else bag_name

            bags[outermost_bag][bag_name] = int(bag_num)
    return bags


def count_bag(bags, bag_name: str) -> int:
    if not bags[bag_name]:
        return 1

    local_value = 1
    for k, v in bags[bag_name].items():
        local_value += count_bag(bags, k) * v

    return local_value


def part2(file_path: pathlib.Path) -> int:
    data: list[str] = read_file(file_path)

    target_bag = "shiny gold bag"
    bags = create_bags(data)

    return count_bag(bags, target_bag) - 1


answer_test = part2(DATA_TEST) == 32
answer = part2(DATA) == 8015

print("Part 2: ", answer_test, answer)
