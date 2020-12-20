#! /usr/bin/env python

import re
from collections import namedtuple

contents = namedtuple("contents", "colour number")


def parse_bags(line):
    parent, children_string = line.split(" bags contain ")

    p = r"([0-9]+) ([a-z ]+) bag"
    children = []
    for child_string in children_string.split(","):
        m = re.search(p, child_string)
        if m:
            children.append(contents(m.group(2), int(m.group(1))))

    return parent, children


def get_data(path):
    bags = {}
    with open(path) as in_f:
        for line in in_f:
            bag, children = parse_bags(line)
            bags[bag] = children
    return bags


def find_unique_parents(bags, colour):
    parents = set()
    for parent, children in bags.items():
        if colour in [c.colour for c in children]:
            parents.add(parent)
            parents = parents.union(find_unique_parents(bags, parent))
    return parents


def count_children(bags, colour):
    count = 0
    for child in bags[colour]:
        count += child.number
        count += child.number * count_children(bags, child.colour)
    return count


if __name__ == "__main__":
    bags = get_data("data")

    # Part 1
    print(len(find_unique_parents(bags, "shiny gold")))

    # Part 2
    print(count_children(bags, "shiny gold"))
