"""A place to build things used by multiple tests."""

import pytest

from main import api

@pytest.fixture
def test_api():
    """Returns a clean copy of the test API."""

    return api.test_client()