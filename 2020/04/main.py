#! /usr/bin/env python

import re


def load_data(path):
    with open(path) as in_f:
        return in_f.read().split("\n\n")


def parse_record(record):
    parsed = {}
    for field in record.split():
        k, v = field.split(":")
        parsed[k] = v
    return parsed


def has_required_fields(record):
    required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    for field in required_fields:
        if field not in record.keys():
            return False
    return True


def year_is_valid(earliest, latest, year):
    try:
        year = int(year)
    except ValueError:
        return False
    return int(year) >= earliest and int(year) <= latest


def byr_is_valid(byr):
    return year_is_valid(1920, 2002, byr)


def iyr_is_valid(iyr):
    return year_is_valid(2010, 2020, iyr)


def eyr_is_valid(eyr):
    return year_is_valid(2020, 2030, eyr)


def hgt_is_valid(hgt):
    limits = {
        "cm": (150, 193),
        "in": (59, 76),
    }
    try:
        value, unit = re.match(r"^([0-9]+)(cm|in)$", hgt).groups()
        value = int(value)
        unit_limits = limits[unit]
        return value >= unit_limits[0] and value <= unit_limits[1]
    except Exception:
        return False


def hcl_is_valid(hcl):
    return re.match(r"^#[0-9a-f]{6}$", hcl)


def ecl_is_valid(ecl):
    valid_colours = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    return ecl in valid_colours


def pid_is_valid(pid):
    return re.match(r"^[0-9]{9}$", pid)


def validate_record(record, extended):
    if not extended:
        return has_required_fields(record)
    return (
        has_required_fields(record)
        and byr_is_valid(record["byr"])
        and iyr_is_valid(record["iyr"])
        and eyr_is_valid(record["eyr"])
        and hgt_is_valid(record["hgt"])
        and hcl_is_valid(record["hcl"])
        and ecl_is_valid(record["ecl"])
        and pid_is_valid(record["pid"])
    )


def parse_and_validate_records(records, extended=False):
    for record in records:
        parsed = parse_record(record)
        if validate_record(parsed, extended):
            yield parsed


if __name__ == "__main__":
    data = load_data("data")

    # Part 1
    records = parse_and_validate_records(data)
    print(len(list(records)))

    # Part 2
    records = parse_and_validate_records(data, extended=True)
    print(len(list(records)))
