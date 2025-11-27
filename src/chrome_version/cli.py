"""CLI entrypoint for retrieving the installed Chrome version."""
# Copyright (c) 2023 Hasan Sezer Taşan <hasansezertasan@gmail.com>
# Licensed under the MIT License

import platform
import sys
from typing import Optional

from chrome_version._version import version
from chrome_version.core import get_chrome_version


def main() -> None:
    """Print the detected Chrome version to stdout.

    This function is used by the ``chrome-version`` console script.
    """
    if "--info" in sys.argv:
        python_version: str = platform.python_version()
        python_implementation: str = platform.python_implementation()
        print(f"Application Version: {version}")
        print(f"Python Version: {python_version} ({python_implementation})")
        print(f"Platform: {platform.system()}")
        sys.exit(0)
    if "--version" in sys.argv:
        print(version)
        sys.exit(0)
    chrome_version: Optional[str] = get_chrome_version()
    if chrome_version:
        print(chrome_version)
        sys.exit(0)
    print(
        "Chrome is not installed or its version could not be detected.", file=sys.stderr
    )
    sys.exit(1)
