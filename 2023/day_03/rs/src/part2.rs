use regex::Regex;

fn find_stars(lines: &Vec<String>) -> Vec<(i32, i32)> {
    let mut stars: Vec<(i32, i32)> = Vec::new();

    for (row_idx, line) in lines.iter().enumerate() {
        for (col_idx, c) in line.chars().enumerate() {
            if c == '*' {
                stars.push((row_idx as i32, col_idx as i32));
            }
        }
    }

    stars
}

fn find_horizontal_adjacent_num(
    mut adj_nums: Vec<i32>,
    re: &Regex,
    lines: &Vec<String>,
    row_idx: usize,
    col_idx: usize,
) -> Vec<i32> {
    for digit_match in re.find_iter(&lines[row_idx]) {
        let start = if digit_match.start() == 0 {
            0
        } else {
            digit_match.start() - 1
        };
        if (col_idx == digit_match.end() as usize) || (col_idx == start as usize) {
            let val = digit_match.as_str().parse::<i32>().unwrap();
            adj_nums.push(val)
        }
    }
    adj_nums
}

fn find_vertical_adjacent_num(
    mut adj_nums: Vec<i32>,
    re: &Regex,
    lines: &Vec<String>,
    row_idx: usize,
    col_idx: usize,
) -> Vec<i32> {
    if row_idx != 0 {
        for digit_match in re.find_iter(&lines[row_idx - 1]) {
            let start = if digit_match.start() > 0 {
                digit_match.start() - 1
            } else {
                0
            };
            let end = if digit_match.end() != lines[0].len() {
                digit_match.end() + 1
            } else {
                digit_match.end()
            };
            if (start..end).contains(&col_idx) {
                let val = digit_match.as_str().parse::<i32>().unwrap();
                adj_nums.push(val)
            }
        }
    }

    if row_idx != lines[0].len() - 1 {
        for digit_match in re.find_iter(&lines[row_idx + 1]) {
            let start = if digit_match.start() > 0 {
                digit_match.start() - 1
            } else {
                0
            };
            let end = if digit_match.end() != lines[0].len() {
                digit_match.end() + 1
            } else {
                digit_match.end()
            };
            if (start..end).contains(&col_idx) {
                let val = digit_match.as_str().parse::<i32>().unwrap();
                adj_nums.push(val)
            }
        }
    }
    adj_nums
}

pub fn part2(contents: &String) -> i32 {
    let lines = contents
        .lines()
        .map(|s| s.to_string())
        .collect::<Vec<String>>();
    let stars = find_stars(&lines);
    let mut sum = 0;

    let re = Regex::new(r"(\d+)").unwrap();
    for star in stars {
        let mut adj_nums = Vec::<i32>::new();
        adj_nums =
            find_horizontal_adjacent_num(adj_nums, &re, &lines, star.0 as usize, star.1 as usize);
        adj_nums =
            find_vertical_adjacent_num(adj_nums, &re, &lines, star.0 as usize, star.1 as usize);

        if adj_nums.len() == 2 {
            sum += adj_nums[0] * adj_nums[1]
        }
    }
    sum
}

#[cfg(test)]
mod tests {
    use super::*;
    use std::fs;

    #[test]
    fn test_part2_test() {
        let contents: String = fs::read_to_string("../data/input_test.txt").unwrap();
        assert_eq!(part2(&contents), 467835);
    }

    #[test]
    fn test_part2() {
        let contents: String = fs::read_to_string("../data/input.txt").unwrap();
        assert_eq!(part2(&contents), 73646890);
    }
}
