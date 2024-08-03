import main

# run a podinfo/httpbin container at test start

def test_test_function():
    assert main.test() == 0

    # raise AssertionError
    # assert False


def test_root_get():
    assert True