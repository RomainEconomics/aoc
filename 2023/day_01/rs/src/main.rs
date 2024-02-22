
pub mod part1;
pub mod part2;
use std::fs;

fn main() {

    let filename: &str = "../data/input.txt";
    let contents: String = fs::read_to_string(filename).unwrap();

    let res = part1::part1(&contents);
    println!("Part 1: {}", res);

    let res = part2::part2(&contents);
    println!("Part 2: {}", res);

}
