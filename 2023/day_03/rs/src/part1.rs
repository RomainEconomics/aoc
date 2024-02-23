// extern crate regex;
use regex::Regex;

fn find_adjacent_symbol(
    grid: &Vec<String>,
    line: &str,
    neighbors: &Vec<(i32, i32)>,
    grid_count: &usize,
    digit_match: regex::Match,
    row_idx: usize,
) -> i32 {
    let start_idx = digit_match.start();
    let end_idx = digit_match.end();
    let value = digit_match.as_str().parse::<i32>().unwrap();

    for idx in start_idx..end_idx {
        for neighbor in neighbors.iter() {
            let adj_col = idx as i32 + neighbor.0;
            let adj_row = row_idx as i32 + neighbor.1;
            if (0 <= adj_col)
                && (adj_col < line.len() as i32)
                && (0 <= adj_row)
                && (adj_row < *grid_count as i32)
            {
                let adj_value = grid[adj_row as usize]
                    .chars()
                    .nth(adj_col as usize)
                    .unwrap();
                if (!adj_value.is_digit(10)) && (adj_value != '.') {
                    return value;
                }
            }
        }
    }

    0
}

pub fn part1(contents: &String) -> i32 {
    let neighbors: Vec<(i32, i32)> = vec![
        (0, 1),
        (1, 0),
        (0, -1),
        (-1, 0),
        (1, 1),
        (-1, -1),
        (1, -1),
        (-1, 1),
    ];
    let mut sum = 0;

    let re = Regex::new(r"(\d+)").unwrap();

    let grid: Vec<String> = contents.lines().map(|s| s.to_string()).collect();
    let grid_count: usize = grid.len();

    grid.iter().enumerate().for_each(|(row_idx, line)| {
        for digit_match in re.find_iter(line) {
            sum += find_adjacent_symbol(&grid, line, &neighbors, &grid_count, digit_match, row_idx)
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
        assert_eq!(part1(&contents), 4361);
    }

    #[test]
    fn test_part1() {
        let contents: String = fs::read_to_string("../data/input.txt").unwrap();
        assert_eq!(part1(&contents), 531932);
    }
}
