"""Basic tests for the cost_overruns package."""

import pytest

from cost_overruns import __version__
from cost_overruns.simulation import hello


def test_hello() -> None:
    """Test that the hello function returns the expected string."""
    assert hello() == "cost_overruns"


def test_version() -> None:
    """Test that the package version is defined."""
    assert __version__ == "0.1.0"
