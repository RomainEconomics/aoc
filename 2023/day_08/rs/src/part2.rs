use std::collections::HashMap;

pub fn part2(contents: &String) -> i64 {
    let data: Vec<_> = contents.split("\n\n").collect();
    let seq: Vec<_> = data[0].chars().collect();

    let mut nodes = Vec::new();

    let hash: HashMap<&str, (&str, &str)> = data[1]
        .split("\n")
        .map(|line| {
            let (src, dest) = line.split_once(" = ").unwrap();
            let (left, right) = dest.split_once(", ").unwrap();

            if src.ends_with('A') {
                nodes.push(src);
            }

            (src, (&left[1..], &right[0..(right.len() - 1)]))
        })
        .collect();

    let mut node_steps = Vec::new();

    for node in nodes {
        let mut steps: i64 = 0;
        let mut current = node;

        while !current.ends_with('Z') {
            let direction = seq[(steps % seq.len() as i64) as usize];
            let (left, right) = hash.get(current).unwrap();

            current = if direction == 'L' { left } else { right };
            steps += 1;
        }

        node_steps.push(steps as usize);
    }

    node_steps
        .iter()
        .cloned()
        .reduce(|acc, x| lcm(acc, x))
        .unwrap() as i64
}

fn gcd(mut a: usize, mut b: usize) -> usize {
    if a == b {
        return a;
    }
    if b > a {
        let temp = a;
        a = b;
        b = temp
    }
    while b > 0 {
        let temp = a;
        a = b;
        b = temp % b
    }
    return a;
}

fn lcm(a: usize, b: usize) -> usize {
    return a * (b / gcd(a, b));
}

#[cfg(test)]
mod tests {
    use super::*;
    use std::fs;

    #[test]
    fn test_part2_test() {
        let contents: String = fs::read_to_string("../data/input_test_p2.txt").unwrap();
        assert_eq!(part2(&contents), 6);
    }

    #[test]
    fn test_part2() {
        let contents: String = fs::read_to_string("../data/input.txt").unwrap();
        assert_eq!(part2(&contents), 11795205644011);
    }
}
