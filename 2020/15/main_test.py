from main import Game


def test_next_turn():
    game = Game(0, 3, 6)
    for number in [0, 3, 3, 1, 0, 4, 0]:
        assert game.next_turn() == number
