"""Definitions for things used by multiple tests."""

import pytest

from main import Horse

@pytest.fixture # Make this available to all tests
def test_herd():
    """Returns a new set of horses."""
    return [Horse("Harriet", "golden"),
            Horse("Roach", "brown"),
            Horse("Shadowfax", "white")]