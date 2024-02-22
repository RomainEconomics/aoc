
extern crate regex;
use regex::Regex;

pub fn part1(contents: &String) -> i32 {
    let re = Regex::new(r"\d").unwrap();
    
    let digits: Vec<i32> = contents
        .lines()
        .map( |line| {
            let x: String = re.find_iter(line)
                .map(|match_| match_.as_str())
                .collect::<Vec<_>>()
                .join("");
            let first: char = x.chars().next().unwrap();
            let last: char = x.chars().last().unwrap();
            let num: String = first.to_string() + &last.to_string();
            
            num.parse::<i32>().unwrap()
        }
        )
        .collect::<Vec<_>>();

    digits.iter().sum::<i32>()
}


#[cfg(test)]
mod tests {
    use std::fs;

    use super::*;

    #[test]
    fn test_part1_test() {
        let contents: String = "1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet".to_string();
        assert_eq!(part1(&contents), 142);
    }


    #[test]
    fn test_part1() {
        let contents: String = fs::read_to_string("../data/input.txt").unwrap();
        assert_eq!(part1(&contents), 55816);
    }
}