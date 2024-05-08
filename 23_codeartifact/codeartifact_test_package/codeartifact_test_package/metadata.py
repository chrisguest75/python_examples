import codeartifact_test_package

def get_metadata():
    return {
        'name': 'codeartifact-test-package',
        'version': codeartifact_test_package.__version__,
        'description': 'A test package for CodeArtifact',
    }