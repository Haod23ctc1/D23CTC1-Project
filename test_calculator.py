import pytest

from calculator import add, divide, is_positive, multiply, subtract


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0


def test_subtract():
    assert subtract(10, 4) == 6
    assert subtract(3, 9) == -6


def test_multiply():
    assert multiply(4, 5) == 20
    assert multiply(-2, 6) == -12


def test_divide():
    assert divide(10, 2) == 5
    assert divide(9, 3) == 3


def test_is_positive():
    assert is_positive(5) == True
    assert is_positive(-3) == False
    with pytest.raises(ValueError):
        is_positive(0)
