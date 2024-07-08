from torch_test_package import checks
import importlib.metadata

def test_test_function():
    print(dir(checks))
    print(f'importlib.metadata.version("torch_test_package"): {importlib.metadata.version("torch_test_package")}')
    checks.is_cuda()
    checks.is_working()

