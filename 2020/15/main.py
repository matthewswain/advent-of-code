#! /usr/bin/env python

from typing import Dict


class Game:
    history: Dict[int, int]
    previous_number: int
    turn: int

    def __init__(self, *starting_numbers: int):
        self.turn = 0
        self.history = {}

        for number in starting_numbers[:-1]:
            self.turn += 1
            self.history[number] = self.turn

        self.turn += 1
        self.previous_number = starting_numbers[-1]

    def next_turn(self):
        self.turn += 1

        next_number = 0
        if last_seen := self.history.get(self.previous_number):
            next_number = self.turn - 1 - last_seen

        self.history[self.previous_number] = self.turn - 1
        self.previous_number = next_number

        return next_number

    def play_to_turn(self, turn: int):
        while self.turn < turn:
            self.next_turn()
        return self.previous_number


if __name__ == "__main__":
    game = Game(9, 6, 0, 10, 18, 2, 1)

    # Part 1
    print(game.play_to_turn(2020))

    # Part 2
    print(game.play_to_turn(30000000))
