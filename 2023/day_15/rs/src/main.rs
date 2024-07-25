pub mod part1;
pub mod part2;

fn main() {
    let result = part1::part1("../data/input.txt");
    println!("Part 1: {}", result);

    let part2 = part2::part2("../data/input.txt");
    println!("Part 2: {}", part2);
}
