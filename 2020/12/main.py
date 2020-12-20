#! /usr/bin/env python


def load_data(path):
    with open(path) as in_f:
        lines = [line.strip() for line in in_f.readlines()]
        return [(line[0], int(line[1:])) for line in lines]


class Ferry:
    bearing: int
    x: int
    y: int
    waypoint_x: int
    waypoint_y: int

    def __init__(self, bearing: int = 0, waypoint_x: int = 0, waypoint_y: int = 0):
        self.bearing = bearing
        self.x, self.y = 0, 0
        self.waypoint_x, self.waypoint_y = waypoint_x, waypoint_y

    def update(self, action: str, value: int):
        if action == "N":
            self.y += value
        elif action == "S":
            self.y -= value
        elif action == "E":
            self.x += value
        elif action == "W":
            self.x -= value
        elif action == "L":
            self.bearing -= value
            self.bearing = self.bearing % 360
        elif action == "R":
            self.bearing += value
            self.bearing = self.bearing % 360
        elif action == "F":
            directions = {0: "N", 90: "E", 180: "S", 270: "W"}
            self.update(directions[self.bearing], value)

    def update_waypoint(self, action: str, value: int):
        if action == "N":
            self.waypoint_y += value
        elif action == "S":
            self.waypoint_y -= value
        elif action == "E":
            self.waypoint_x += value
        elif action == "W":
            self.waypoint_x -= value
        elif action == "L":
            for i in range(0, int(value / 90)):
                self.waypoint_x, self.waypoint_y = -self.waypoint_y, self.waypoint_x
        elif action == "R":
            for i in range(0, int(value / 90)):
                self.waypoint_x, self.waypoint_y = self.waypoint_y, -self.waypoint_x
        elif action == "F":
            self.x += self.waypoint_x * value
            self.y += self.waypoint_y * value

    def manhattan_position(self):
        return abs(self.x) + abs(self.y)


if __name__ == "__main__":
    instructions = load_data("data")

    # Part 1
    ferry = Ferry(90)

    for action, value in instructions:
        ferry.update(action, value)

    print(ferry.manhattan_position())

    # Part 2
    ferry = Ferry(90, 10, 1)

    for action, value in instructions:
        ferry.update_waypoint(action, value)

    print(ferry.manhattan_position())
