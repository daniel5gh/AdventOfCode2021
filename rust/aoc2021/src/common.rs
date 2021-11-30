use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

// thanks https://doc.rust-lang.org/stable/rust-by-example/std_misc/file/read_lines.html
// The output is wrapped in a Result to allow matching on errors
// Returns an Iterator to the Reader of the lines of the file.
pub fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
    where P: AsRef<Path>, {
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}

pub fn read_as_ints(filename: &str) -> Vec<i32> {
    let mut result: Vec<i32> = Vec::new();

    for line in read_lines(filename).unwrap() {
        let n = line.unwrap().parse::<i32>().unwrap();
        result.push(n);
    }

    result
}