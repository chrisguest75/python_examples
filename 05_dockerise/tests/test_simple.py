from main import fibonacci_sequence


def test_fibonacci_sequence():
    g = fibonacci_sequence()
    assert [0, 1, 1, 2, 3, 5, 8] == [next(g) for _ in range(7)]
