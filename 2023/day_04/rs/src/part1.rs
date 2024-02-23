use std::collections::HashSet;

use regex::Regex;

pub fn process_line(line: &str) -> (HashSet<i32>, HashSet<i32>) {
    let re: Regex = Regex::new(r"(\d+)").unwrap();
    let parts: Vec<&str> = line.split("|").collect::<Vec<&str>>();

    let winning_nums: HashSet<i32> = re
        .find_iter(parts[0])
        .map(|x| x.as_str().parse::<i32>().unwrap())
        .skip(1)
        .collect();
    let my_nums: HashSet<i32> = re
        .find_iter(parts[1])
        .map(|x| x.as_str().parse::<i32>().unwrap())
        .collect();

    (winning_nums, my_nums)
}

pub fn part1(contents: &String) -> i32 {
    let mut sum: i32 = 0;

    contents.lines().for_each(|line| {
        let (winning_nums, my_nums) = process_line(line);
        let winning_cards: usize = winning_nums
            .intersection(&my_nums)
            .collect::<HashSet<&i32>>()
            .len();

        if winning_cards != 0 {
            sum += 2_i32.pow(((winning_cards - 1) as i32).try_into().unwrap());
        }
    });

    sum
}

#[cfg(test)]
mod tests {
    use super::*;
    use std::fs;

    #[test]
    fn test_part1_test() {
        let contents: String = fs::read_to_string("../data/input_test.txt").unwrap();
        assert_eq!(part1(&contents), 13);
    }

    #[test]
    fn test_part1() {
        let contents: String = fs::read_to_string("../data/input.txt").unwrap();
        assert_eq!(part1(&contents), 23847);
    }
}
