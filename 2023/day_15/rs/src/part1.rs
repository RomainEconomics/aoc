use std::{fs::File, io::Read};

pub fn read_file(path: &str) -> Vec<u8> {
    let mut f = File::open(path).unwrap();
    let mut buffer = Vec::new();
    f.read_to_end(&mut buffer).unwrap();
    buffer
}

pub fn format_data(data: &Vec<u8>) -> Vec<&[u8]> {
    data.strip_suffix(&[b'\n'])
        .unwrap()
        .split(|&x| x == b',')
        .collect::<Vec<_>>()
}

pub fn compute_hash(x: &[u8]) -> usize {
    x.iter()
        .map(|&v| v as usize)
        .fold(0, |acc, val| ((acc + val) * 17) % 256)
}

pub fn compute_hashes(data: Vec<&[u8]>) -> usize {
    data.iter().map(|&x| compute_hash(x)).sum::<usize>()
}

pub fn part1(path: &str) -> usize {
    let data = read_file(path);
    let values = format_data(&data);
    compute_hashes(values)
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_part1_test() {
        assert_eq!(part1("../data/input_test.txt"), 1320);
    }

    #[test]
    fn test_part1() {
        assert_eq!(part1("../data/input.txt"), 510013);
    }
}
