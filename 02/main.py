#! /usr/bin/env python

import re


policy_regex = r"([0-9]+)-([0-9]+) ([a-z]): ([a-z]+)"


def get_lines(path):
    with open(path) as in_f:
        for line in in_f:
            if line.strip():
                yield line.strip()


def get_data(path):
    data = []
    for line in get_lines(path):
        m = re.match(policy_regex, line)
        minimum, maximum, character, password = m.groups()
        data.append(((int(minimum), int(maximum), character), password))
    return data


def validate_password_1(policy, password):
    chars = list([c for c in password if c == policy[2]])
    count = len(chars)
    return count >= policy[0] and count <= policy[1]


def validate_password_2(policy, password):
    matches = 0

    for i in range(0, 2):
        position = policy[i] - 1
        match = policy[2] == password[position]
        if match:
            matches += 1

    return matches == 1


def count_valid_passwords(data, validator):
    count = 0
    for policy, password in data:
        valid = validator(policy, password)
        if valid:
            count += 1
    return count


if __name__ == "__main__":
    data = get_data("02/data")
    
    count = count_valid_passwords(data, validate_password_1)
    print(count)

    count = count_valid_passwords(data, validate_password_2)
    print(count)
