use core::str;
use indexmap::IndexMap;

use crate::part1::{compute_hash, format_data, read_file};

fn hashmap(data: &Vec<&[u8]>) -> Vec<IndexMap<Vec<u8>, u64>> {
    let mut boxes: Vec<IndexMap<Vec<u8>, u64>> = (0..256).map(|_| IndexMap::new()).collect();

    for s in data {
        let raw_values: Vec<u8> = s.iter().copied().filter(|&i| i != b'-').collect();

        let parts: Vec<&[u8]> = raw_values.split(|&b| b == b'=').collect();

        match parts.as_slice() {
            [label, value] => {
                let label = label.to_vec();
                if let Ok(value_str) = std::str::from_utf8(value) {
                    if let Ok(value) = value_str.parse::<u64>() {
                        boxes[compute_hash(&label) as usize].insert(label, value);
                    }
                }
            }
            [label] => {
                let label = label.to_vec();
                boxes[compute_hash(&label) as usize].shift_remove(&label);
            }
            _ => {}
        }
    }
    boxes
}

fn compute_score(boxes: Vec<IndexMap<Vec<u8>, u64>>) -> u64 {
    boxes.iter().enumerate().fold(0, |acc, (box_id, boxx)| {
        acc + boxx
            .iter()
            .enumerate()
            .fold(0, |inner_acc, (slot, (_, &focal))| {
                inner_acc + (box_id as u64 + 1) * (slot as u64 + 1) * focal
            })
    })
}

pub fn part2(path: &str) -> u64 {
    let data = read_file(path);
    let values = format_data(&data);

    let boxes = hashmap(&values);
    compute_score(boxes)
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_part2_test() {
        assert_eq!(part2("../data/input_test.txt"), 145);
    }

    #[test]
    fn test_part2() {
        assert_eq!(part2("../data/input.txt"), 268497);
    }
}
