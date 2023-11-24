
import pathlib
import re
from dataclasses import dataclass

path = pathlib.Path(__file__)
DATA_FOLDER = path.parent.parent / "data"

DATA_TEST =   DATA_FOLDER / "input_test.txt"
DATA = DATA_FOLDER / "input.txt"

def read_file(file_path: pathlib.Path):
    with open(file_path) as f:
        data = []
        passport_data = ""
        for line in f:
            line = line.strip()
            if line == "":
                data.append(passport_data.strip())
                passport_data = ""
                continue
            passport_data += f" {line}"
        return data 

def parse_passport(raw_passports: list[str]) -> list[dict]:
    clean_passports = []
    for passport in raw_passports:
        split = passport.split(" ")
        split_kv = [i.split(":") for i in split]
        clean_passport = dict(split_kv)
        clean_passports.append(clean_passport)
    return clean_passports

def is_valid(passport: dict, required_fields: set) -> bool:
    return all(field in passport for field in required_fields)

def part1(data_path: pathlib.Path) -> int:
    data = read_file(data_path)

    passports = parse_passport(data)
    fields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"} 
    return sum(is_valid(p, fields) for p in passports)

# Part 1

answer_test = part1(DATA_TEST)
answer= part1(DATA)

print("Part 1: ", answer_test, answer)


# Part 2


@dataclass
class Passport:
    byr: str
    iyr: str
    eyr: str
    hgt: str
    hcl: str
    ecl: str
    pid: str
    cid: str | None = None

    def __post_init__(self):
        if not (1920 <= int(self.byr) <= 2002):
            raise ValueError(f"Byr incorrect: {self.byr}")

        if not (2010 <= int(self.iyr) <= 2020):
            raise ValueError(f"iyr incorrect: {self.iyr}")
        
        if not (2020 <= int(self.eyr) <= 2030):
            raise ValueError(f"Eyr incorrect: {self.eyr}")

        val = int(self.hgt[:-2])
        match self.hgt[-2:]:
            case "cm":
                if not (150 <= val <= 193):
                    raise ValueError(f"Bad HGT: {val}")
            case "in":
                if not (59 <= val <= 76):
                    raise ValueError(f"Bad HGT: {val}")
            case _:
                raise ValueError(f"No in or cm defined: {self.hgt}")

        if not self.hcl.startswith("#"):
            raise ValueError("Missing # for hcl")
        
        if len(self.hcl[1:]) != 6:
            raise ValueError("Need exactly 6 values for hcl.")
        
        valid_hcl = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"}
        for val in tuple(self.hcl[1:]):
            if val not in valid_hcl: 
                raise ValueError(f"Bad character in hcl: {self.hcl}")
            
        valid_ecl = {"amb", "blu", "brn", "gry", "grn", "hzl","oth"}
        if self.ecl not in valid_ecl:
            raise ValueError(f"Bad value for ecl: {self.ecl}")

        if not re.fullmatch(r"\d{9}", self.pid):
            raise ValueError(f"Bad value for pid: {self.pid}")


def part2(data_path: pathlib.Path) -> int:
    data = read_file(data_path)
    passports = parse_passport(data)

    valid_passport = 0
    for passport in passports:
        try:
            Passport(**passport)
            valid_passport += 1
        except Exception as e:
            pass
    return valid_passport



answer = part2(DATA) == 130
print("Part 2: ", answer)