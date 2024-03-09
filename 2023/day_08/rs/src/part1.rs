use std::collections::HashMap;

pub fn part1(contents: &str) -> usize {
    let data: Vec<_> = contents.split("\n\n").collect();
    let seq: Vec<_> = data[0].chars().collect();

    let mut node = "AAA";
    let end = "ZZZ";

    let mut steps = 0;

    let hash: HashMap<&str, (&str, &str)> = data[1]
        .split("\n")
        .map(|line| {
            let (src, dest) = line.split_once(" = ").unwrap();
            let (left, right) = dest.split_once(", ").unwrap();
            (src, (&left[1..], &right[0..(right.len() - 1)]))
        })
        .collect();

    while node != end {
        let (left, right) = hash[&node];
        let direction = seq[steps % seq.len()];

        steps += 1;
        node = if direction == 'L' { left } else { right };
    }
    steps
}

#[cfg(test)]
mod tests {
    use super::*;
    use std::fs;

    #[test]
    fn test_part1_test() {
        let contents: String = fs::read_to_string("../data/input_test.txt").unwrap();
        assert_eq!(part1(&contents), 6);
    }

    #[test]
    fn test_part1() {
        let contents: String = fs::read_to_string("../data/input.txt").unwrap();
        assert_eq!(part1(&contents), 16409);
    }
}
