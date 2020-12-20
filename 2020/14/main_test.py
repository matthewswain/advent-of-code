from main import Program


def test_apply_mask():
    cases = [
        {
            "bitmask": "XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X",
            "number": 11,
            "expected": 73,
        },
        {
            "bitmask": "XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X",
            "number": 101,
            "expected": 101,
        },
        {
            "bitmask": "XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X",
            "number": 0,
            "expected": 64,
        },
    ]
    for case in cases:
        assert case["expected"] == Program.apply_mask(case["bitmask"], case["number"])


def test_program():
    instructions = [
        "mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X",
        "mem[8] = 11",
        "mem[7] = 101",
        "mem[8] = 0",
    ]
    program = Program()
    program.run(instructions)
    assert program.memory[7] == 101
    assert program.memory[8] == 64
