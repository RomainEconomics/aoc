

async function part1(dataPath: string) {
    const file = Bun.file(dataPath);
    const data = await file.text();
    const lines = data.split('\n')
    
    const regex: RegExp = /\d/g

    let sum = 0
    for (let i = 0; i < lines.length; i++) {
        const line = lines[i]
        const digits = line.match(regex)
        const calibration_value = parseInt(digits[0] + digits[digits.length - 1])
        sum += calibration_value
    }
    return sum
}


const pathTest = '2023/day_01/data/input_test.txt'
const pathTest2 = '2023/day_01/data/input_test_part2.txt'
const path = '2023/day_01/data/input.txt'

const answerTest = await part1(pathTest) === 142
const answer = await part1(path) === 55816

console.log(await part1(path))
console.log("Part 1:", answerTest, answer)

const digitMapping = {
    'zero': 0,
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4, 
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8, 
    'nine': 9,
}

async function part2(dataPath: string) {
    const file = Bun.file(dataPath);
    const data = await file.text();
    const lines = data.split('\n')
    
    const regex: RegExp = /(\d|zero|one|two|three|four|five|six|seven|eight|nine)/g
    
    let output = 0

    for (let i = 0; i < lines.length; i++) {
        const line = lines[i]
        const digits = line.match(regex)

        let first = digits[0]
        let last = digits[digits.length - 1]


        if (isNaN(parseInt(first))) {
            first = digitMapping[first]
        }

        if (isNaN(parseInt(last))) {
            last = digitMapping[last]
        }

        const calibration_value = parseInt(first + last)   
        output += calibration_value
    }

    return output
}

const answerTest2 = await part2(pathTest2) === 281
const answer2 = await part2(path) === 54980

console.log("Part 2:", answerTest2, answer2)





