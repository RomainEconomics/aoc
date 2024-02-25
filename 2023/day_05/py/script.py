
import pathlib

path = pathlib.Path(__file__)
DATA_FOLDER = path.parent.parent / "data"

DATA_TEST = DATA_FOLDER / "input_test.txt"
DATA = DATA_FOLDER / "input.txt"

def read_file(file_path: pathlib.Path):
    with open(file_path) as f:
        return f.read().split("\n\n") 


# Part 1

def part1(data_path: pathlib.Path):
    data = read_file(data_path)

    seeds = list(map(int, data[0].split()[1:]))

    maps = []
    for x_to_y_map in data[1:]:
        sources = [list(map(int, x.split())) for x in x_to_y_map.split("\n")[1:] if x]
        maps.append(sources)

    for ranges in maps:

        new_seeds = []
        for x in seeds:
            for r in ranges:
                dest, source, range_len = r
        
                if source <= x < source + range_len:
                    new_seeds.append(x - source + dest)
                    break
            else:
                new_seeds.append(x)

        seeds = new_seeds

    return min(seeds)

answer_test: bool = part1(DATA_TEST) == 35
answer: bool = part1(DATA) == 403695602

print("Part 1: ", answer_test, answer)

# Part 2

def part2(data_path: pathlib.Path):
    data = read_file(data_path)

    seeds = list(map(int, data[0].split()[1:]))
    seeds = [(seeds[i], seeds[i] + seeds[i + 1]) for i in range(0, len(seeds), 2)]

    for x_to_y_map in data[1:]:
        sources = [list(map(int, x.split())) for x in x_to_y_map.split("\n")[1:] if x]

        new = []

        while seeds:
            start, end = seeds.pop(0)
            for r in sources:
                r_start, r_end, r_len = r
                # o: overlap
                os = max(start, r_end)
                oe = min(end, r_end + r_len)
                if os < oe:
                    new.append((os - r_end + r_start, oe - r_end + r_start))
                    if os > start:
                        seeds.append((start, os))
                    if oe < end:
                        seeds.append((oe, end))
                    break
            else:
                new.append((start, end))
        seeds = new

    return min(seeds)[0]

answer_test = part2(DATA_TEST) == 46
answer = part2(DATA) == 219529182

print("Part 2: ", answer_test, answer)
