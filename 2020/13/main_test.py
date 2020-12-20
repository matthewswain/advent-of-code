from main import find_pattern, lcm


def test_find_pattern():
    cases = [
        ([17, None, 13, 19], 3_417),
        ([67, 7, 59, 61], 754_018),
    ]
    for busses, expected in cases:
        assert find_pattern(busses) == expected
