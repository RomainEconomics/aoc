// Build an enum with those values: A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, or 2

use std::{cmp::Reverse, collections::HashMap};

pub fn card_value(card: &str) -> i64 {
    match card {
        "A" => 14,
        "K" => 13,
        "Q" => 12,
        "J" => 11,
        "T" => 10,
        _ => card.parse::<i64>().unwrap(),
    }
}

fn check_hand_type(cards: &str) -> i64 {
    let mut card_count: HashMap<char, i64> = HashMap::new();
    for card in cards.chars() {
        *card_count.entry(card).or_insert(0) += 1;
    }

    let mut card_count: Vec<i64> = card_count.values().cloned().collect();
    card_count.sort_unstable_by_key(|&count| Reverse(count));

    match card_count.as_slice() {
        [5] => 6,
        [4, 1] => 5,
        [3, 2] => 4,
        [3, 1, 1] => 3,
        [2, 2, 1] => 2,
        [2, 1, 1, 1] => 1,
        _ => 0,
    }
}

pub fn part1(contents: &String) -> i32 {
    let mut hands: Vec<(String, i32)> = Vec::new();

    for line in contents.lines() {
        let parts: Vec<&str> = line.split(" ").collect();
        let cards: String = parts[0].to_string();
        let bid: i32 = parts[1].parse::<i32>().unwrap();
        hands.push((cards, bid));
    }

    hands.sort_by(|a, b| {
        let hand_type_comparison = check_hand_type(&a.0).cmp(&check_hand_type(&b.0));
        if hand_type_comparison == std::cmp::Ordering::Equal {
            let a_vals = a.0.chars().map(|c| card_value(&c.to_string()));
            let b_vals = b.0.chars().map(|c| card_value(&c.to_string()));
            let cmp_val = a_vals
                .zip(b_vals)
                .find(|(a_val, b_val)| a_val != b_val)
                .unwrap();

            cmp_val.0.cmp(&cmp_val.1)
        } else {
            hand_type_comparison
        }
    });
    hands
        .iter()
        .enumerate()
        .map(|(idx, hand)| (idx as i32 + 1) * hand.1)
        .sum::<i32>()
}

#[cfg(test)]
mod tests {
    use super::*;
    use std::fs;

    #[test]
    fn test_part1_test() {
        let contents: String = fs::read_to_string("../data/input_test.txt").unwrap();
        assert_eq!(part1(&contents), 6440);
    }

    #[test]
    fn test_part1() {
        let contents: String = fs::read_to_string("../data/input.txt").unwrap();
        assert_eq!(part1(&contents), 250951660);
    }
}
