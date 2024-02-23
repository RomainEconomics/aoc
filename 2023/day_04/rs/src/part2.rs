use crate::part1::process_line;

pub fn part2(contents: &String) -> i32 {
    let mut hash_map: std::collections::HashMap<usize, i32> = std::collections::HashMap::new();
    for i in 0..(contents.lines().count()) {
        hash_map.insert(i, 1);
    }

    contents.lines().enumerate().for_each(|(idx, line)| {
        let (winning_nums, my_nums) = process_line(line);
        let winning_cards: usize = winning_nums
            .intersection(&my_nums)
            .collect::<Vec<&i32>>()
            .len();
        for i in (idx + 1)..(idx + 1 + winning_cards) {
            let val = *hash_map.get(&idx).unwrap();
            hash_map.entry(i).and_modify(|e| *e += val);
        }
    });

    hash_map.values().sum::<i32>()
}

#[cfg(test)]
mod tests {
    use super::*;
    use std::fs;

    #[test]
    fn test_part2_test() {
        let contents: String = fs::read_to_string("../data/input_test.txt").unwrap();
        assert_eq!(part2(&contents), 30);
    }

    #[test]
    fn test_part2() {
        let contents: String = fs::read_to_string("../data/input.txt").unwrap();
        assert_eq!(part2(&contents), 8570000);
    }
}
