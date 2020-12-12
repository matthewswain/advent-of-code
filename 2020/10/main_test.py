from main import count_possible_chains, prepare_data


def test_count_chains():
    adapters = prepare_data([16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4])
    assert count_possible_chains(adapters, 0) == 8
