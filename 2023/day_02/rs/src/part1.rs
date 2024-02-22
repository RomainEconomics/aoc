use std::collections::HashMap;

pub fn part1(contents: &String) -> i32 {

    let mut max_bag = HashMap::new();
    max_bag.insert("red", 12);
    max_bag.insert("green", 13);
    max_bag.insert("blue", 14);


    contents
        .lines()
        .map(|line| {

            let game = line
                .split(":")
                .collect::<Vec<_>>();

            let game_id = game[0].split(" ").collect::<Vec<_>>()[1].parse::<i32>().unwrap();

            for cube in game[1].split(";") {
                let cube = cube.trim();
                let cube = cube.split(", ").collect::<Vec<_>>();
                for c in cube {
                    let c = c.split(" ").collect::<Vec<_>>();
                    let count = c[0].parse::<i32>().unwrap();
                    let color = c[1];
                    
                    if count > max_bag[color] {
                        return 0 as i32;
                    }
                }
            } 
            game_id
            
        }
        )
        .collect::<Vec<_>>()
        .iter()
        .sum::<i32>()
}


#[cfg(test)]
mod tests {
    use super::*;
    use std::fs;

    #[test]
    fn test_part1_test() {
        let contents: String = fs::read_to_string("../data/input_test.txt").unwrap();
        assert_eq!(part1(&contents), 8);
    }

        #[test]
    fn test_part1() {
        let contents: String = fs::read_to_string("../data/input.txt").unwrap();
        assert_eq!(part1(&contents), 1734);
    }
}