pub fn move_rocks(mut data: Vec<Vec<char>>) -> Vec<Vec<char>> {
    for i in 1..data.len() {
        for j in 0..data[i].len() {
            let val = data[i][j];

            if val == 'O' {
                let mut new_row_idx = i;
                loop {
                    if (new_row_idx > 0) && (data[new_row_idx - 1][j] == '.') {
                        new_row_idx -= 1;
                    } else {
                        break;
                    }
                }

                if new_row_idx != i {
                    data[i][j] = '.';
                    data[new_row_idx][j] = 'O';
                }
            }
        }
    }

    data
}

pub fn calculate_score(data: Vec<Vec<char>>) -> usize {
    let mut score = 0;
    for i in 0..data.len() {
        let mut count = 0;
        for j in 0..data[i].len() {
            if data[i][j] == 'O' {
                count += 1;
            }
        }

        score += count * (data.len() - i);
    }
    score
}

pub fn part1(contents: &str) -> usize {
    let mut data: Vec<Vec<char>> = contents
        .lines()
        .map(|line| line.chars().collect::<Vec<_>>())
        .collect();

    data = move_rocks(data);

    calculate_score(data)
}

#[cfg(test)]
mod tests {
    use super::*;
    use std::fs;

    #[test]
    fn test_part1_test() {
        let contents: String = fs::read_to_string("../data/input_test.txt").unwrap();
        assert_eq!(part1(&contents), 136);
    }

    #[test]
    fn test_part1() {
        let contents: String = fs::read_to_string("../data/input.txt").unwrap();
        assert_eq!(part1(&contents), 110274);
    }
}
