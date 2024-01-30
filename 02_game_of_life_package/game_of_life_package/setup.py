from distutils.core import setup

# WARNING: Also update the version in the init.py file for game-of-life-package
setup(
    name="game_of_life_package",
    version="0.0.1",
    author="Chris Guest",
    author_email="chris@chrisguest.dev",
    packages=["game_of_life_package", "tests"],
    scripts=[],
    url="https://github.com/chrisguest75/python_examples/tree/master/02_game_of_life_package/game_of_life_package",
    license="LICENSE.txt",
    description="A package for creating game of life boards.",
    long_description=open("README.md").read(),
    install_requires=[],
)
