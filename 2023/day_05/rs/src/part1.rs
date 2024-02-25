

fn parse_line(map: & Vec<Vec<i64>>, seeds: &mut Vec<i64>) -> Vec<i64> {
                 
    let mut new_seeds: Vec<i64> = Vec::new();

    for seed in seeds {
        if let Some(m) = map.iter().find(|m| m[1] <= *seed && *seed <= m[1] + m[2]) {
            new_seeds.push(*seed - m[1] + m[0]);
        } else {
            new_seeds.push(*seed);
        }
    }
    new_seeds
}


pub fn part1(contents: &String) -> i64 {

    let mut lines = contents.split("\n").collect::<Vec<&str>>();

    let mut seeds: Vec<i64> = lines[0].split_whitespace().skip(1).map(|x| x.parse::<i64>().unwrap()).collect();

    lines.remove(0);
    lines.remove(0);

    let mut map: Vec<Vec<i64>> = Vec::new();

    for line in lines {

        if line.is_empty() {

            let new_seeds = parse_line(&mut map, &mut seeds);
            seeds = new_seeds;

            map.clear();
            continue;
        }

        if line.contains("map:") {
            continue;
        }

        let row: Vec<i64> = line.split_whitespace().map(|x| x.parse::<i64>().unwrap()).collect();
        map.push(row);

    }

    let new_seeds = parse_line(&mut map, &mut seeds);
    *new_seeds.iter().min().unwrap()

}



#[cfg(test)]
mod tests {
    use super::*;
    use std::fs;

    #[test]
    fn test_part1_test() {
        let contents: String = fs::read_to_string("../data/input_test.txt").unwrap();
        assert_eq!(part1(&contents), 35);
    }

    #[test]
    fn test_part1() {
        let contents: String = fs::read_to_string("../data/input.txt").unwrap();
        assert_eq!(part1(&contents), 403695602);
    }
}