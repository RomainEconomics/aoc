
// extern crate regex;
use regex::Regex;
use std::collections::hash_map::HashMap;

pub fn part2(contents: &String) -> i32 {

    let mut map = HashMap::new();
    map.insert("one", "1");
    map.insert("two", "2");
    map.insert("three", "3");
    map.insert("four", "4");
    map.insert("five", "5");
    map.insert("six", "6");
    map.insert("seven", "7");
    map.insert("eight", "8");
    map.insert("nine", "9");

    let re: Regex = Regex::new(r"(\d|one|two|three|four|five|six|seven|eight|nine)").unwrap();

    let digits = contents
        .lines()
        .map(|line| {
            // In python, we can use `(?=...)` to match a pattern without consuming it, allowing to match overlapping patterns.
            // In rust, I'm not sure it possible. An alternative is to use a loop to find all matches, but keeping only the match starting at the current index.
            let mut x = Vec::new();
            for (i, _) in line.char_indices() {
                if let Some(mat) = re.find(&line[i..]) {
                    if mat.start() == 0 {
                        x.push(mat.as_str());
                    }
                }
            }

            let first = map.get(x[0]).unwrap_or(&x[0]);
            let last = map.get(x[x.len() - 1]).unwrap_or(&x[x.len() - 1]);
            
            let num = first.to_string() + &last.to_string();
            num.parse::<i32>().unwrap()
        })
        .collect::<Vec<_>>();
        
    digits.iter().sum::<i32>()

}


#[cfg(test)]
mod tests {
    use std::fs;

    use super::*;

    #[test]
    fn test_part2_test() {
        let contents: String = "two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen".to_string();
        assert_eq!(part2(&contents), 281);
    }

    #[test]
    fn test_part2_test2() {
        let contents: String = "9eighthvxnlvthqjtpsjnleightwokq".to_string();
        assert_eq!(part2(&contents), 92);
    }

    #[test]
    fn test_part2() {
        let contents: String = fs::read_to_string("../data/input.txt").unwrap();
        assert_eq!(part2(&contents), 54980);
    }
}