use crate::part1::is_sorted;

pub fn part2(contents: &str) -> i32 {
    contents
        .lines()
        .map(|line| {
            let reports = line
                .split_whitespace()
                .map(|x| x.parse::<i32>().unwrap())
                .collect::<Vec<i32>>();

            match is_sorted(&reports) {
                true => 1,
                false => retry(&reports) as i32,
            }
        })
        .sum::<i32>()
}

fn retry(reports: &[i32]) -> bool {
    let mut retry_report = Vec::with_capacity(reports.len() - 1);

    (0..reports.len()).any(|i| {
        retry_report.clear();
        retry_report.extend_from_slice(&reports[..i]);
        retry_report.extend_from_slice(&reports[i + 1..]);

        is_sorted(&retry_report)
    })
}

#[cfg(test)]
mod tests {
    use std::fs;

    use super::*;

    #[test]
    fn test_part2_test() {
        let contents: String = fs::read_to_string("../data/input_test.txt").unwrap();
        assert_eq!(part2(&contents), 4);
    }

    #[test]
    fn test_part2() {
        let contents: String = fs::read_to_string("../data/input.txt").unwrap();
        assert_eq!(part2(&contents), 398);
    }
}
