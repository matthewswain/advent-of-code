#! /usr/bin/env python

import re


def load_data(path):
    with open(path) as in_f:
        return list([l.strip() for l in in_f.readlines()])


def eval_line_1(line):
    line = line.replace(" ", "")

    while matches := re.findall(r"\(([0-9\*\+]+)\)", line):
        for m in matches:
            line = line.replace(f"({m})", str(eval_line_1(m)))

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


def eval_line_2(line):
    line = line.replace(" ", "")

    while matches := re.findall(r"\(([0-9\*\+]+)\)", line):
        for m in matches:
            line = line.replace(f"({m})", str(eval_line_2(m)))

    while m := re.search(r"([0-9]+(?:\+[0-9]+)+)", line):
        e = m.groups()[0]
        pattern = r"(?<![0-9]){}(?![0-9])".format(e.replace("+", r"\+"))
        line = re.sub(pattern, str(eval(e)), line)

    return eval(line)


if __name__ == "__main__":
    data = load_data("data")

    # Print 1
    print(sum([eval_line_1(l) for l in data]))

    # Part 2
    print(sum([eval_line_2(l) for l in data]))
