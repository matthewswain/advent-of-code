#! /usr/bin/env python

from functools import reduce


def get_map(path):
    with open(path) as in_f:
        map_ = [line.strip() for line in in_f.readlines()]
        return map_


def is_tree(map_, v_pos, h_pos):
    # Using the modulus operator effectively makes map_ infinite; if len(map_)
    # is 10, and h_pos is 10+, we'll loop back around to the start of the map.
    h_pos = h_pos % len(map_[0])
    return map_[v_pos][h_pos] == "#"


def navigate(map_, right, down):
    h_pos = 0
    trees = 0
    for v_pos in range(0, len(map_), down):
        if is_tree(map_, v_pos, h_pos):
            trees += 1
        h_pos += right
    return trees


if __name__ == "__main__":
    map_ = get_map("03/data")

    # Part 1
    trees = navigate(map_, 3, 1)
    print(trees)

    # Part 2
    paths = [
        (1, 1),
        (3, 1),
        (5, 1),
        (7, 1),
        (1, 2),
    ]
    trees = [navigate(map_, p[0], p[1]) for p in paths]
    print(reduce(lambda a, b: a * b, trees))
