pub fn part2(contents: &str) -> i32 {
    let (l1, l2): (Vec<i32>, Vec<i32>) = contents
        .lines()
        .map(|line| {
            let mut nums = line.split_whitespace().map(|n| n.parse::<i32>().unwrap());
            (nums.next().unwrap(), nums.next().unwrap())
        })
        .unzip();

    l1.iter()
        .map(|n| l2.iter().filter(|x| *x == n).count() as i32 * n)
        .sum()
}

#[cfg(test)]
mod tests {
    use std::fs;

    use super::*;

    #[test]
    fn test_part2_test() {
        let contents: String = fs::read_to_string("../data/input_test.txt").unwrap();
        assert_eq!(part2(&contents), 31);
    }

    #[test]
    fn test_part2() {
        let contents: String = fs::read_to_string("../data/input.txt").unwrap();
        assert_eq!(part2(&contents), 22565391);
    }
}
