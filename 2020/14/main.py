#! /usr/bin/env python


from typing import Dict, List


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


if __name__ == "__main__":
    instructions = load_data("data")

    program = Program()
    program.run(instructions)

    # Part 1
    print(program.total())
