#! /usr/bin/env python

from typing import List


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

    @staticmethod
    def parse_rules(data):
        rules = []
        lines = data.strip().split("\n")
        for line in lines:
            rules.append(Rule(line))
        return rules


class Ticket:
    values: List[int]

    def __init__(self, line: str):
        self.values = [int(n) for n in line.strip().split(",")]

    def get_invalid_values(self, rules: List[Rule]):
        for value in self.values:
            invalid = True
            for rule in rules:
                for valid_range in rule.ranges:
                    if valid_range.minimum <= value <= valid_range.maximum:
                        invalid = False
            if invalid:
                yield value


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


if __name__ == "__main__":
    rules, my_ticket, other_tickets = load_data("data")

    # Part 1
    scanning_error_rate = 0
    for ticket in other_tickets:
        for value in ticket.get_invalid_values(rules):
            scanning_error_rate += value
    print(scanning_error_rate)
