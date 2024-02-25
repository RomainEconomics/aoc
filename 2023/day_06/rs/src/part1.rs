

pub fn part1(contents: &String) -> i64 {

    let times: Vec<i64> = contents.lines().nth(0).unwrap().split(" ").filter_map(|x| x.parse().ok()).collect();
    let distances: Vec<i64> = contents.lines().nth(1).unwrap().split(" ").filter_map(|x| x.parse().ok()).collect();
    
    times
        .iter()
        .zip(distances)
        .map(|(t, d)| {
            (0..*t).map(|i| i * (t - i)).filter(|x| *x > d).count() as i64
        }
        )
        .product::<i64>()
}


#[cfg(test)]
mod tests {
    use super::*;
    use std::fs;

    #[test]
    fn test_part1_test() {
        let contents: String = fs::read_to_string("../data/input_test.txt").unwrap();
        assert_eq!(part1(&contents), 288);
    }

    #[test]
    fn test_part1() {
        let contents: String = fs::read_to_string("../data/input.txt").unwrap();
        assert_eq!(part1(&contents), 252000);
    }
}
