#! /usr/bin/env python

from functools import reduce


def get_data(path):
    with open(path) as in_f:
        data = in_f.read()
        for group in data.split("\n\n"):
            yield [list(p) for p in group.split("\n") if p]


def count_unique_answers(group):
    answers = set([answer for person in group for answer in person])
    return len(answers)


def keep_matching(list_a, list_b):
    return [x for x in list_a if x in list_b]


def count_unanimous_answers(group):
    unanimous = reduce(keep_matching, group)
    return len(unanimous)


def calculate_total_score(groups, count_func):
    scores = list([count_func(g) for g in groups])
    return reduce(lambda x, y: x + y, scores)


if __name__ == "__main__":
    groups = list(get_data("data"))

    # Part 1
    total = calculate_total_score(groups, count_unique_answers)
    print(total)

    # Part 2
    total = calculate_total_score(groups, count_unanimous_answers)
    print(total)
