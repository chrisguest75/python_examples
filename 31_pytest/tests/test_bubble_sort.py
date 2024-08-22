import bubblesort


def test_reversed():
    assert bubblesort.sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]


def test_empty():
    assert bubblesort.sort([]) == []


def test_single():
    assert bubblesort.sort([10]) == [10]


def test_same():
    assert bubblesort.sort([1, 1, 1]) == [1, 1, 1]


def test_normal():
    assert bubblesort.sort([1, 6, 8, 1, 2, 4, 3]) == [1, 1, 2, 3, 4, 6, 8]
