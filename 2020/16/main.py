#! /usr/bin/env python

from functools import reduce
from typing import Dict, List


class Range:
    minimum: int
    maximum: int

    def __init__(self, line: str):
        min_string, max_string = line.split("-")
        self.minimum, self.maximum = int(min_string), int(max_string)


class Rule:
    name: str
    ranges: List[Range]

    def __init__(self, line: str):
        self.name, ranges_string = line.strip().split(":")

        self.ranges = []
        for range_string in ranges_string.split(" or "):
            self.ranges.append(Range(range_string))

    def validate(self, value: int):
        for valid_range in self.ranges:
            if valid_range.minimum <= value <= valid_range.maximum:
                return True
        return False

    @staticmethod
    def parse_rules(data) -> List:
        rules = []
        lines = data.strip().split("\n")
        for line in lines:
            rules.append(Rule(line))
        return rules


class Ticket:
    values: List[int]

    def __init__(self, line: str):
        self.values = [int(n) for n in line.strip().split(",")]

    def get_invalid_values(self, rules: List[Rule]) -> List[int]:
        for value in self.values:
            invalid = True
            for rule in rules:
                if rule.validate(value):
                    invalid = False
            if invalid:
                yield value

    def is_valid(self, rules: List[Rule]) -> bool:
        return len(list(self.get_invalid_values(rules))) == 0

    def decode(self, lookup: Dict[int, str]) -> Dict[str, int]:
        decoded = {}
        for i, value in enumerate(self.values):
            name = lookup[i]
            decoded[name] = value
        return decoded


def load_data(path):
    with open(path) as in_f:
        data = in_f.read()
    rules_data, my_ticket_data, other_tickets_data = data.split("\n\n")

    rules = Rule.parse_rules(rules_data)

    my_ticket = Ticket(my_ticket_data.split("\n")[1])

    other_tickets = []
    for line in other_tickets_data.split("\n")[1:]:
        if line:
            other_tickets.append(Ticket(line))

    return rules, my_ticket, other_tickets


def get_field_lookup(rules, tickets):
    possibilities = {}

    for rule in rules:
        consistently_valid_indexes = set(range(0, len(rules)))
        for ticket in tickets:
            valid_indexes = set(
                [i for i, v in enumerate(ticket.values) if rule.validate(v)]
            )
            consistently_valid_indexes = consistently_valid_indexes.intersection(
                valid_indexes
            )
        possibilities[rule.name] = consistently_valid_indexes

    actual = {}

    for i in range(1, len(rules) + 1):
        for k, v in possibilities.items():
            if len(v) == i:
                index = list(filter(lambda x: x not in actual.keys(), v))[0]
                actual[index] = k

    return actual


if __name__ == "__main__":
    rules, my_ticket, other_tickets = load_data("data")

    # Part 1
    scanning_error_rate = 0
    for ticket in other_tickets:
        for value in ticket.get_invalid_values(rules):
            scanning_error_rate += value
    print(scanning_error_rate)

    # Part 2
    valid_tickets = list(filter(lambda t: t.is_valid(rules), other_tickets))
    field_lookup = get_field_lookup(rules, valid_tickets)
    decoded = my_ticket.decode(field_lookup)

    values = [v for k, v in decoded.items() if k.startswith("departure")]
    print(reduce(lambda x, y: x * y, values, 1))
