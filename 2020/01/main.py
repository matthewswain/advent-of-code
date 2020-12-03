#! /usr/bin/env python


def load_data(path):
    with open(path) as in_f:
        return [int(line.strip()) for line in in_f.readlines()]


def find_pair(data):
    for x in data:
        for y in data:
            if x + y == 2020:
                return x, y
    raise Exception("pair not found")


def find_triple(data):
    for x in data:
        for y in data:
            for z in data:
                if x + y + z == 2020:
                    return x, y, z
    raise Exception("triple not found")


if __name__ == "__main__":
    data = load_data("01/data")

    # Part 1
    x, y = find_pair(data)
    print(x * y)

    # Part 2
    x, y, z = find_triple(data)
    print(x * y * z)
