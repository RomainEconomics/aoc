pub fn part1(contents: &str) -> i32 {
    contents
        .lines()
        .map(|line| {
            let reports = line
                .split_whitespace()
                .map(|x| x.parse::<i32>().unwrap())
                .collect::<Vec<i32>>();
            is_sorted(&reports) as i32
        })
        .sum::<i32>()
}

pub fn is_sorted(reports: &[i32]) -> bool {
    let increasing = reports[1] > reports[0];

    reports.windows(2).all(|pair| {
        let diff = pair[1] - pair[0];
        !((increasing && diff <= 0) || (!increasing && diff >= 0) || diff.abs() > 3)
    })
}

#[cfg(test)]
mod tests {
    use std::fs;

    use super::*;

    #[test]
    fn test_part1_test() {
        let contents: String = fs::read_to_string("../data/input_test.txt").unwrap();
        assert_eq!(part1(&contents), 2);
    }

    #[test]
    fn test_part1() {
        let contents: String = fs::read_to_string("../data/input.txt").unwrap();
        assert_eq!(part1(&contents), 332);
    }
}
