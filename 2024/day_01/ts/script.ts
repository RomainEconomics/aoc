export {};

const pathTest = "2024/day_01/data/input_test.txt";
const path = "2024/day_01/data/input.txt";

function parseFile(data: string) {
  const lines = data.split("\n");

  let l1: number[] = [];
  let l2: number[] = [];

  for (const line of lines.slice(0, -1)) {
    const s = line.split(/[ ]+/);
    l1.push(parseInt(s[0]));
    l2.push(parseInt(s[1]));
  }

  return { l1, l2 };
}

// Part 1

async function part1(dataPath: string) {
  const file = Bun.file(dataPath);
  const s = await file.text();

  const { l1, l2 } = parseFile(s);

  l1.sort();
  l2.sort();

  return l1.reduce((total_distance, current, idx) => {
    return total_distance + Math.abs(current - l2[idx]);
  }, 0);
}

const answerTest = (await part1(pathTest)) === 11;
const answer = (await part1(path)) === 3574690;

console.log("Part 1:", answerTest, answer);

// Part 2

async function part2(dataPath: string) {
  const file = Bun.file(dataPath);
  const s = await file.text();

  const { l1, l2 } = parseFile(s);

  const map = new Map<number, number>();

  return l1.reduce((similarityScore, current) => {
    if (!map.has(current)) {
      map.set(current, current * l2.filter((x) => x == current).length);
    }
    return similarityScore + map.get(current);
  }, 0);
}

const answerTest2 = (await part2(pathTest)) === 31;
const answer2 = (await part2(path)) == 22565391;

console.log("Part 2:", answerTest2, answer2);
