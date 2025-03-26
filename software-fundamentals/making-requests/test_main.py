"""Tests for the API-related code in main."""

import re

import pytest

from main import get_user_repo_count


def test_get_user_repo_count_returns_int(requests_mock):
    """Checks that the function returns an integer."""

    # Ensure that, if a request is made to the outside world, it is intercepted
    # You need to fake the request well enough not to be detected
    requests_mock.get("https://api.github.com/users/zertidana",
                      status_code=200, json={"public_repos": 3})

    result = get_user_repo_count("zertidana")

    assert isinstance(result, int)


def test_get_user_repo_count_raises_error_on_404(requests_mock):
    """Checks that the function returns an integer."""

    # Ensure that, if a request is made to the outside world, it is intercepted
    # You need to fake the request well enough not to be detected
    pattern = re.compile("https://api.github.com/users/.+")

    requests_mock.get(pattern,
                      status_code=404)

    with pytest.raises(ValueError):
        get_user_repo_count("zertikyle")
