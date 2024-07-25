use crate::part1::{calculate_score, move_rocks};
use std::collections::HashMap;

fn transpose(data: Vec<Vec<char>>) -> Vec<Vec<char>> {
    let rows = data.len();
    let cols = data[0].len();

    (0..cols)
        .map(|col| (0..rows).map(|row| data[row][col]).collect())
        .collect()
}

fn cycle(mut data: Vec<Vec<char>>) -> Vec<Vec<char>> {
    for _ in 0..4 {
        data = move_rocks(data);
        data.reverse();
        data = transpose(data)
    }

    return data;
}

pub fn part2(contents: &String, n: usize) -> usize {
    let mut data: Vec<Vec<char>> = contents
        .lines()
        .map(|line| line.chars().collect::<Vec<_>>())
        .collect();

    let mut cache: HashMap<Vec<Vec<char>>, usize> = HashMap::new();

    for i in 0..n {
        if cache.contains_key(&data) {
            let cycle_start = cache.get(&data).unwrap();
            let cycle_length = i - cycle_start;
            let remaining = (n - i) % cycle_length;
            for _ in 0..remaining {
                data = cycle(data);
            }
            break;
        }

        cache.insert(data.clone(), i);
        data = cycle(data);
    }

    calculate_score(data)
}

#[cfg(test)]
mod tests {
    use super::*;
    use std::fs;

    #[test]
    fn test_part2_test() {
        let contents: String = fs::read_to_string("../data/input_test.txt").unwrap();
        assert_eq!(part2(&contents, 1000000000), 64);
    }

    #[test]
    fn test_part2() {
        let contents: String = fs::read_to_string("../data/input.txt").unwrap();
        assert_eq!(part2(&contents, 1000000000), 90982);
    }
}
