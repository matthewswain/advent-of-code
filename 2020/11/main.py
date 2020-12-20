#! /usr/bin/env python


from collections import namedtuple
from copy import deepcopy

Coords = namedtuple("coords", "line col")


def load_data(path):
    with open(path) as in_f:
        return [list(line.strip()) for line in in_f.readlines()]


def get_next_seat(data, start, direction, count_floor):
    next_seat = Coords(start.line + direction.line, start.col + direction.col)

    if (
        next_seat.line < 0
        or next_seat.line >= len(data)
        or next_seat.col < 0
        or next_seat.col >= len(data[start.line])
    ):
        return None

    value = data[next_seat.line][next_seat.col]

    if value == "." and not count_floor:
        value = get_next_seat(data, next_seat, direction, count_floor)

    return value


def count_occupied_neighbours(data, seat, count_floor):
    values = []

    for line in range(-1, 2):
        for col in range(-1, 2):
            if line == 0 and col == 0:
                continue

            value = get_next_seat(data, seat, Coords(line, col), count_floor)
            if value is not None:
                values.append(value)

    return len([v for v in values if v == "#"])


def update_seat(data, seat, count_floor, threshold):
    if data[seat.line][seat.col] == ".":
        return data[seat.line][seat.col]

    occupied_neighbours = count_occupied_neighbours(data, seat, count_floor)
    if occupied_neighbours == 0:
        return "#"
    if occupied_neighbours >= threshold:
        return "L"
    return data[seat.line][seat.col]


def update_plan(data, count_floor, threshold):
    new = deepcopy(data)
    for line in range(0, len(data)):
        for col in range(0, len(data[line])):
            new[line][col] = update_seat(
                data, Coords(line, col), count_floor, threshold
            )
    return new


def run_to_completion(data, count_floor=True, threshold=4):
    while True:
        same = True
        new = update_plan(data, count_floor, threshold)
        for line in range(0, len(data)):
            for col in range(0, len(data[line])):
                if data[line][col] != new[line][col]:
                    same = False
        if same:
            return new
        data = new


def count_occupied_seats(data):
    return len([seat for line in data for seat in line if seat == "#"])


if __name__ == "__main__":
    data = load_data("data")

    # Part 1
    print(count_occupied_seats(run_to_completion(data)))

    # Part 2
    print(count_occupied_seats(run_to_completion(data, False, 5)))
