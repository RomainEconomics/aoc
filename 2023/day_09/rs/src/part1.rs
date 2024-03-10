pub fn part1(contents: &str) -> i64 {
    let data: Vec<Vec<i64>> = contents
        .lines()
        .map(|line| {
            line.split(' ')
                .map(|x| x.parse::<i64>().unwrap())
                .collect::<Vec<i64>>()
        })
        .collect();

    let mut ans: i64 = 0;

    for line in data {
        let mut new_data: Vec<Vec<i64>> = vec![line.clone()];

        let mut diff = line.clone();

        while diff.iter().any(|&x| x != 0) {
            diff = diff
                .windows(2)
                .map(|window| window[1] - window[0])
                .collect();
            new_data.push(diff.clone())
        }

        let l: i64 = new_data
            .iter()
            .map(|v| *v.last().unwrap())
            .collect::<Vec<_>>()
            .iter()
            .sum();
        ans += l;
    }
    ans
}

#[cfg(test)]
mod tests {
    use super::*;
    use std::fs;

    #[test]
    fn test_part1_test() {
        let contents: String = fs::read_to_string("../data/input_test.txt").unwrap();
        assert_eq!(part1(&contents), 114);
    }

    #[test]
    fn test_part1() {
        let contents: String = fs::read_to_string("../data/input.txt").unwrap();
        assert_eq!(part1(&contents), 1731106378);
    }
}
