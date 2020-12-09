#! /usr/bin/env python


def load_data(path):
    with open(path) as in_f:
        return [int(line.strip()) for line in in_f.readlines()]


def matrix_sum(numbers):
    results = []
    for a in numbers:
        for b in numbers:
            if a != b:
                results.append(a + b)
    return results


def find_invalid_number(numbers, preamble_size):
    for i in range(preamble_size, len(numbers)):
        if numbers[i] not in matrix_sum(numbers[i - preamble_size : i]):
            return numbers[i]


def find_set(numbers, total):
    running_total = 0
    for i, n in enumerate(numbers):
        running_total += n
        if running_total == total:
            return numbers[: i + 1]
        if running_total > total:
            return None


def find_any_set(numbers, total):
    for i in range(0, len(numbers)):
        set_ = find_set(numbers[i:], total)
        if set_:
            return set_


def find_weakness(numbers, total):
    set_ = find_any_set(numbers, total)
    minimum, maximum = min(set_), max(set_)
    return minimum + maximum


if __name__ == "__main__":
    numbers = load_data("data")

    # Part 1
    invalid_number = find_invalid_number(numbers, 25)
    print(invalid_number)

    # Part 2
    print(find_weakness(numbers, invalid_number))
