"""Public package interface for ``chrome_version``.

This package exposes ``get_chrome_version`` for programmatic use.
"""
# Copyright (c) 2023 Hasan Sezer Taşan
# Licensed under the MIT License

from chrome_version.core import get_chrome_version

__all__ = ("get_chrome_version",)
