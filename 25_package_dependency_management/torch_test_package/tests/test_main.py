from src.torch_test_package import checks


def test_checks():
    print(dir(checks))
    checks.is_cuda()
    checks.is_working()

    #assert False == True

