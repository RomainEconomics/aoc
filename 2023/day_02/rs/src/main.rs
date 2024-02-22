
use std::fs;
pub mod part1;
pub mod part2;

fn main() {

    let filename = "../data/input.txt";
    let contents = fs::read_to_string(filename).unwrap();

    let result = part1::part1(&contents);
    println!("Part 1: {}", result);

    let result = part2::part2(&contents);
    println!("Part 2: {}", result);

}
