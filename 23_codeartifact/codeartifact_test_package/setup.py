from distutils.core import setup

# WARNING: Also update the version in the init.py file for package
setup(
    name="codeartifact_test_package",
    version="0.0.2",
    author="Chris Guest",
    author_email="chris@chrisguest.dev",
    packages=["codeartifact_test_package"],
    scripts=[],
    url="https://github.com/chrisguest75/python_examples/tree/master/23_codeartifact_test_package/codeartifact_test_package",
    license="LICENSE.txt",
    description="A simple test for publishing to CodeArtifact",
    long_description=open("README.md").read(),
    install_requires=[],
)
