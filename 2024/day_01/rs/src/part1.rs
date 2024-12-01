pub fn part1(contents: &str) -> i32 {
    let (mut l1, mut l2): (Vec<i32>, Vec<i32>) = contents
        .lines()
        .map(|line| {
            let mut nums = line.split_whitespace().map(|n| n.parse::<i32>().unwrap());
            (nums.next().unwrap(), nums.next().unwrap())
        })
        .unzip();

    l1.sort();
    l2.sort();

    l1.iter().zip(l2).map(|(x, y)| (x - y).abs()).sum()
}

#[cfg(test)]
mod tests {
    use std::fs;

    use super::*;

    #[test]
    fn test_part1_test() {
        let contents: String = fs::read_to_string("../data/input_test.txt").unwrap();
        assert_eq!(part1(&contents), 11);
    }

    #[test]
    fn test_part1() {
        let contents: String = fs::read_to_string("../data/input.txt").unwrap();
        assert_eq!(part1(&contents), 3574690);
    }
}
