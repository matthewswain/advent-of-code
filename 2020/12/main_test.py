from main import Ferry


def test_ferry():
    ferry = Ferry(90)
    instructions = [
        ("F", 10),
        ("N", 3),
        ("F", 7),
        ("R", 90),
        ("F", 11),
    ]

    for action, value in instructions:
        ferry.update(action, value)

    assert ferry.manhattan_position() == 25


def test_waypoint():
    ferry = Ferry(90, 10, 1)
    instructions = [
        ("F", 10),
        ("N", 3),
        ("F", 7),
        ("R", 90),
        ("F", 11),
    ]

    for action, value in instructions:
        ferry.update_waypoint(action, value)

    assert ferry.manhattan_position() == 286

