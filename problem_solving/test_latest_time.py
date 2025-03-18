import pytest

from latest_time import (get_first_digit,
                         get_second_digit,
                         get_third_digit)


def test_get_first_digit_returns_zero():
    assert get_first_digit([0, 9, 3, 8]) == 0


def test_get_first_digit_returns_one():
    assert get_first_digit([1, 9, 8, 3]) == 1


def test_get_first_digit_returns_two():
    assert get_first_digit([9, 1, 2, 5]) == 2


def test_get_third_digit_returns_five():
    assert get_third_digit([5, 1,]) == 5


@pytest.mark.parametrize("digits,second,expected",
                         [([9, 1, 5], 2, 5),
                          ([9, 8, 3], 1, 9)])
def test_get_second_digit_returns_five(digits, second, expected):
    assert get_second_digit(digits, second) == expected
