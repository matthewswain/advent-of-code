#! /usr/bin/env python

from functools import cache


def load_data(path):
    with open(path) as in_f:
        return [int(line.strip()) for line in in_f.readlines()]


def prepare_data(adapters):
    adapters.append(0)
    adapters.append(max(adapters) + 3)
    return tuple(sorted(adapters))


def get_differences(adapters):
    for i in range(1, len(adapters)):
        yield adapters[i] - adapters[i - 1]


def can_plug(chain, adapter):
    return adapter - chain[-1] <= 3


def test_all_adapters(adapters):
    differences = list(get_differences(adapters))
    one_jolt_count = len([d for d in differences if d == 1])
    three_jolt_count = len([d for d in differences if d == 3])
    return one_jolt_count * three_jolt_count


@cache
def count_possible_chains(adapters, position):
    if position == len(adapters) - 1:
        return 1

    total = 0
    for i in range(position + 1, position + 4):
        if i < len(adapters) and can_plug(adapters[: position + 1], adapters[i]):
            total += count_possible_chains(adapters, i)

    return total


if __name__ == "__main__":
    adapters = prepare_data(load_data("data"))

    # Part 1
    print(test_all_adapters(adapters))

    # Part 2
    print(count_possible_chains(adapters, 0))
