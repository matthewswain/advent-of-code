from main import eval_line


def test_eval_line():
    cases = [
        {"input": "7 * 8 + 2 + 8 * (8 * 4) * (4 + 8)", "expected": 25344},
    ]
    for case in cases:
        assert eval_line(case["input"]) == case["expected"]
