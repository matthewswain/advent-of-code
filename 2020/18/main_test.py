from main import eval_line_1, eval_line_2


def test_eval_line_1():
    cases = [
        {"input": "7 * 8 + 2 + 8 * (8 * 4) * (4 + 8)", "expected": 25344},
    ]
    for case in cases:
        assert eval_line_1(case["input"]) == case["expected"]


def test_eval_line_2():
    cases = [
        {"input": "1 + (2 * 3) + (4 * (5 + 6))", "expected": 51},
        {"input": "2 * 3 + (4 * 5)", "expected": 46},
        {"input": "5 + (8 * 3 + 9 + 3 * 4 * 3)", "expected": 1445},
        {"input": "5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))", "expected": 669060},
        {"input": "((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2", "expected": 23340},
        {"input": "2 + 4", "expected": 6},
        {"input": "2 * 4", "expected": 8},
        {"input": "10", "expected": 10},
        {
            "input": "3 + 6 * (7 * 8 * 6 * (5 + 8 + 6) + 5 * 4) * ((8 + 9 + 6 * 8) * 9 + 6 * 6 + 2 * 2) * 4",
            "expected": 51279298560,
        },
        {"input": "17 + 7 * 2 * 117 + 71", "expected": 9024},
    ]
    for case in cases:
        assert eval_line_2(case["input"]) == case["expected"]
