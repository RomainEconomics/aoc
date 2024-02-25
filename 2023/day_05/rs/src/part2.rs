
pub fn part2(contents: &String) -> i64 {

    let mut seeds: Vec<(i64, i64)> = contents.lines().next().unwrap()
        .split_whitespace()
        .skip(1)
        .map(|x| x.parse::<i64>().unwrap())
        .collect::<Vec<i64>>()
        .chunks(2)
        .map(|x| (x[0], x[0] + x[1]))
        .collect();

    for x_to_y_map in contents.split("\n\n") {
        let sources: Vec<Vec<i64>> = x_to_y_map
            .split('\n')
            .skip(1)
            .filter_map(|x| {
                if x.is_empty() {
                    None
                } else {
                    Some(
                        x.split_whitespace()
                            .map(|x| x.parse::<i64>().unwrap())
                            .collect(),
                    )
                }
            })
            .collect();

        let mut new = Vec::new();

        while !seeds.is_empty() {
            let (start, end) = seeds.remove(0);
            let mut breaked = false;
            for r in &sources {
                let (r_start, r_end, r_len) = (r[0], r[1], r[2]);
                let os = start.max(r_end);
                let oe = end.min(r_end + r_len);
                if os < oe {
                    new.push((os - r_end + r_start, oe - r_end + r_start));
                    if os > start {
                        seeds.push((start, os));
                    }
                    if oe < end {
                        seeds.push((oe, end));
                    }
                    breaked = true;
                    break;
                }
            }
            if !breaked {
                new.push((start, end));
            }
        }
        seeds = new;
    }

    seeds.iter().map(|(x, _)| *x).min().unwrap()
}


#[cfg(test)]
mod tests {
    use super::*;
    use std::fs;

    #[test]
    fn test_part2_test() {
        let contents: String = fs::read_to_string("../data/input_test.txt").unwrap();
        assert_eq!(part2(&contents), 46);
    }

    #[test]
    fn test_part2() {
        let contents: String = fs::read_to_string("../data/input.txt").unwrap();
        assert_eq!(part2(&contents), 219529182);
    }
}