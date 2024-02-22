
use std::collections::HashMap;

pub fn part2(contents: &String) -> i32 {

    contents
        .lines()
        .map(|line| {

            let mut min_bag: HashMap<&str, i32> = HashMap::new();            
            
            let game = line
                .split(":")
                .collect::<Vec<_>>();

            for cube in game[1].split(";") {
                let cube = cube.trim();
                let cube = cube.split(", ").collect::<Vec<_>>();
                for c in cube {
                    let c = c.split(" ").collect::<Vec<_>>();
                    let count = c[0].parse::<i32>().unwrap();
                    let color = c[1];
                    min_bag.entry(color).and_modify(|e| *e = std::cmp::max(*e, count)).or_insert(count);
                }
            } 

            min_bag.values().fold(1, |acc, x| acc * x)
            
            }
        )
        .collect::<Vec<_>>()
        .iter()
        .cloned()
        .sum::<i32>()
}


#[cfg(test)]
mod tests {
    use super::*;
    use std::fs;

    #[test]
    fn test_part2_test() {
        let contents: String = fs::read_to_string("../data/input_test.txt").unwrap();
        assert_eq!(part2(&contents), 2286);
    }

        #[test]
    fn test_part2() {
        let contents: String = fs::read_to_string("../data/input.txt").unwrap();
        assert_eq!(part2(&contents), 70387);
    }
}