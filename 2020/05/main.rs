use std::fs;

fn main() {
    let lines = get_data("data");
    let seats: Vec<u32> = lines.iter().map(|l| get_seat(l)).collect();
    
    println!("{}", seats.iter().max().unwrap());

    println!("{}", find_missing_seat(seats).unwrap());
}

fn find_missing_seat(seats: Vec<u32>) -> Option<u32> {
    let min = *seats.iter().min().unwrap();
    let max = *seats.iter().max().unwrap();
    for seat in min..max {
       if !seats.contains(&seat) {
            return Some(seat);
       }
    }
    return None;
}

fn get_seat(boarding_pass: &str) -> u32 {
    let row = read_binary(&boarding_pass[..7], 'B');
    let col = read_binary(&boarding_pass[7..], 'R');
    return row * 8 + col;
}

fn read_binary(value: &str, set_val: char) -> u32 {
    let mut total: u32 = 0;
    for (i, c) in value.chars().rev().enumerate() {
        if c != set_val {
            continue;
        }
        total += u32::pow(2, i as u32);
    }
    return total;
}

fn get_data(file_path: &str) -> Vec<String> {
    let data = fs::read_to_string(file_path).unwrap();

    return data.split("\n")
        .map(|s| s.to_string())
        .filter(|s| s != "").collect();
}
