from main import expand_grid, get_bounds, update_cube

# .#.
# ..#
# ###
original_grid = {
    (0, 0, 0): False,
    (0, 1, 0): True,
    (0, 2, 0): False,
    (1, 0, 0): False,
    (1, 1, 0): False,
    (1, 2, 0): True,
    (2, 0, 0): True,
    (2, 1, 0): True,
    (2, 2, 0): True,
}


def test_update_cube():
    cases = [
        {"coords": (0, 1, 0), "expected": False},
        {"coords": (1, 2, 0), "expected": True},
        {"coords": (2, 2, -1), "expected": True},
        {"coords": (0, 0, 1), "expected": False},
    ]
    for case in cases:
        assert update_cube(original_grid, *case["coords"]) == case["expected"]


def test_get_bounds():
    assert get_bounds(original_grid) == ((0, 0, 0), (2, 2, 0))


def test_expand_grid():
    grid = expand_grid(original_grid.copy())
    assert get_bounds(grid, include_inactive=True) == ((-1, -1, -1), (3, 3, 1))
