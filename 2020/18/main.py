#! /usr/bin/env python

import re


def load_data(path):
    with open(path) as in_f:
        return list([l.strip() for l in in_f.readlines()])


def eval_line(line):
    line = line.replace(" ", "")

    while matches := re.findall(r"\(([0-9\*\+]+)\)", line):
        for m in matches:
            line = line.replace(f"({m})", str(eval_line(m)))

    total = 0
    operator = "+"
    value = ""
    for c in line:
        if c in "0123456789":
            value += c
        if c in "+*":
            total = eval(f"{total}{operator}{value}")
            value = ""
            operator = c

    total = eval(f"{total}{operator}{value}")
    return total


if __name__ == "__main__":
    data = load_data("data")

    # Print 1
    print(sum([eval_line(l) for l in data]))
