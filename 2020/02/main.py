#! /usr/bin/env python

import re

policy_regex = r"([0-9]+)-([0-9]+) ([a-z]): ([a-z]+)"


def get_lines(path):
    with open(path) as in_f:
        return [line.strip() for line in in_f.readlines()]


def get_data(path):
    data = []
    for line in get_lines(path):
        m = re.match(policy_regex, line)
        minimum, maximum, character, password = m.groups()
        data.append(((int(minimum), int(maximum), character), password))
    return data


def validate_password_1(policy, password):
    # The policy specifies minimum repeats, maximum repeats and a character;
    # the character must be repeated at least the minimum number of times, and
    # no more than the maximum.
    chars = list([c for c in password if c == policy[2]])
    count = len(chars)
    return count >= policy[0] and count <= policy[1]


def validate_password_2(policy, password):
    # The policy specifies two positions and a character; the character must
    # appear in exactly one of the two positions.
    matches = 0

    for i in range(0, 2):
        position = policy[i] - 1
        match = policy[2] == password[position]
        if match:
            matches += 1

    return matches == 1


def count_valid_passwords(data, validator):
    # By passing the validator in as a function, we can reuse the counting
    # logic; effectively a basic strategy pattern.
    count = 0
    for policy, password in data:
        valid = validator(policy, password)
        if valid:
            count += 1
    return count


if __name__ == "__main__":
    data = get_data("data")

    # Part 1
    count = count_valid_passwords(data, validate_password_1)
    print(count)

    # Part 2
    count = count_valid_passwords(data, validate_password_2)
    print(count)
