from datetime import datetime
from unittest.mock import patch

import pytest

from main import Horse, Stable, is_it_the_weekend, predict_future


def test_stable_horse_list_contains_horses(test_herd):

    test_stable = Stable(test_herd)

    assert isinstance(test_stable.horses[0], Horse)


def test_stable_horse_list_contains_3_horses(test_herd):

    test_stable = Stable(test_herd)

    assert len(test_stable.horses) == 3


def test_stable_raises_error_on_insufficient_horses():

    with pytest.raises(ValueError):
        Stable([])


def test_stable_raises_error_on_not_horses():

    with pytest.raises(TypeError):
        Stable([3, 3, 3])


@patch("main.datetime")
def test_is_it_the_weekend_accurate(fake_datetime):

    fake_now = fake_datetime.now.return_value
    fake_now.weekday = 7

    assert is_it_the_weekend()


@patch("main.randint")
def test_predict_future_says_yes_correctly(fake_randint):

    fake_randint.return_value = 1

    assert predict_future("Will I ever be able to rest?") == "Yes!!"