#! /usr/bin/env python

from typing import List


class Game:
    numbers: List[int]

    def __init__(self, *starting_numbers: int):
        self.numbers = list(starting_numbers)

    def next_turn(self):
        last_number = self.numbers[-1]
        next_number = 0
        for i, number in enumerate(reversed(self.numbers[:-1])):
            if number == last_number:
                next_number = i + 1
                break
        self.numbers.append(next_number)
        return next_number

    def play_to_turn(self, turn: int):
        while len(self.numbers) < turn:
            self.next_turn()
        return self.numbers[-1]


if __name__ == "__main__":
    game = Game(9, 6, 0, 10, 18, 2, 1)

    # Part 1
    print(game.play_to_turn(2020))

    # Part 2
    print(game.play_to_turn(30000000))
