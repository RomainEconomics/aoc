export {}

const pathTest = '2023/day_02/data/input_test.txt'
const path = '2023/day_02/data/input.txt'


const maxBag = {
    "red": 12,
    "green": 13,
    "blue": 14
}

// Part 1

function checkBag(line: string) {

    const splitLine = line.split(":")
    const gameID = parseInt(splitLine[0].split(" ")[1])

    const cubes = splitLine[1].trim().split(";")

    for (let i = 0; i < cubes.length; i++) {
        const cube = cubes[i].trim().split(",")
        for (let j = 0; j < cube.length; j++) {
            const cleanCube = cube[j].trim().split(" ")
            const value = parseInt(cleanCube[0])
            const color = cleanCube[1].trim()
            if (value > maxBag[color]) return 0 
        }
    }
    return gameID
}

async function part1(dataPath: string) {

    const file = Bun.file(dataPath);
    const data = await file.text();
    const lines = data.split('\n')

    let output = 0

    for (let i = 0; i < lines.length; i++) {
        const line = lines[i];
        output += checkBag(line)
    }

    return output
}   


const answerTest = await part1(pathTest) === 8
const answer = await part1(path) === 1734

console.log("Part 1:", answerTest, answer)


// Part 2


function computeLinePower(line: string) {

    let minBag = {
        "red": 0,
        "green": 0,
        "blue": 0
    }

    const splitLine = line.split(":")

    const cubes = splitLine[1].trim().split(";")

    for (let i = 0; i < cubes.length; i++) {
        const cube = cubes[i].trim().split(",")
        for (let j = 0; j < cube.length; j++) {
            const cleanCube = cube[j].trim().split(" ")
            const value = parseInt(cleanCube[0])
            const color = cleanCube[1].trim()

            minBag[color] = Math.max(value, minBag[color])
        }
    }

    let output = 1
    
    for (const color in minBag) {
        output *= minBag[color]
    }

    return output
}


async function part2(dataPath: string) {

    const file = Bun.file(dataPath);
    const data = await file.text();
    const lines = data.split('\n')

    let output = 0

    for (let i = 0; i < lines.length; i++) {
        const line = lines[i];
        output += computeLinePower(line)
    }

    return output
}

const answerTest2 = await part2(pathTest) === 2286
const answer2 = await part2(path) === 70387

console.log("Part 2:", answerTest2, answer2)