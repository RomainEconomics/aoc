

pub fn part2(contents: &String) -> i64 {

    let time: i64 = contents.lines().nth(0).unwrap().split(":").filter_map(|x| x.replace(" ", "").parse().ok()).nth(0).unwrap();
    let distance: i64 = contents.lines().nth(1).unwrap().split(":").filter_map(|x| x.replace(" ", "").parse().ok()).nth(0).unwrap();

    let mut sum: i64 = 0;
    
    for i in 0..time {
        let x = i * (time - i);
        if x > distance {
            sum += i as i64;
            break
        }
    }

    for i in (0..time).rev() {
        let x = i * (time - i);
        if x > distance {
            sum = i - sum + 1;
            break
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
        assert_eq!(part2(&contents), 71503);
    }

    #[test]
    fn test_part2() {
        let contents: String = fs::read_to_string("../data/input.txt").unwrap();
        assert_eq!(part2(&contents), 36992486);
    }
}
