#! /usr/bin/env python

from functools import partial
from math import lcm
from typing import Dict, List


def load_data(path: str) -> (int, List[int]):
    with open(path) as in_f:
        lines = [line.strip() for line in in_f.readlines()]
        departure = int(lines[0])
        busses = map(lambda b: None if b == "x" else int(b), lines[1].split(","))
    return departure, list(busses)


def departure_after(bus: int, after: int):
    departure = 0
    while departure < after:
        departure += bus
    return departure


def departures_after(busses: List[int], after: int) -> Dict[int, int]:
    times = map(partial(departure_after, after=after), busses)
    return dict(zip(busses, times))


def earliest_departure(departures: Dict[int, int]) -> (int, int):
    bus = min(departures.keys(), key=(lambda k: departures[k]))
    return bus, departures[bus]


def find_pattern(busses: List[int]) -> int:
    t = 0
    step = busses[0]

    for offset, bus in enumerate(busses):
        if not bus:
            continue

        while (t + offset) % bus != 0:
            t += step

        step = lcm(step, bus)

    return t


if __name__ == "__main__":
    departure, busses = load_data("data")

    # Part 1
    departures = departures_after([b for b in busses if b], departure)
    bus, bus_departure = earliest_departure(departures)
    print(bus * (bus_departure - departure))

    # Part 2
    print(find_pattern(busses))
