"""CLI entrypoint for retrieving the installed Chrome version."""
# Copyright (c) 2023 Hasan Sezer Taşan
# Licensed under the MIT License
# ruff: noqa: T201

import sys

from chrome_version.core import get_chrome_version


def main() -> None:
    """Print the detected Chrome version to stdout.

    This function is used by the ``chrome-version`` console script.
    """
    version = get_chrome_version()
    if version:
        print(version)
        sys.exit(0)
    print(
        "Chrome is not installed or its version could not be detected.", file=sys.stderr
    )
    sys.exit(1)
