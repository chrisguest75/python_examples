from torch_test_package import checks


def test_test_function():
    print(dir(checks))
    checks.is_cuda()
    checks.is_working()

    assert False == True

    # raise AssertionError
    # assert False
