import main
import pytest
from fruit import Fruit

def test_test_function():
    assert main.test() == 0


def test_fruit_type_checking_passes():
    Fruit(
        name='Apple',
        color='red',
        weight=4.2,
        bazam={'foobar': [(1, True, 0.1)]},
    )


def test_fruit_type_checking_fails():
    with pytest.raises(Exception):
        Fruit(
            name='Apple',
            color='blue',
            weight=4.2,
            bazam={'foobar': [(1, True, 0.1)]},
        )
