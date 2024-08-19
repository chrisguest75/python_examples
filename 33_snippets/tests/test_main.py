import main


def test_test_function():
    assert main.test() == 0

    # raise AssertionError
    # assert False

def test_baseline_indented_comments():
    count = 0
    iterations = 0
    for i in range(0, 10):
        assert i == count
        count += 1

        ## comments
        ## stuff

        assert i + 1 == count
        iterations += 1

    assert 10 == iterations

def test_under_indented_comments():
    count = 0
    iterations = 0
    for i in range(0, 10):
        assert i == count
        count += 1

    ## comments
    ## stuff

        assert i + 1 == count
        iterations += 1

    assert 10 == iterations

def test_over_indented_comments():
    count = 0
    iterations = 0
    for i in range(0, 10):
        assert i == count
        count += 1

            ## comments
            ## stuff

        assert i + 1 == count
        iterations += 1

    assert 10 == iterations

def test_mixed_indented_comments():
    count = 0
    iterations = 0
    for i in range(0, 10):
        assert i == count
        count += 1

    ## comments
                ## stuff

        assert i + 1 == count
        iterations += 1

    assert 10 == iterations

def test_indentation():
    count = 0
    iterations = 0
    for i in range(0, 10):
        assert i == count
        count += 1

        ## comments
        ## stuff

    assert i + 1 == count
    iterations += 1

    assert 10 == iterations