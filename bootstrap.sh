#!/bin/bash

python_code=$(cat <<- END

import pathlib

path = pathlib.Path(__file__)
DATA_FOLDER = path.parent.parent / "data"

DATA_TEST = DATA_FOLDER / "input_test.txt"
DATA = DATA_FOLDER / "input.txt"

def read_file(file_path: pathlib.Path):
    with open(file_path) as f:
        data = f.read().splitlines()
        return data 

data = read_file(DATA_TEST)


# Part 1

def part1(data_path: pathlib.Path):
    data = read_file(data_path)
    return 0

# answer_test = part1(DATA_TEST) == 0
# answer = part1(DATA) == 0

# print("Part 1: ", answer_test, answer)

# Part 2

def part2(data_path: pathlib.Path):
    data = read_file(data_path)
    return 0

# answer_test = part2(DATA_TEST) == 0
# answer = part2(DATA) == 0

# print("Part 2: ", answer_test, answer)

END

)


ts_code() {
    code=$(cat <<- END
export {}

const pathTest = '2023/day_$1/data/input_test.txt'
const path = '2023/day_$1/data/input.txt'

const file = Bun.file(pathTest);
const data = await file.text();
const lines = data.split('\n')

console.log(lines)

// Part 1

async function part1(dataPath: string) {
    const file = Bun.file(dataPath);
    const data = await file.text();
    const lines = data.split('\n')
    
    return 0
}


// const answerTest = await part1(pathTest) === 0
// const answer = await part1(path) === 0

// console.log("Part 1:", answerTest, answer)


// Part 2

async function part2(dataPath: string) {
    const file = Bun.file(dataPath);
    const data = await file.text();
    const lines = data.split('\n')

    return 0
}

// const answerTest2 = await part2(pathTest2) === 0
// const answer2 = await part2(path) == 0

// console.log("Part 2:", answerTest2, answer2)

END
)
    printf "%s" "$code"
}




mkdir $1
cd $1

for i in {01..25}; do
    
    folder="day_$i"
    
    mkdir $folder
    cd $folder
    
    mkdir data
    cd data
    touch input.txt input_test.txt
    cd ..
    
    mkdir py go ts
    for j in py go ts; do
        cd $j
        touch script.$j
        if [ $j == "py" ]; then
            echo "$python_code" > script.$j
        fi

        if [ $j == "ts" ]; then
            echo "$(ts_code $i)" > script.$j
        fi

        cd ..
    done
    
    cd ..
done