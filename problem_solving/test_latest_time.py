# pylint: skip-file
import pytest

from latest_time import (get_first_digit,
                         get_second_digit,
                         get_third_digit,
                         find_latest_time)


def test_get_first_digit_returns_zero():
    assert get_first_digit([0, 9, 3, 8]) == 0


def test_get_first_digit_returns_one():
    assert get_first_digit([1, 9, 8, 3]) == 1


def test_get_first_digit_returns_two():
    assert get_first_digit([9, 1, 2, 5]) == 2

<<<<<<< HEAD

def test_get_third_digit_returns_five():
    assert get_third_digit([5, 1,]) == 5


@pytest.mark.parametrize("digits,second,expected",
                         [([9, 1, 5], 2, 5),
=======
@pytest.mark.parametrize("digits,second,expected", 
                         [([9, 1, 5], 2, 1),
>>>>>>> 5688994e15ef2b2d4da976494a0c5f1af9cad6c3
                          ([9, 8, 3], 1, 9)])
def test_get_second_digit_returns_five(digits, second, expected):
    assert get_second_digit(digits, second) == expected

def test_find_latest_time_base_case():
    assert find_latest_time([1, 9, 8, 3]) == "19:38"

def test_find_latest_time_base_case_two_option():
    assert find_latest_time([9, 1, 2, 5]) == "21:59"
    
def test_get_first_digit_but_no_zero_one_or_two():
    with pytest.raises(ValueError):
        get_first_digit([9, 8, 6, 7])

def test_get_second_digit_returns_zero():
    assert get_second_digit([4, 9, 0], 2) == 0

def test_get_second_digit_returns_three_when_first_is_two():
    assert get_second_digit([2, 3, 3, 1], 2) == 3

def test_get_second_digit_after_one():
    assert get_second_digit([1, 2, 5], 1) == 5

def test_get_second_digit_returns_one_when_first_digit_is_two():
    assert get_second_digit([1, 1, 0], 2) == 1

def test_get_third_digit_returns_five():
    assert get_third_digit([5, 9]) == 5

