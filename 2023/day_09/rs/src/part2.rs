pub fn part2(contents: &String) -> i64 {
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

        let mut val = new_data.last().unwrap().first().unwrap().clone();
        for i in (0..(new_data.len() - 1)).rev() {
            val = new_data[i][0] - val;
        }

        ans += val;
    }
    ans
}

#[cfg(test)]
mod tests {
    use super::*;
    use std::fs;

    #[test]
    fn test_part2() {
        let contents: String = fs::read_to_string("../data/input.txt").unwrap();
        assert_eq!(part2(&contents), 1087);
    }
}
