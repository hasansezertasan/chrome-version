"""Tests for the runnable entrypoint (``python -m chrome_version``)."""

from __future__ import annotations

import importlib


def test_main_entrypoint_is_callable() -> None:
    """``chrome_version.__main__`` re-exports the CLI's callable ``main``."""
    main_module = importlib.import_module("chrome_version.__main__")

    assert callable(main_module.main)
