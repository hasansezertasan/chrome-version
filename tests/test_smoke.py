"""Smoke tests for chrome_version package."""


def test_smoke() -> None:
    """Test that the package can be imported."""
    import chrome_version  # noqa: PLC0415

    assert chrome_version is not None
