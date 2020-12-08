#! /usr/bin/env python


def parse_line(line):
    parts = line.strip().split()
    return parts[0], int(parts[1])


def load_data(path):
    with open(path) as in_f:
        lines = in_f.readlines()
        return list(map(parse_line, lines))


def run(code):
    visited = []
    position = 0
    accumulator = 0
    while True:
        visited.append(position)
        instruction, value = code[position]

        if instruction == "nop":
            position += 1
        elif instruction == "acc":
            accumulator += value
            position += 1
        elif instruction == "jmp":
            position += value
        else:
            raise ValueError("invalid instruction")

        if position in visited:
            return -1, accumulator
        if position >= len(code):
            return 0, accumulator


def fix_and_run(code):
    for i in range(0, len(code)):
        instruction, value = code[i]
        if instruction == "acc":
            continue
        modified = code.copy()
        modified[i] = ("jmp", value) if instruction == "nop" else ("nop", value)
        rc, accumulator = run(modified)
        if rc == 0:
            return (rc, accumulator)


if __name__ == "__main__":
    code = load_data("data")

    # Part 1
    print(run(code))

    # Part 2
    print(fix_and_run(code))
