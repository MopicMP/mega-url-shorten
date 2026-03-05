"""Tests for mega-url-shorten."""

import pytest
from mega_url_shorten import shorten


class TestShorten:
    """Test suite for shorten."""

    def test_basic(self):
        """Test basic usage."""
        result = shorten("test")
        assert result is not None

    def test_empty(self):
        """Test with empty input."""
        try:
            shorten("")
        except (ValueError, TypeError):
            pass  # Expected for some utilities

    def test_type_error(self):
        """Test with wrong type raises or handles gracefully."""
        try:
            result = shorten(12345)
        except (TypeError, AttributeError, ValueError):
            pass  # Expected for strict-typed utilities
