export {}

const pathTest = '2023/day_08/data/input_test.txt'
const path = '2023/day_08/data/input.txt'

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
