#! /usr/bin/env python


def get_data(path):
    with open(path) as in_f:
        return [line.strip() for line in in_f.readlines()]


def read_binary(data, set_val):
    return sum([2 ** i for i, v in enumerate(reversed(data)) if v == set_val])


def get_seat(boarding_pass):
    row = read_binary(boarding_pass[:7], "B")
    col = read_binary(boarding_pass[7:], "R")
    return row * 8 + col


def find_missing_seat(seats):
    min_seat, max_seat = min(seats), max(seats)
    return [i for i in range(min_seat, max_seat) if i not in seats][0]


if __name__ == "__main__":
    data = get_data("data")
    seats = [get_seat(bp) for bp in data]

    # Part 1
    print(max(seats))

    # Part 2
    print(find_missing_seat(seats))
