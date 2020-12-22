#! /usr/bin/env python


from itertools import combinations
from typing import Dict, List, Set


def load_data(path: str):
    with open(path) as in_f:
        return [line.strip() for line in in_f.readlines()]


class Program:
    memory: Dict[int, int]
    bitmask: str

    def __init__(self):
        self.memory = {}
        self.bitmask = "X" * 36

    def update_mask(self, bitmask: str):
        self.bitmask = bitmask

    def update_memory(self, address: int, value: int):
        self.memory[address] = self.apply_mask(self.bitmask, value)

    def step(self, instruction: str):
        k, v = instruction.split(" = ")
        if k.startswith("mem"):
            address = int(k[4 : len(k) - 1])
            self.update_memory(address, int(v))
        elif k == "mask":
            self.update_mask(v)
        else:
            raise ValueError(f"Unexpected instruction: {instruction}")

    def run(self, instructions: List[str]):
        for instruction in instructions:
            self.step(instruction)

    def total(self) -> int:
        return sum(self.memory.values())

    @staticmethod
    def apply_mask(bitmask: str, number: int) -> int:
        on = int(bitmask.replace("X", "0"), 2)
        off = int(bitmask.replace("X", "1"), 2)
        return (number & off) | on


class ProgramV2:
    memory: Dict[int, int]
    bitmask: str

    def __init__(self):
        self.memory = {}
        self.bitmask = "0" * 36

    def update_mask(self, bitmask: str):
        self.bitmask = bitmask

    def update_memory(self, address: int, value: int):
        addresses = self.apply_mask(self.bitmask, address)
        for address in addresses:
            self.memory[address] = value

    def step(self, instruction: str):
        k, v = instruction.split(" = ")
        if k.startswith("mem"):
            address = int(k[4 : len(k) - 1])
            self.update_memory(address, int(v))
        elif k == "mask":
            self.update_mask(v)
        else:
            raise ValueError(f"Unexpected instruction: {instruction}")

    def run(self, instructions: List[str]):
        for instruction in instructions:
            self.step(instruction)

    def total(self) -> int:
        return sum(self.memory.values())

    @staticmethod
    def apply_mask(bitmask: str, number: int) -> Set[int]:
        numbers = set()

        on = int(bitmask.replace("X", "0"), 2)
        number = number | on
        numbers.add(number)

        masks = []
        for i, c in enumerate(bitmask):
            if c == "X":
                mask = 2 ** (len(bitmask) - (i + 1))
                masks.append((mask, True))
                masks.append((~mask, False))

        mask_combinations = []
        for i in range(1, len(masks) + 1):
            list(map(lambda x: mask_combinations.append(x), combinations(masks, i)))

        for combination in mask_combinations:
            masked_number = number
            for mask, on in combination:
                if on:
                    masked_number = masked_number | mask
                else:
                    masked_number = masked_number & mask
            numbers.add(masked_number)

        return numbers


if __name__ == "__main__":
    instructions = load_data("data")

    # Part 1
    program = Program()
    program.run(instructions)
    print(program.total())

    # Part 2
    program = ProgramV2()
    program.run(instructions)
    print(program.total())
