use aoc2021::common;

fn part1(ints: &Vec<i32>) {
    for x in ints.iter() {
        for y in ints.iter() {
            if x + y == 2020 {
                println!("{}", x * y);
            }
        }
    }
}

fn part2(ints: &Vec<i32>) {
    for x in ints.iter() {
        for y in ints.iter() {
            for z in ints.iter() {
                if x + y + z == 2020 {
                    println!("{}", x * y * z);
                }
            }
        }
    }
}

fn main() {
    let ints = common::read_as_ints("input/aoc2020-day01.txt");
    println!("Hello {} ints!", ints.len());
    part1(&ints);
    part2(&ints);
}
